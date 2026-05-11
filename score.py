grade=input().split()
i=0
total=0
count=0
for a in grade:
  a=int(a)
  total+=int(a)
  count+=1
  if a<60:
    i=i+1
  else:
    continue
average=total/count
print(average)
print(i)



max_score=grade[0]
min_score=grade[0]
for a in grade:
  a=int(a)
  if a>int(max_score):
    max_score=a

  if a<int(min_score):
    min_score=a

print(max_score,min_score)
