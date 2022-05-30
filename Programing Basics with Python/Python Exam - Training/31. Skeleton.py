minutes_for_controls = int(input())
seconds_for_controls = int(input())
distance_in_meters = float(input())
seconds_for_100_meters = int(input())

full_time_in_seconds = (minutes_for_controls * 60) + seconds_for_controls
losing_time = distance_in_meters / 120
full_losing_time = losing_time * 2.5
marin_time = (distance_in_meters / 100) * seconds_for_100_meters - full_losing_time
diff = full_time_in_seconds - marin_time
if marin_time <= full_time_in_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f"His time is {marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(diff):.3f} second slower.")
