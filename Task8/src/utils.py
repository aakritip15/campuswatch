import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os, glob


def load_csv_from_dir(path='data'):
    csvs = glob.glob(os.path.join(path, '*.csv'))
    if not csvs:
        raise FileNotFoundError('No CSV found in data/')
    df = pd.read_csv(csvs[0])
    return df


def preprocess(df):
    df = df.dropna()
    X = df.select_dtypes(include=[np.number]).copy()
    if 'bandwidth' in df:
        y = df['bandwidth'].values
        X = X.drop(columns=['bandwidth'], errors=False)
    elif 'target' in df:
        y = df['target'].values
        X = X.drop(columns=['target'], errors=False)
    else:
        y = X.iloc[:, -1].values
        X = X.iloc[:, :-1]
    return X, y


def split(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)