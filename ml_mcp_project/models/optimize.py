import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import optuna
import xgboost as xgb
from sklearn.metrics import accuracy_score
from data.data_loader import load_data

X_train, X_test, y_train, y_test = load_data()

def optimize_hyperparameters(n_trials: int = 10) -> str:
    def objective(trial):
        params = {
            'max_depth': trial.suggest_int('max_depth', 2, 10),
            'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3),
            'n_estimators': trial.suggest_int('n_estimators', 50, 200),
            'objective': 'binary:logistic'
        }
        model = xgb.XGBClassifier(**params)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        return accuracy_score(y_test, y_pred)
    
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=n_trials)
    return f"Best hyperparameters: {study.best_params} with accuracy: {study.best_value:.4f}" 