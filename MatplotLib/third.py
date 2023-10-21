import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.arange(0, math.pi * 5, 0.05)
x2 = range(1, 50)

y1 = np.sin(x1)
y2 = np.cos(x1)
y3 = [i ** 2 for i in x2]
y4 = [2 / i for i in x2]

figure, axis = plt.subplots(2, 2)
figure.tight_layout(h_pad=2)


axis[0, 0].plot(x1, y1)
axis[0, 0].set_title("Y(x) = SIN(x)")
axis[0, 0].grid()

axis[0, 1].plot(x1, y2)
axis[0, 1].set_title("Y(x) = COS(x)")
axis[0, 1].grid()

axis[1, 0].plot(x2, y3)
axis[1, 0].set_title("Y(x) = X^2")
axis[1, 0].grid()

axis[1, 1].plot(x2, y4)
axis[1, 1].set_title("Y(x) = 2 / x")
axis[1, 1].grid()
plt.subplots_adjust(top=0.87)
plt.show()
