a, b = map(int, input().strip().split(' '))

for j in range(b):
    str=""
    for i in range(a):
        str += "*"
    print(str)
