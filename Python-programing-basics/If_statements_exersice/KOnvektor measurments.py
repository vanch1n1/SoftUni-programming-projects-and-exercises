number = float(input())
input_measurement = input()
outcome_measurement = input()
if input_measurement == ('mm') and outcome_measurement == ('m'):
    outcome = (number / 1000)
    print(f'{outcome:.3f}')
if input_measurement == ('m') and outcome_measurement == ('cm'):
    outcome = number * 100
    print(f'{outcome:.3f}')
if input_measurement == ('cm') and outcome_measurement == ('mm'):
    outcome = number * 10
    print(f'{outcome:.3f}')
if input_measurement == ('mm') and outcome_measurement ==('cm'):
    outcome = number / 10
    print(f'{outcome:.3f}')
if input_measurement == ('cm') and outcome_measurement == ('m'):
    outcome = number / 100
    print(f'{outcome:.3f}')
if input_measurement == ('m') and outcome_measurement == ('mm'):
    outcome = number * 1000
    print(f'{outcome:.3f}')
