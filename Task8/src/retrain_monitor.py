import os
import hashlib
import json
import subprocess
from glob import glob


STATE_FILE = 'models/.retrain_state.json'


def file_hash(path):
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
         h.update(chunk)
    return h.hexdigest()


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    return json.load(open(STATE_FILE))


def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    json.dump(state, open(STATE_FILE, 'w'))


def find_data_files(data_dir='data'):
    return sorted(glob(os.path.join(data_dir, '*.csv')))


def main():
    state = load_state()
    files = find_data_files()
    changed = False
    new_hashes = {}


    for f in files:
        h = file_hash(f)
        new_hashes[f] = h
        if state.get('files', {}).get(f) != h:
         changed = True


    if changed:
        print('Change detected in data files. Triggering retrain...')
        subprocess.check_call(['python', '-m', 'src.train', '--model-type', 'xgb'])
        state['files'] = new_hashes
        save_state(state)
    else:
     print('No change detected.')


if __name__ == '__main__':
    main()