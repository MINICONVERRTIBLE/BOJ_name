num = int(input())
nat_cap = {}

for i in range(num):
    word = input().split()
    nat_cap[word[0]]= word[1]

word = input()
print(nat_cap.get(word,'Unknown Country'))