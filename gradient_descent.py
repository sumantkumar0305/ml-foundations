class gd_for_n_dim:
    def __init__(self, epoch=160, learningRate=0.01):
        self.coef = None
        self.intercept = None
        self.epoch = epoch
        self.LR = learningRate
  
    def fit(self, X_train, y_train):
        n, d = X_train.shape
        self.intercept = 0
        self.coef = np.ones(d)

        for i in range(self.epoch):
            y_hat = np.dot(X_train, self.coef) + self.intercept
            error = y_train - y_hat

            # Gradients
            inter_slope = (-2/n) * np.sum(error)
            coef_slope = (-2/n) * np.dot(X_train.T, error)

            # Updates
            self.intercept -= self.LR * inter_slope
            self.coef -= self.LR * coef_slope

        print("Intercept:", self.intercept)
        print("Coefficients:", self.coef)
