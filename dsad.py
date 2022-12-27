def show_board(f):
    num = '  0 1 2'
    print(num)
    for row, i in zip(f, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")


def user_input(f, user):
    while True:
        position = input('Введите позицию: ').split()
        if len(position) != 2:
            print('Введите корректную позицию')
            continue
        if not (position[0].isdigit() and position[1].isdigit()):
            print('Введите числа.')
            continue
        x, y = map(int, position)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Введите правильный диапазон')
            continue
        if f[x][y] != '-':
            print('Клетка занята.')
            continue
        break
    return x, y

def win_position(f,user):
    f_list=[]
    print(f)
    for l in f:
        f_list+=l
    print(f_list)
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p)))==3:
            return True
    return False

def start(board):

    count = 0
    while True:
        show_board(board)
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        if count < 9:
            x, y = user_input(board, user)
            board[x][y] = user

        elif count == 9:
            print('Ничья')
            break
        if win_position(board, user):
            print(f"Выйграл {user}")
            break
        count+=1
board = [['-'] * 3 for _ in range(3)]

start(board)
