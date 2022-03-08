n  = int(input())

for _ in range (n) :
    r, word = input().split()
    for words in word:
        print(words*int(r),end='')
    print()