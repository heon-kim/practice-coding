N, R = map(int, input().split())
choose = []
check=[False]*(N+1)

def perm(level):
  if(level==R):
    print(" ".join(map(str, choose)))
    return
    
  for i in range(1, N+1):
    if check[i]==True:
      continue
      
    choose.append(i)
    check[i]=True
    
    perm(level+1)
    
    choose.pop()
    check[i]=False


perm(0)


# 오답노트
## 처음 접근 방식은?
### 순열을 이용해서 접근
## 사용한 알고리즘/아이디어는?
### 순열 알고리즘
## 어디서 막혔는가 or 왜 틀렸는가?
### range(1, N+1) 부분에서 range 값을 설정 못함.
### NPR을 구할 때 1~N까지 수 중 이전에 사용하지 않은 값을 choose 배열에 넣어주고 사용한 값을 check에 체크해준다.