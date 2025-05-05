#asks the user for 5 numbers and tells them whether each one is even or odd.

number = int(input("Enter number: "))

while number != 0:
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
    number = int(input("Enter number: "))
    
