   counting a digit


LOGIC 1

n=int(input())
count=0
while(n>0):
    n//=10
    count=count+1
    
print(count)

LOGIC 2

n=int(input())
print(len(str(n)))
