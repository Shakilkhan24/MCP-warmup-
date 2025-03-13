import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import xgboost as xgb
import mlflow
from sklearn.metrics import accuracy_score
from data.data_loader import load_data
from config.model_config import ModelConfig


X_train, X_test, y_train, y_test = load_data()

def train_model(config: ModelConfig) -> str:
    mlflow.set_tracking_uri("http://localhost:5000")
    with mlflow.start_run():
        mlflow.log_params(config.dict())
        model = xgb.XGBClassifier(**config.dict())
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.xgboost.log_model(model, "model")
        return f"Model trained with accuracy: {accuracy:.4f}"

x = train_model(ModelConfig(
    max_depth=2,
    learning_rate=0.20218480200547248,
    objective="binary:logistic",
    n_estimators=188
))
print(x) 