for value in list(range(1, 101)):
    if value % 3 and value % 5:
        print('FuzzBuzz')
    elif value % 3:
        print('Fuzz')
    elif value % 5:
        print('Buzz')
    else:
        print(value)
