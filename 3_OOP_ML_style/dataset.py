# Day 03 - Dataset Class
# Author: Rakshith

class Dataset:
    def __init__(self, data):
        self.data = data
        
    def summary(self):
        print(f"Total samples: {len(self.data)}")
        print(f"First 5 samples: {self.data[:5]}")
        
    def remove_missing(self):
        clean_data = []
        for value in self.data:
            if value is not None:
                clean_data.append(value)
        self.data = clean_data