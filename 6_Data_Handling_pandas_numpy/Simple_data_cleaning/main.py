from data_loader import DataLoader
from data_cleaner import DataCleaner
from Feature_Engineering import FeatureEngineer
from model_trainer import ModelTrainer
from evaluator import Evaluator

# 1. Load data
df = DataLoader().load_sample_data()

# 2. Clean data
clean_df = (
    DataCleaner(df)
    .handle_missing_values()
    .remove_invalid_rows()
    .get_clean_data()
)

# 3. Feature engineering
X, y = (
    FeatureEngineer(clean_df)
    .create_features()
    .prepare_features("purchased")
)

# 4. Train model
trainer = ModelTrainer()
X_train, X_test, y_train, y_test = trainer.split_data(X, y)
trainer.train(X_train, y_train)

# 5. Evaluate model
evaluator = Evaluator(trainer.model)
accuracy, report = evaluator.evaluate(X_test, y_test)

print("Accuracy:", accuracy)
print("\nClassification Report:\n", report)
