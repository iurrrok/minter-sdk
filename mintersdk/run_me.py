import os

f = open("requirements.txt")

for row in f:
    os.system(f'pip install {row}')

print('done')
