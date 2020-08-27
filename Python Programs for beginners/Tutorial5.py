import calendar

# Taking input from user

year = int(input("Enter the year"))
month = int(input("Enter the month"))


# Display the output

result = calendar.month(year, month)
print(result)