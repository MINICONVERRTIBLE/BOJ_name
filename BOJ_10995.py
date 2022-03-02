N = int(input())

if N == 1:
    print('*')
    
else:
    for n in range(N):
        if n % 2 == 0:
            a = print('* ' * N)
        else:
            b = print(' *' * N)


n = int(input())
line = "*" *n

for i in range(n):
    print(line)
    line = line[::-1]