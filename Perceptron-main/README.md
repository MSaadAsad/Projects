## Perceptron
A simple perceptron implementation for binary classification tasks. The perceptron can be trained to mimic and basic logic gate.

## Description
This implementation utilizes the sigmoid activation function and is designed to handle binary classification. It can be trained with two input features.

## Usage
### Initialization
Create a Perceptron object by specifying the initial weights, bias, the number of training epochs, and the learning rate:

p = Perceptron(w1=0.5, w2=-0.5, bias=0, epoch=100, rate=0.1)

### Training
Train the perceptron using the train method. Pass the training data for both features along with the corresponding truth values:

x1 = [0, 1, 1]
x2 = [0, 0, 1]
truth = [0, 0, 1]
p.train(x1, x2, truth)

### Prediction
Predict the output for given input values using the predict method:

result = p.predict(1, 1)
print(result)  # Output: 1
