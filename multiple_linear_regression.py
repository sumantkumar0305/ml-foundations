import numpy as np

class OwnMultipleLR:
    def __init__(self):
        self.intercept = None
        self.coeff = None

    def fit(self, x_train, y_train):
        # Add column of ones for intercept
        X = np.insert(x_train, 0, 1, axis=1)
        
        # Closed-form solution using pseudo-inverse
        bheta = np.linalg.pinv(X.T @ X) @ X.T @ y_train

        self.intercept = bheta[0]
        self.coeff = bheta[1:]

    def predict(self, x_test):
        return x_test @ self.coeff + self.intercept
