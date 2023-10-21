import matplotlib.pyplot as plt
from random import choices


def random_pie(pieces):
    labels = range(1, pieces + 1)
    values = choices(range(1, 100), k=pieces)
    plt.pie(values, labels=labels)
    plt.title("Random Pie")
    plt.show()


random_pie(10)
