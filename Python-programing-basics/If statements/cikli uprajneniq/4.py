steps = 0

while steps < 10000:
    more_steps = input('more steps:')
    if more_steps == ('Going home'):
        steps_to_home = input('steps_to_home:')
        steps += int(steps_to_home)
        break

    steps += int(more_steps)

if steps >= 10000:
    print('Goal reached! Good job!')
else: print(f"{abs(steps - 10000)} more steps to reach the goal.")