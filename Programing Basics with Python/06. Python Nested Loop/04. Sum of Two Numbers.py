start = int(input())
finish = int(input())
magic_number = int(input())
combination = 0
is_found = False
for i in range(start, finish + 1):
    for j in range(start, finish + 1):
            combination += 1
            if i + j == magic_number:
                print(f"Combination N:{combination} ({i} + {j} = {magic_number})")
                is_found = True
                break
    if is_found:
        break
else:
    print(f"{combination} combinations - neither equals {magic_number}")