operator = input()
first_number = int(input())
second_number = int(input())


def calculations(operator, first_number, second_number):
    if operator == 'multiply':
        result = first_number * second_number
        return result
    elif operator == "divide":
        result = first_number // second_number
        return result
    elif operator == 'add':
        result = first_number + second_number
        return result
    elif operator == 'substract':
        result = first_number - second_number
        return result
print(calculations(operator, first_number, second_number))