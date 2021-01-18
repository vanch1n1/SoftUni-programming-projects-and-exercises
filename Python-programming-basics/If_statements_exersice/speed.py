<<<<<<< HEAD
speed = float(input())
if speed <= 10:
    outcome = ('slow')
elif 10 < speed <= 50:
    outcome = ('average')
elif 50 < speed <= 150:
    outcome = ('fast')
elif 150 < speed <= 1000:
    outcome = ('ultra fast')
else: outcome = ('extremely fast')
=======
speed = float(input())
if speed <= 10:
    outcome = ('slow')
elif 10 < speed <= 50:
    outcome = ('average')
elif 50 < speed <= 150:
    outcome = ('fast')
elif 150 < speed <= 1000:
    outcome = ('ultra fast')
else: outcome = ('extremely fast')
>>>>>>> f5e08af265b4e5302a530dba1d0ac93840d06fcc
print(outcome)