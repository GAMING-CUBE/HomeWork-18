import glob

a = ['1', '719.py']

for i in a:
    files = glob.glob(i)
    print(files)
