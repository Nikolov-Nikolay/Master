deposit = float(input())
months = int(input())
percent = float(input())
final_sum = deposit + months * ((deposit * (percent / 100)) / 12)
print(final_sum)
