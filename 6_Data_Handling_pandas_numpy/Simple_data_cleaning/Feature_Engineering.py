class FeatureEngineer:
    def __init__(self, df):
        self.df = df.copy()

    def create_features(self):
        self.df["salary_per_experience"] = (
            self.df["salary"] / (self.df["experience"] + 1)
        )
        self.df["is_experienced"] = self.df["experience"] > 2
        return self

    def prepare_features(self, target_column):
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        return X, y
