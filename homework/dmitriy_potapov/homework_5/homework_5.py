person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

num_1 = int(result_1[result_1.index(':')+2:])
print(num_1 + 10)

num_2 = int(result_2[result_2.index(':')+2:])
print(num_2 + 10)

num_3 = int(result_3[result_3.index(':')+2:])
print(num_3 + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
students = ', '.join(students)
subjects = ['math', 'biology', 'geography']
subjects = ', '.join(subjects)

print(f'Student {students} study these subjects: {subjects}')
