import os

i = 0
x = os.listdir(os.getcwd())
for file_name in x:
    print(file_name)
    i = i + 1
    os.rename(file_name, "program{}.py".format(i))