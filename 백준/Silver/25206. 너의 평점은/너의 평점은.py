import sys

total=0
scoreTotal=0

scoreMap = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

for _ in range(20):
  subject, score, grade = map(str, input().split())
  if not grade == 'P':
    total += float(score) * scoreMap[grade]
    scoreTotal += float(score)

    
print(round(total/scoreTotal, 6))