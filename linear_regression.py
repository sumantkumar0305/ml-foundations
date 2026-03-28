class OwnLR:

    def __init__(self):
        self.m = None
        self.b = None

    def fit(self, x_train, y_train):
        y_bar = y_train.mean()
        x_bar = x_train.mean()

        num = 0
        den = 0

        for i in range(x_train.shape[0]):
            a = x_train.iloc[i] - x_bar
            b = y_train.iloc[i] - y_bar

            num = num + a * b
            den = den + a ** 2

        self.m = num / den
        self.b = y_bar - self.m * x_bar

    def predict(self, x_test):
        return self.m * x_test + self.b
