rent_for_the_hall = int(input())

statuette = rent_for_the_hall - (rent_for_the_hall * 30) / 100
catering = statuette - (statuette * 15) / 100
sound_system = catering / 2

final_prize = rent_for_the_hall + statuette + catering + sound_system
print(f'{final_prize:.2f}')
