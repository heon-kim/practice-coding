N=int(input())
number = 666
count = 0

while (N!=count):
  if('666' in str(number)):
    count += 1
  number += 1
  
print(number-1)


# 오답노트
## 처음 접근 방식은?
### 1. N번째로 작은 종말의 수를 잘못 이해.
### 2. count 조건과 number 조건 헷갈림

## 사용한 알고리즘/아이디어는?
### 브루트 포스

## 어디서 막혔는가 or 왜 틀렸는가?
### 정답 조건에 해당하면 count를 증가시키고, 반복 조건에 해당하면 number를 증가시켜야하는데, 둘 다 같이 증가시켜서 틀림.

# 정답 풀이
## 브루트포스
## "문자열 포함" 검사 → in 연산자