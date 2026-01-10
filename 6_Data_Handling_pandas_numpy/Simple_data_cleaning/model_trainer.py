from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class ModelTrainer:
    def __init__(self, test_size=0.2, random_state=42):
        self.test_size = test_size
        self.random_state = random_state
        self.model = LogisticRegression()
        self.is_trained = False

    def split_data(self, X, y):
        return train_test_split(
            X, y,
            test_size=self.test_size,
            random_state=self.random_state
        )

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        self.is_trained = True
