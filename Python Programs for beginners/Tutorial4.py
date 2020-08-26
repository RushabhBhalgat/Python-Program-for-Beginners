'''
Python Program to Display the multiplication Table
'''

#Taking Input From User
num = int(input("Enter The number to display the multiplication table "))

for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

