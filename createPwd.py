#checks if the entered password matches a predefined password.
#gives the user 3 attempts before it breaks out of the loop.

pd_pwd = "Python123"
attempts = 1

while attempts <= 3:
    pwd = input("Please enter the password: ")
    attempts += 1
    print(pwd)
    if pwd != pd_pwd:
        print(f"Access denied {88:c}")
    else:
        print(f"Access granted {10003:c}")
        break
