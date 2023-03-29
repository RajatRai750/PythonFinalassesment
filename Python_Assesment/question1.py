# used to input statment so that the person can write the temp they want to convert
t = float(input("Enter The Temperature: "))
conver = (input("convert to Celsius: "))

# the most suitable condition i thought for this kind of problem was the usage of if-elif-else statements in order to check the  conver. 


if conver == "C":
    celcs = (t - 32)*5/9
    print(f"{t} degree Fahrenheit is {celcs:.2f} degrees Celsius")

elif conver == "F":
    fhr = (t * 9/5) + 32
    print(f"{t} degree celsius is {fhr:.2f} degrees Fahrenheit")
else:
    print("Result not found. Please enter the correct form")