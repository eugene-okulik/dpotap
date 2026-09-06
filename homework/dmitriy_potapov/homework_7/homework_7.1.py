number = 10
while True:
    user_input = int(input("Угадай цифру. Введи число: "))
    if user_input == number:
        print("Поздравляю! Вы угадали")
        break
    elif user_input != number:
        print("Попробуйте снова")
        continue


