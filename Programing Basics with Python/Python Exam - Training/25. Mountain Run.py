import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

time_in_seconds_for_all_distance = distance_in_meters * time_in_seconds_for_one_meter
every_fifth_meters = distance_in_meters / 50
every_fifth_meters = math.floor(every_fifth_meters)
all_meters = every_fifth_meters * 30
all_needed_time = time_in_seconds_for_all_distance + all_meters
diff = all_needed_time - record_in_seconds

if all_needed_time >= record_in_seconds:
    print(f'No! He was {diff:.2f} seconds slower.')
else:
    print(f'Yes! The new record is {all_needed_time:.2f} seconds.')
