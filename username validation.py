username=input("enter your username: ")

if len(username) > 12:
    print("your username cannot be 12 characters long")
elif not username.find(" ")== -1:
    print("your username canno have space")
elif not username.isalpha():
    print("your username cannot have numbers")
else:
    print(f"welcome {username}")



