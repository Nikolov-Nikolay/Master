my_dict = {}
word = input()

for ch in word:
    if ch not in my_dict and ch != ' ':
        my_dict[ch] = 1
    else:
        my_dict[ch] += 1

print(my_dict)