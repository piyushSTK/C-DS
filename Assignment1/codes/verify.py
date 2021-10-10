import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from time import time

def recur(n, arr):
    if (n<=0):
        return
    else:
        recur(int(n/2), arr)
        arr.append(n%2)
    return
  
def objective( x, a, b):
    return a + b*np.log(x)

  
timeArr = []
for i in range(1,100000, 100):
    numba = 20*i
    arr = []
    t1 = time()
    recur(numba, arr)
    t2 = time()
    timeArr.append(t2-t1)
    
x = np.linspace(1,len(timeArr),len(timeArr))
popt, pcov = curve_fit(objective, x, timeArr)
                
plt.figure()
plt.plot(x, timeArr, label="Original Noised Data")
plt.plot(x, objective(x, *popt), 'r-', label="Fitted Curve")
plt.legend()
plt.show()
