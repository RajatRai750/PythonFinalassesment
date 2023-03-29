# I tried using the loop method to get the factorial based on my memorization but still unable to get the result with this code.

"""
as per my program it prompts the user to input function and converts it to an integer using the int() function. if the input is neg
the error message will be printed other wise the factorial should have been calculated by the for loop that multiplies each number from 1 to num
"""
while True:
    try:
        num= int(input("Enter a non-neg int: "))
        if num < 0:
            raise ValueError("Input must be non-int")
        break
    except ValueError:
        print("Invalid input please write again.")


fact = 1
for i in range(1, num + 1):
    fact *= i
    print(f"The factorial: {num} is {fact}")