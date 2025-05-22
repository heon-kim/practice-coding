N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

count = {}
kind = 0
answer = 0

# k까지 초밥 종류 세기
for i in range(k):
    sushi = belt[i]
    if sushi not in count:
        count[sushi] = 0
        kind += 1
    count[sushi] += 1

answer = kind + (0 if c in count else 1)

# 슬라이딩 윈도우
for i in range(1, N):
  # 왼쪽 초밥 제거
  out_sushi = belt[i - 1]
  count[out_sushi] -= 1
  if count[out_sushi] == 0:
    del count[out_sushi]
    kind -= 1

  # 오른쪽 초밥 추가
  in_sushi = belt[(i - 1 + k) % N]
  if in_sushi not in count:
      count[in_sushi] = 0
      kind += 1
  count[in_sushi] += 1

  # 최대 개수 업데이트
  answer = max(answer, kind + (0 if c in count else 1))

print(answer)
  
      