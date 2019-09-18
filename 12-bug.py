"""
This sript selects the function to use given the argument.
"""
import numpy as np

arg = '--max'

vector = np.array([1, 2, 3])

if arg == '--max':
    output = np.max(vector)
if arg == '--min':
    output = np.min(vector)
else:
    output = np.mean(vector)

print(output)