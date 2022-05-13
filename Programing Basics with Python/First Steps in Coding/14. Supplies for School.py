count_pens = int(input())
count_markers = int(input())
liters_cleaner = int(input())
percent = int(input())
sum_pens = count_pens * 5.80
sum_markers = count_markers * 7.20
sum_liters = liters_cleaner * 1.20
total_sum = sum_pens + sum_markers + sum_liters
total_sum = total_sum - (total_sum * (percent / 100))
print(total_sum)
