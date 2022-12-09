command = input()
programs = {}
registered_students = 0

while command != 'end':
    program, student = command.split(' : ')
    if program not in programs:
        programs[program] = [student]
    else:
        programs[program].append(student)

    command = input()

#sorted_courses = dict(programs.items(), key=lambda x: len(x[0]))

for program, student in programs.items():
    print(f'{program}: {len(student)}')
    for name in student:
        print(f'-- {name}')

