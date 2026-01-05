# Day 03 - ML Pipeline
# Author: Rakshith

from dataset import Dataset
from model import SimpleModel

data = [1, 2, None, 4, 5, None, 6]

dataset = Dataset(data)
dataset.summary()

dataset.remove_missing()
print("After cleaning:", dataset.data)

model = SimpleModel()
model.train(dataset.data)

predictions = model.predict(dataset.data)
print("Predictions:", predictions)
