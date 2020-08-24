'''
Python Program to find average of n numbers
'''
numbers = input("Enter Numbers Seperated By Space ")
numberList = numbers.split()

print('\n')
print("The Numbers That You Entered ", numberList)

# Calculate The Sum Of All The Numbers
sum1 = 0
for num in numberList:
    sum1 += int(num)

print("Sum of all entered numbers = ", sum1)

#calculating the average of all user entered values
average = sum1 / len(numberList)
print("average of al entered values is ", average)
