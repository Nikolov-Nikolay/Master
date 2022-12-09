number_of_commands = int(input())

registered_dict = {}

for command in range(number_of_commands):
    info = input().split(" ")

    if info[0] == "register":
        name = info[1]
        plate = info[2]

        if name not in registered_dict.keys():
            registered_dict[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")

    elif info[0] == "unregister":
        name = info[1]
        if name not in registered_dict.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            registered_dict.pop(name)

[print(f"{name} => {plate}") for name, plate in registered_dict.items()]