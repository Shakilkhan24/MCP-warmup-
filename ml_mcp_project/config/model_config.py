from pydantic import BaseModel, Field

class ModelConfig(BaseModel):
    max_depth: int = Field(3, description="Maximum depth of a tree")
    learning_rate: float = Field(0.1, description="Boosting learning rate")
    n_estimators: int = Field(100, description="Number of boosting rounds")
    objective: str = Field("binary:logistic", description="Objective function") 