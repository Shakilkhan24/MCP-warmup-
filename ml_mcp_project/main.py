import mlflow
from server.server import mcp

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("XGBoost Experiment")
    mcp.run() 