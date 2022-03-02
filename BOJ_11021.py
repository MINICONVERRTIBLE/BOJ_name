T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    C = A+B
    print("Case #%d:"%(i+1),C)

#강사님 설명
T =  int(input())
for i in range(T):
    a,b=map(int,input().split())
    print(f"Case #{i+1}: {a+b}")