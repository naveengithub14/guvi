# your code goes here
n=input()
a=input()
d=input()
def ap(n,a,d):
  b=0
  i=0
  while(i<n):
    b=b+a
    a=a+d
    i=i+1
  return b
print(ap(n,a,d))
