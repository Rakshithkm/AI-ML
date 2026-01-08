from data_loader import DataLoader
from data_cleaner import DataCleaner
from Feature_Engineering import FeatureEngineer

loader = DataLoader()
df = loader.load_sample_data()

clean_df = (
    DataCleaner(df)
    .handle_missing_values()
    .remove_invalid_rows()
    .get_clean_data()
)

X, y = (
    FeatureEngineer(clean_df)
    .create_features()
    .prepare_features("purchased")
)

print("Features:")
print(X)
print("\nTarget:")
print(y)
