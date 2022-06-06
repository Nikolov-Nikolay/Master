n = [int(x) for x in input().split(', ')]
beggars = int(input())

beggars_list = [0] * beggars

for num in range(len(beggars_list)):
    current_beggar = num
    for i in range(len(n)):
        current_num = i % beggars
        if current_num == current_beggar:
            if beggars_list[num] == 0:
                if n[i] == 0:
                    beggars_list[current_num] = n[i]
                    break
                beggars_list[current_num] = n[i]
            else:
                beggars_list[current_num] += n[i]

print(beggars_list)