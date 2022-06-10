def validate(word):
    if len(word) < 6:
        print("Password must be between 6 and 10 characters")

    if not word.isalnum():
        print("Password must consist only of letters and digits")

    if word.isalnum() and sum(map(lambda x: x.isdigit(), word)) < 2:
        print("Password must have at least 2 digits")

    if word.isalnum() and sum(map(lambda x: x.isdigit(), word)) >= 2 and sum(map(lambda x: x.isalpha(), word)) != 0:
        print("Password is valid")


entry = input()
validate(entry)