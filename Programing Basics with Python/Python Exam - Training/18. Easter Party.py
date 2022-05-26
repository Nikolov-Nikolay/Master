number_of_guests = int(input())
price_for_envelope_fot_one_guest = float(input())
budget = float(input())

if 10 <= number_of_guests <= 15:
    price_for_envelope_fot_one_guest = price_for_envelope_fot_one_guest - (price_for_envelope_fot_one_guest * 15 / 100)
elif 15 < number_of_guests <= 20:
    price_for_envelope_fot_one_guest = price_for_envelope_fot_one_guest - (price_for_envelope_fot_one_guest * 20 / 100)
elif number_of_guests > 20:
    price_for_envelope_fot_one_guest = price_for_envelope_fot_one_guest - (price_for_envelope_fot_one_guest * 25 / 100)
price_for_cake = (budget * 10 / 100)
needed_money = price_for_cake + (price_for_envelope_fot_one_guest * number_of_guests)
diff = budget - needed_money
if budget >= needed_money:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {abs(diff):.2f} leva needed.")
