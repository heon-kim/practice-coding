def solution(s):
    list = [int(i) for i in s.split(" ")]
    list.sort()
    return str(list[0]) + " " + str(list[-1])
