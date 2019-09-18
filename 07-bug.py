"""
This script removes 0 from the list.
"""
old_list = [
    0,
    2,
    4,
    6,
    8,
]
for i in range(len(old_list)):
    if old_list[i] == 0:
        old_list.pop(i)