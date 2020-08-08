#Taking Input From The User
Principle = float(input('Enter THe Principle'))
Time_Period = float(input('Enter The Time Period'))
Rate_Of_Interest = float(input('Enter The Rate Of Intrest'))


#creating The Function
def Simple_Interest_Cal(P, T, R):
    print('The principle Is ', P)
    print('The Time Period Is ', T)
    print('The Rate Of Intrest Is ', R)
    S_I = (P * T * R) / 100
    amount = S_I + P
    print('The Simple Intrest Is ', S_I)
    print('The FInal Amount Is ', amount)
    


#CAll the Function
Simple_Interest_Cal(Principle, Time_Period, Rate_Of_Interest)
