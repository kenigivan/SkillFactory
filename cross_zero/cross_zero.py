from random import randint


def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! (номер строки и номер столбца через пробел)")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Вводить можно только числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! Введите два числа от 0 до 2 через пробел!")
            continue

        if field[x][y] != " ":
            print(" Эта клетка уже занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print('\t Выиграл X (КРЕСТИК)')
            return True
        if symbols == ["0", "0", "0"]:
            show()
            print('\t Выиграл 0 (НОЛИК)')
            return True
    return False


choice = None
while choice != '0':
    count = 0
    print('''
    Игра "крестики-нолики" v1.0
   --------------------------------
    0 - Выйти
    1 - Играть с человеком
    2 - Игать с ПК
    3 - Описание и правила игры
   --------------------------------
   формат ввода в игре (x пробел y)
    ''')
    choice = input('Ваш выбор: ')

# выход
    if choice == '0':
        print('До свидания!')

# Игра с человеком
    elif choice == '1':
        field = [[" "] * 3 for i in range(3)]
        count = 0
        while True:
            count += 1
            show()
            if count % 2 == 1:
                print(' Ходит 1 игрок (КРЕСТИК)')
            else:
                print(' Ходит 2 игрок (НОЛИК)')

            x, y = ask()

            if count % 2 == 1:
                field[x][y] = "X"
            else:
                field[x][y] = "0"

            if check_win():
                break

            if count == 9:
                print(' Ничья! Победила дружба! :)')
                break

# Игра с компьютером
    elif choice == '2':
        field = [[' '] * 3 for i in range(3)]
        count = 0
        all_steps = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]  # Все! возможные шаги
        while True:
            count += 1
            show()
            if count % 2 == 1:
                print(' Ходит 1 игрок (КРЕСТИК)')
                x, y = ask()
                all_steps.remove([x, y])
            else:
                move = all_steps[randint(0, len(all_steps) - 1)]
                x = move[0]
                y = move[1]
                all_steps.remove([x, y])
                print(f' Компьтер сходил по координатам {x, y} (НОЛИК)')

            if count % 2 == 1:
                field[x][y] = "X"
            else:
                field[x][y] = "0"




            if check_win():
                break

            if count == 9:
                print(" Ничья! Победила дружба! :)")
                break

# Описание игры
    elif choice == '3':
        print(
            '''
            Крестики-нолики — логическая игра между двумя противниками на квадратном поле 3 на 3 клетки.
        Игроки по очереди ставят на свободные клетки поля, знаки (один всегда крестики, другой всегда нолики).
           Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.
                                Первый ход делает игрок, ставящий крестики.
                            
             ----- Формат ввода координат в игре (x пробел y), например: 2 1 или 0 0 или 1 0 -----
                          ----- После ввода координат нажмите Enter (Энтер) -----     
                          
                                        ПРИЯТНОЙ ВАМ ИГРЫ!
            ''')
        input('\nНажмите Enter, чтобы вернуться в главное меню.')

    else:
        print(f'\n\t! Извените в меню нет пункта: {choice}')


input('\nНажмите Enter, чтобы выйти.')
