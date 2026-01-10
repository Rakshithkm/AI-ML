from sklearn.metrics import accuracy_score, classification_report


class Evaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)

        return accuracy, report
