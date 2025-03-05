N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B 큰 것부터
SB = sorted(B, reverse=True)
# A 작은 것부터
SA = sorted(A)



print(sum([SB[i]*SA[i] for i in range(N)]))