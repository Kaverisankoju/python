#Fibonacci
n1,n2=0,1
n=int(input("enter a number:"))
for i in range(n):
    print(n1)
    third_num=n1+n2
    n1=n2
    n2=third_num
    
n1,n2=0,1
n=int(input("enter a number:"))
for i in range(n):
    print(n1)
    n1,n2=n2,n1+n2

#Armstrong 
n=153
temp=n
sum=0
k=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**k
    n//=10
if temp==sum:
    print(sum,"it is amstrong number")
else:
    print(sum,"not a amstrong")
    

#Fibonacci
#method-1
n1,n2=0,1
n=int(input("enter a number:"))
for i in range(n):
    print(n1)
    third_num=n1+n2
    n1=n2
    n2=third_num
#method-2    
n1,n2=0,1
n=int(input("enter a number:"))
for i in range(n):
    print(n1)
    n1,n2=n2,n1+n2

#Armstrong 
n=153
temp=n
sum=0
k=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**k
    n//=10
if temp==sum:
    print(sum,"it is amstrong number")
else:
    print(sum,"not a amstrong")
    
