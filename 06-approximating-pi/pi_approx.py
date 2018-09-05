import numpy as np 
import matplotlib.pyplot as plt

k = 0
n = 10000
for i in range(n):
    x = np.random.rand(1)
    y = np.random.rand(1)
    hyp = x**2 + y**2
    if hyp < 1:
        k+=1   
        plt.figure(1)
        plt.scatter(x,y,color='r')
    else:
        plt.figure(1)
        plt.scatter(x,y,color='b')
plt.show()
pi_4 = k/n
print("Pi/4 is ", pi_4)




