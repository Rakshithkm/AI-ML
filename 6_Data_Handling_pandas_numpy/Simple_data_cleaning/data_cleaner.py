import numpy as np

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()

    def handle_missing_values(self):
        for col in self.df.select_dtypes(include=np.number):
            self.df[col].fillna(self.df[col].median(), inplace=True)
        return self

    def remove_invalid_rows(self):
        self.df = self.df[self.df["age"] >= 0]
        return self

    def get_clean_data(self):
        return self.df
