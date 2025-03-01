d = int(input())

g = 1000-d

ob = g // 500 # 500엔 개수
g = g % 500

b = g // 100 # 100엔 개수
g = g % 100

os = g // 50 # 50엔 개수
g = g % 50

s = g // 10 # 10엔 개수
g = g % 10

o = g // 5 # 5엔 개수
g = g % 5 # 1엔 개수

print(ob+b+os+s+o+g)