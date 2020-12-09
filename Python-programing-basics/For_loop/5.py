n = int(input())
p1 = 0
p2 = 0
p3 = 0
for action in range(n):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1

procent2 = p1/(p1+p2+p3) * 100
procent3 = p2/(p1+p2+p3) * 100
print(f'{procent2}\n {procent3}')