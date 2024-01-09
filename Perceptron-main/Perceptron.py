from math import exp

class Perceptron():
    def __init__(self, w1, w2, bias, epoch, rate):
        self.w1 = w1      # Weight for the first input
        self.w2 = w2      # Weight for the second input
        self.bias = bias  # Bias term
        self.epoch = epoch # Number of epochs to train
        self.rate = rate  # Learning rate
        
    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # Training the perceptron with input x1, x2 and ground truth values
    def train(self, x1, x2, truth):
        for i in range(self.epoch):
            for j in range(len(x1)):
                # Compute the prediction using sigmoid activation
                pred = self.sigmoid(self.w1 * x1[j] + self.w2 * x2[j] + self.bias)
                # Calculate the error term
                error = self.rate * (truth[j] - pred)
                # Update weights and bias
                self.w1 += error * x1[j]
                self.w2 += error * x2[j]
                self.bias += error
    
    # Predicting the output for given inputs x1 and x2
    def predict(self, x1, x2):
        if self.sigmoid(self.w1 * x1 + self.w2 * x2 + self.bias) > 0.5:
            return 1
        else:
            return 0
