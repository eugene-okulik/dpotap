result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'


def program(result):
    num = int(result[result.index(':') + 2:])
    print(num + 10)


def program2(result):
    a = result.split(':', 1)
    num = int(a[1].strip())
    print(num + 10)


program2(result_4)
