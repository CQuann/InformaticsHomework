import matplotlib.pyplot as plt

k1, b1 = int(input()), int(input())
k2, b2 = int(input()), int(input())

x = [i for i in range(50)]
y1 = [k1 * i + b1 for i in x]
y2 = [k2 * j + b2 for j in x]

plt.xlabel("x")
plt.ylabel("y1, y2")
plt.grid()
plt.plot(x, y1, x, y2)
plt.show()
