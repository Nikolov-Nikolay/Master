budget = float(input())
price_for_kg_flour = float(input())

price_for_one_pack_of_eggs = price_for_kg_flour - (price_for_kg_flour * 25) / 100
price_for_l_milk = price_for_kg_flour + (price_for_kg_flour * 25) / 100
price_for_one_loaves = price_for_kg_flour + price_for_one_pack_of_eggs + (price_for_l_milk / 4)
price_for_all_loaves = 0
colored_egg_counter = 0
loaves = 0
price_for_all_loaves += price_for_one_loaves
while budget > price_for_all_loaves:
    price_for_all_loaves += price_for_one_loaves
    colored_egg_counter += 3
    loaves += 1
    if loaves % 3 == 0:
       colored_egg_counter = (colored_egg_counter - (loaves - 2))

prince_for_loaves = loaves * price_for_one_loaves
money_left = budget - prince_for_loaves
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_egg_counter} eggs and {money_left:.2f}BGN left.")
