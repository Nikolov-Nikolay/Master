n = int(input())
odd_sum = 0
even_sum = 0
value = -1
for step in range(1, n + 1):
    value = int(input())
    if step % 2 == 0:
        even_sum += value
    else:
        odd_sum += value
if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {abs(even_sum - odd_sum)}')


