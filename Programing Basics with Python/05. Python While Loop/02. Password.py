username = input()
password = input()

entered_password = input()

while entered_password != password:
    entered_password = input()
else:
    print(f"Welcome {username}! ")

    