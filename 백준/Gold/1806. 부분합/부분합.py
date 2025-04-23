N, S = map(int, input().split())
arr=list(map(int, input().split()))
    

# 오답노트
## 처음 접근 방식은?
### 조합을 이용하여 가능한 합을 모두 확인하고 답을 출력
## 사용한 알고리즘/아이디어는?
### 조합 알고리즘
## 어디서 막혔는가 or 왜 틀렸는가?
### 수열은 연속된 수들의 조합을 찾는 것. 이전에도 수열과 조합을 착각한 경우 있었다. 주의할 것.

# 오답 풀이 (시간 복잡도 O(N**2))
# answers = []

# for j in range(1, N+1):
#   for k in range(N-j+1):
#     sum_S = sum(arr[k:k+j])
#     if(sum_S>=S):
#       answers.append(j)
#       break

# print(min(answers))

# 정답 풀이 (시간복잡도 O(N))
total = 0
start = 0
end = 0
min_len = N+1

while True:
  if(total>=S):
    min_len = min(min_len, end - start)
    total -= arr[start]
    start += 1
  elif(N==end):
    break
  else:
    total += arr[end]
    end += 1

print(min_len if min_len != N + 1 else 0)

# 정답 풀이 (시간복잡도 O(1))
# # 누적합
# nu = [0]*(N+1)
# for i in range(N):
#   nu[i]=nu[i-1]+arr[i-1]

# min_len = N+1

# for i in range(N):
#   for j in range(i+1, N+1):
#     if (nu[j] - nu[i]) >= S:
#       min_len = min(j-i, min_len)
#       break

# print(min_len if min_len != N + 1 else 0)