def main():
    turn = 0
    board = {'A': 3, 'B': 4, 'C': 5}
    while board != [0, 0, 0]:
        if turn % 2 == 0:
            print('Board:', board)
            move = input('Alice > ')
        else:
            print('Board:', board)
            move = input('Bob > ')
        try:
            board[move[0]] -= int(move[1])
            if board[move[0]] < 0:
                raise
        except ValueError:
            board[move[0]] = 0
    if turn % 2 == 0:
        print('Bob wins!')
    else:
        print('Alice wins!')


if __name__ == '__main__':
    main()
