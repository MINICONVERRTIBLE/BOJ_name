paper = [list(input()) for _ in range(0,100)]

for _ in range(int(input)):
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[i+a][j+b]
        r = 0
        for i in paper:
            r+= sum(i)
        print(r)
