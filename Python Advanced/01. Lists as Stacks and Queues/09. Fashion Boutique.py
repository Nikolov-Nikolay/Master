clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
racks_counter = 1

while clothes:
    piece_ot_clothing = clothes[-1]
    if piece_ot_clothing > current_rack_capacity:
        racks_counter += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= piece_ot_clothing
        clothes.pop()

print(racks_counter)
