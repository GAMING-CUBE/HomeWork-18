import os

filenames = ['my.py', 'input.txt']

for filename in filenames:
    print(os.path.exists(filename))
