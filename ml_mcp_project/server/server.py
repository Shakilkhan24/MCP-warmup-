from mcp.server.fastmcp import FastMCP
from models import train, optimize
from resources import metrics, model
from prompts import training, optimization

mcp = FastMCP("ML MCP Project", dependencies=["xgboost", "mlflow", "optuna"])

# Register tools
mcp.tool()(train.train_model)
mcp.tool()(optimize.optimize_hyperparameters)

# Register resources
mcp.resource("metrics://latest")(metrics.get_latest_metrics)
mcp.resource("model://best")(model.get_best_model)

# Register prompts
mcp.prompt("explain-training")(training.explain_training_prompt)
mcp.prompt("explain-optimization")(optimization.explain_optimization_prompt) 