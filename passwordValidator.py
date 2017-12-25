import re


#Taking input of password
x = str(input('Enter a password: '))


#Checking whether the password has atleast 8 digit using REGULAR EXPRESSION

'''USE LOOK-AHEAD'''
# y = re.findall(('\w'),x)
valid = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}')

if re.search(valid,x):
    print('Valid')
else:
    print('Invalid')
