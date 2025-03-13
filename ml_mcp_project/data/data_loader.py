from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def load_data():
    data = load_breast_cancer()
    return train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    ) 