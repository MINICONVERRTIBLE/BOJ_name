''''
array=list[map(int,input())]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

total = 0
for i in range(n):
    for j in range(m):
        total += a[i][j]

'''
# 강사님 array 예시 
array = list[map(int,input())]
n, m= map(int, input().split())
array_1 = [[int(x) for x in input().split()]for y in range(2)]
array_2 = [[int(x) for x in input().split()]for y in range(2)]
for i in range(n):
    for j in range(m):
        total *=a[i][j]
print()

#강사님 예시 (리스트 comprehension 없이)
list_a = []
for i in range(2):
    line = list(map(int, input().split()))
    list_a.append

'''
list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(list_a[i][j] * list_b[i][j], end=" ")
    print()
'''