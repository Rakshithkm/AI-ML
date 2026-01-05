# Day 03 - Model Class
# Author: Rakshith

class SimpleModel:
    def __init__(self):
        self.is_trained = False

    def train(self, data):
        print("Training model on data...")
        self.is_trained = True

    def predict(self, X):
        if not self.is_trained:
            raise Exception("Model is not trained yet!")
        return [1 for _ in X]
