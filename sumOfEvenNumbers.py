#asks the user for 5 numbers and adds all the even numbers.

sum = 0
count = 1

while count <= 5:
    number = int(input(f"Enter a number {count}: "))
    count += 1
    if number % 2 == 0:
        sum += number

print(f"The sum of all the even numbers is {sum}")
    