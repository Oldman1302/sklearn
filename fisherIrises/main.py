import numpy as np

INPUT_DIM = 4  # number of input neurons
OUT_DIM = 3    # number of output neurons
H_DIM = 10     # number of neurons in the hidden layer

'''
if we want to check something special
x = []
for i in range(4):
    x.append(float(input()))
'''

x = np.array([7.9, 3.1, 7.5, 1.8])
# np.random.randn - generation of random numbers from a
# standard normal distribution (Gaussian distribution) with mean 0 and standard deviation 1
w1 = np.random.randn(INPUT_DIM, H_DIM)  # weights on 1st layer
b1 = np.random.randn(H_DIM)
w2 = np.random.randn(H_DIM, OUT_DIM)  # weights on 2nd layer
b2 = np.random.randn(OUT_DIM)

print('iris characteristics\n', x)
print('\nweights on 1st layer\n', w1)


# return t if t > 0, otherwise it returns 0
def relu(t):
    print('\nrelu\n', np.maximum(t, 0))
    return np.maximum(t, 0)


# this function redefine matrix to set of probabilities
def softmax(t):
    res = np.exp(t) / np.sum(np.exp(t))
    print('\nsoftmax\n:', res)
    return res


# h = f(x * w + b), so here we choose relu as f
def predict(x1):
    t1 = x1 @ w1 + b1  # @ - matrix multiplication (np.dot(x, w1))
    h1 = relu(t1)  # function of activation
    t2 = h1 @ w2 + b2
    z = softmax(t2)  # vector of probabilities
    print('\nz\n', z)
    return z


probs = predict(x)
pred_class = np.argmax(probs)
class_names = ['Setosa', 'Versicolor', 'Virginica']
print('\nPredicted:', class_names[pred_class])
