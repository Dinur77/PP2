import os
path = 'C:\\Users\\gainu\\OneDrive\\Рабочий стол\\PP'
#EX1
os.chdir(path)
print(os.listdir())

#EX2
print(os.access(path, os.F_OK))
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))

#EX3
if os.path.exists(path):
    print("exist")
    print(os.path.basename)
    print(os.path.dirname)
else:
    print("not exists")
#Ex4
with open(path, 'r', encoding='utf-8') as file:
    str = sum(1 for x in file)
print(str)

#EX5
name = ['dinur', 'gainullin', 'atyrau', 'almaty']
with open(path, 'w', encoding='utf-8') as file:
    for i in name:
        file.write(i + '\n')
print(path)

#EX6
for i in range(26):
    filename = chr(ord('A') + i) + ".txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")
    print(f"File {filename} created.")

#Ex7
from shutil import copyfile
copyfile('1.txt', '2.txt')

#Ex8
if os.path.exists("1.txt"):
    print(os.access("1.txt", os.F_OK))
    os.remove("1.txt")
else:
    print("not exists")
        


