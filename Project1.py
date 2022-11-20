"""
Mean-Variance-Standard Deviation Calculator.
Creating a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, 
and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function then converts the list into a 3 x 3 Numpy array, 
and then returns a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
"""
import numpy as np
def calculate(lst):
 

  if len(lst) != 9:
    return "List must contain nine numbers."
  x = np.array(lst).reshape(3, 3)
  result = {
    k: [func(x, axis=ax).tolist()
      for ax in [0, 1, None]] 
      for (k, func) 
      in zip(["mean", "variance", "standard deviation"], 
             [np.mean, np.var, np.std])
  } 


  return result
