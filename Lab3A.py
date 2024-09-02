# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

Amount= input("Amount owed: $")
APR= float(input("APR:" ))
Mpr=(APR/12)
percentageAmount=round(Mpr, 3)
print("Monthly percentage rate:" + str(percentageAmount))
Mp=(Amount * int(APR/100/12))
paymentAmount=(round(Mp,2))
print("Minimum payment:" + str(paymentAmount))



