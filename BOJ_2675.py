#테스트 케이스의 개수 조건
T = int(input())
1<= T <= 1000

#반복횟수의 조건 

R = int(input())
1<= R<=8


word = str(input().split())


#코드
for n in range(len(word)):
    for x in word:
        print(x*R,end="")
print()

``