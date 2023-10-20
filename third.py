import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.arange(0, math.pi * 2, 0.05)
x2 = range(1, 50)

Y1 = np.sin(x1)
Y2 = np.cos(x1)
Y3 = [i ** 2 for i in x2]
Y4 = [2 / i for i in x2]

figure, axis = plt.subplots(2, 2)

axis[0, 0].plot(x1, Y1)
axis[0, 0].set_title("Y(x) = SIN(x)")

axis[0, 1].plot(x1, Y2)
axis[0, 1].set_title("Y(x) = COS(x)")

axis[1, 0].plot(x2, Y3)
axis[1, 0].set_title("Y(x) = X^2")

axis[1, 1].plot(x2, Y4)
axis[1, 1].set_title("Y(x) = 2 / x")
plt.grid()

plt.show() 