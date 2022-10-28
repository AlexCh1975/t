# 3. * Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# поле 3х3


board = list(map(str, range(1, 10)))

def draw_board():
    print('-' * 20)
    for i in range(3):
        for j in range(3):
            print(f'{board[j + i * 3]:^5}', end=' ')
        print(f"\n{'-' * 20}")
    print()

def place_sing(token):
    global board
    while True:
        answer = input(f"Введите число от 1 до 9.\nВыбранная позиция {token}? ")
        if answer.isdigit() and int(answer) in range(1, 10):
            answer = int(answer)
            pos = board[answer - 1]
            if pos not in (chr(10060), chr(11093)):
                board[answer - 1] = chr(10060) if token == 'X' else chr(11093)
                break
            else:
                print(f"Эта ячейка уже занята{chr(9995)}{chr(1292292)}")
        else:
            print(f"Некорректный ввод{chr(9940)}. Вы уверены, что вы вводите правильный номер?")

def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n

def main():
    counter = 0
    draw_board()
    while True:
        place_sing('0') if counter % 2 else place_sing('X')
        draw_board()

        if counter > 3:
            if check_win():
                print(f"{check_win()} - WIN {chr(127942)}{chr(127881)}!")
                break
        if counter == 8:
            print(f"Ничья {chr(129318)}{chr(129309)}!")
            break
        counter += 1


main()