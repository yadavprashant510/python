import numpy as np
from sklearn import linear_model, datasets
import matplotlib.pyplot as plt
Digit = datasets.load_digits()
Digit_X = Digit.data[:, np.newaxis, 2]
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
print("Digit data x: ", Digit_X)
print("Data: ",Digit.data)
print("target: ",Digit.target)
print("target_names: ",Digit.target_names)
print("DESCR: ",Digit.DESCR)

