foul = list(input().split())
dict = {}

for name in foul:
    dict[name] = foul.count(name)
    foul_min = min(dict.values())

for name in dict:
    if dict[name] == foul_min:
        print(name)
print(foul_min)
