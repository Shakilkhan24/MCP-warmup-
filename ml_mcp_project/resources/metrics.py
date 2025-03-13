import mlflow

def get_latest_metrics() -> dict:
    client = mlflow.tracking.MlflowClient()
    runs = client.search_runs(experiment_ids=["0"], max_results=1)
    if not runs:
        return {"error": "No runs found"}
    return runs[0].data.metrics 