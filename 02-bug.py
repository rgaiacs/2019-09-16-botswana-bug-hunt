"""
This script reverses a list.
"""

input_list = [
    1,
    3,
    5,
    7,
    9,
]

for i in input_list:
    output_list = [i] + output_list

print(output_list)