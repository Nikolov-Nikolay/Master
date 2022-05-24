name_of_the_movie= input()
percent_busy = 0
total_tickets_for_all_movies = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while name_of_the_movie != 'Finish':
    free_seats = int(input())
    percent_busy = 0
    total_tickets= 0

    for i in range(0, free_seats):
        ticket_type = input()
        if ticket_type == 'End' or ticket_type == 'Finish':
            break
        if ticket_type == 'student':
            student_tickets += 1
            total_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
            total_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1
            total_tickets +=1

        total_tickets_for_all_movies +=1
        percentage_busy = (total_tickets / free_seats ) * 100
    print(f'{name_of_the_movie} - {percentage_busy:.2f}% full.')

    name_of_the_movie = input()

total_tickets = student_tickets + standard_tickets + kids_tickets
student_tickets = (student_tickets / total_tickets) * 100
standard_tickets = (standard_tickets / total_tickets) * 100
kids_tickets = (kids_tickets / total_tickets) * 100
print(f'Total tickets: {total_tickets}')
print(f'{student_tickets:.2f}% student tickets.')
print(f'{standard_tickets:.2f}% standard tickets.')
print(f'{kids_tickets:.2f}% kids tickets.')

