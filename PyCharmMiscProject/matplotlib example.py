import matplotlib.pyplot as plt
import numpy as np
import math
x_val = np.linspace(0,50,10)
def my_square(x):
    return x*x
y_val= [my_square(I)for I in x_val]
plt.plot(x_val,y_val)
plt.show()