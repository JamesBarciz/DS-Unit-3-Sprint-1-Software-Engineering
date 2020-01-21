# Make at least one class for the Python Package made last module

# Importations from original python script
    from sklearn.model_selection import train_test_split
    import pandas as pd


class Wrangle():
    def __init__(self, data, target):
        self.data = data
        self.target = target
    
    def train_val_test_split(self):
        train, test = train_test_split(self.data, random_state=42)
        train, val = train_test_split(train, random_state=42)
        for df in train, val, test:
            X_train, X_val, X_test = df.drop(columns=self.target)

        for df in train, val:
            y_train, y_val = df[self.target]

        return X_train, y_train, X_val, y_val, X_test
