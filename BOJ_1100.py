board = [list(input()) for _ in range(8)]
horse = 0

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if board[i][j] == 'F':
                horse += 1
            else:
                horse += 0

print(horse)
