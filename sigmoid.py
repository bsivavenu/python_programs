import numpy as np
import matplotlib.pyplot as plt
# def sigmoid(x):
# 	func = 1/float(1 + np.exp(- x))
# 	return func
# values = []
# for i in range(100):
# 	values.append(sigmoid(i))
# print(values)
# plt.plot(values)
# plt.show()

# def sigmoid_fun(inputs):
# 	sigmoid =  [ (1/float(1+np.exp(-x))) for x in inputs ]
# 	return sigmoid

# values = [i for i in range(20)]

# print(sigmoid_fun(values))
# plt.plot(sigmoid_fun(values))
# plt.show()

def softmax(x):
	func = np.exp(x) / float(sum(np.exp(x)))
	return func

values = [i for i in range(0,30)]

print(softmax(values))
plt.plot(softmax(values))
plt.show()

