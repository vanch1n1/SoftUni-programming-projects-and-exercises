<<<<<<< HEAD

record = float(input())
lenght = float(input())
time_for_1_meter = float(input())
targeted_time = lenght * time_for_1_meter
delay = lenght // 15 * 12.5
targeted_time += delay
if targeted_time < record:
    print(f'Yes, he succeeded! The new world record is {targeted_time:.2f} seconds. ')
else:
    difference = targeted_time - record
    print(f'No, he failed! He was {difference:.2f} seconds slower. ')
=======

record = float(input())
lenght = float(input())
time_for_1_meter = float(input())
targeted_time = lenght * time_for_1_meter
delay = lenght // 15 * 12.5
targeted_time += delay
if targeted_time < record:
    print(f'Yes, he succeeded! The new world record is {targeted_time:.2f} seconds. ')
else:
    difference = targeted_time - record
    print(f'No, he failed! He was {difference:.2f} seconds slower. ')
>>>>>>> f5e08af265b4e5302a530dba1d0ac93840d06fcc
