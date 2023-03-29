
while True:
    try:
        size = int(input("Enter size: "))
        if size <= 1:
            raise ValueError("Size must be positive ")
        break
    except ValueError as e:
        print("Invalid input: {e}")

for i in range(0,size):
    for j in range(0,i+1):
        print("*", end=' ')
    print('\r')

for i in range(size,0,-1):
    for j in range(0,i-1):
        print("*",end=' ')
    print("\r")



