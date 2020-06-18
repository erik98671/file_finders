import os

path = "C:/Users/braune/Desktop/temp"

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    print(f)
