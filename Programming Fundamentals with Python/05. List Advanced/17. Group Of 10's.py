def groups(numbers):
    border = 10
    lst = []

    while len(numbers) > 0:
        lst = ([num for num in numbers if (border - 10) < num <= border])
        print(f"Group of {border}'s: {lst}")
        numbers = [num for num in numbers if (border - 10) < num > border]
        border += 10


data = list(map(int, input().split(", ")))
groups(data)
