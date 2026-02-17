password = input("Create a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "!@#$%^&*"

if len(password) < 8:
    print("Password must be at least 8 characters long")
else:
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Strong password created successfully!")
        login = input("Enter password to login: ")

        if login == password:
            print("Login successful")
        else:
            print("Incorrect password")
    else:
        print("Password must contain:")
        print("at least one uppercase letter")
        print("at least one lowercase letter")
        print("at least one number")
        print("at least one special character")
