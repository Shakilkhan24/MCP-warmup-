def explain_training_prompt(question: str) -> str:
    return f"""
    The model training process involves the following steps:
    1. Data is split into training and test sets
    2. An XGBoost model is initialized with the specified configuration
    3. The model is trained on the training data
    4. The model's performance is evaluated on the test data
    5. Metrics and the model are logged using MLflow
    
    Your specific question: {question}
    """ 