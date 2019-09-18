"""
This script writes one array into a CSV file.
"""
import numpy as np

x = np.array([1, 3, 5])

x.tofile(
    'data/x.csv',
    sep=','
)