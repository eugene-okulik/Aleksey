# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name = person[0]
last_name = person[1]
city = person[2]
phone = person[3]
country = person[4]

# Задание 2

a = 'результат операции: 42'

b = 'результат операции: 514'

c = 'результат работы программы: 9'

print(int(a[a.index(':') + 2:]) + 10)
print(int(b[b.index(':') + 2:]) + 10)
print(int(c[c.index(':') + 2:]) + 10)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

# students_1 = ' '.join(students)
subjects_2 = ' '.join(subjects)

print(f'Students {students[0]}, {students[1]}, {students[2]} study these subjects: {subjects_2}')
