"""
This script creates a plot for each file in the list.
"""
import matplotlib.pyplot as plt

filenames = [
    'inflammation-01.csv',
    'inflammation-02.csv',
    'inflammation-03.csv',
]

for filename in filenames:
    plt.plot([0, 1, 0])

plt.savefig(filename + '.jpg')