"""
This script replaces txt with jpg.
"""
filename = "inflammation.txt"
filename_len = len(filename)
filename[filename_len - 3] = "j"
filename[filename_len - 3] = "p"
filename[filename_len - 3] = "g"
print(filename)