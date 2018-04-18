

import numpy as np
import matplotlib.pyplot as plt
import math

plt.figure()

x = np.linspace(0.0,1.0,100)
x[0] = x[1]
x[-1] = x[-2]

def f(m):
    return math.log(1/(1-m)) - m/(1-m)

y = np.linspace(0,1,100)

for i in np.arange(0,100):
    y[i] = f(x[i])

plt.plot(x,y)
plt.ylabel(u'$\ln\dfrac{1}{1-X_A}-\dfrac{X_A}{1-X_A} $')
plt.xlabel(u'$X_A$')

plt.savefig('hua.png')

plt.show()
