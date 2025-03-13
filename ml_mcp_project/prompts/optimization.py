def explain_optimization_prompt(question: str) -> str:
    return f"""
    Hyperparameter optimization using Optuna works as follows:
    1. A search space is defined for each hyperparameter
    2. Optuna suggests parameter combinations
    3. Models are trained and evaluated for each combination
    4. The process continues for the specified number of trials
    5. The best performing parameters are selected
    
    Your specific question: {question}
    """ 