import pandas as pd

class DataLoader:
    def __init__(self, filepath=None):
        self.filepath = filepath

    def load_sample_data(self):
        data = {
            "age": [22, None, 35, 28, None],
            "salary": [30000, 50000, None, 45000, 40000],
            "experience": [0, 5, 10, None, 3],
            "purchased": [0, 1, 1, 0, 1]
        }
        return pd.DataFrame(data)
