n = int(input())
dictionary = {}
for every_grade in range(n):
    name = input()
    grade = float(input())
    if not name in dictionary:
        dictionary[name] = []
    dictionary[name].append(grade)
filtered_dictionary = {}
for key, value in dictionary.items():
    average_grade = sum(value)/len(value)
    if average_grade >= 4.50:
        filtered_dictionary[key] = average_grade
for student, av_grade in sorted(filtered_dictionary.items(), key=lambda x: x[1], reverse=True):
    print(f"{student} -> {av_grade:.2f}")

