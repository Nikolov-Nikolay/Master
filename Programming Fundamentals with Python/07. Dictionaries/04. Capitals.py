def capitals():
    countries_data = input().split(', ')
    capitals_data = input().split(', ')
    result = dict(zip(countries_data, capitals_data))

    for keys, value in result.items():
        print(f'{keys} -> {value}')


capitals()
