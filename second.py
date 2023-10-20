import matplotlib.pyplot as plt
from random import choices

nums = choices(range(50), k=7)
plt.title("Random counts")
plt.bar(range(1, 8), nums)
plt.show()
