import mlflow

def get_best_model() -> str:
    client = mlflow.tracking.MlflowClient()
    runs = client.search_runs(
        experiment_ids=["0"],
        order_by=["metrics.accuracy DESC"],
        max_results=1
    )
    if not runs:
        return "No models found"
    return f"Best model run ID: {runs[0].info.run_id}" 