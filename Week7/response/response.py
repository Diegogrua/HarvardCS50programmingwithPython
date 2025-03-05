import validators

email = input("what's is your email?: ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
