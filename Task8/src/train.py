import argparse
import joblib
import os
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from .utils import load_csv_from_dir, preprocess, split


def train_and_save(model_type='xgb', model_path='models/model.joblib'):
    df = load_csv_from_dir('data')
    X, y = preprocess(df)
    X_train, X_val, y_train, y_val = split(X, y)


    if model_type == 'xgb':
        model = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1)
    else:
        model = RandomForestRegressor(n_estimators=100)


    model.fit(X_train, y_train)
    preds = model.predict(X_val)
    rmse = mean_squared_error(y_val, preds)


    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump({'model': model, 'rmse': rmse}, model_path)
    print(f"Saved model to {model_path}, val_rmse={rmse:.4f}")
    return rmse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-type', default='xgb')
    parser.add_argument('--model-path', default='models/model.joblib')
    args = parser.parse_args()
    train_and_save(args.model_type, args.model_path)