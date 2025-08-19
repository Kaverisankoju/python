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

#by using def function
def check_amstrong(n):
    temp=n
    total=0
    k=len(str(n))
    while n>0:
        digit=n%10
        total+=digit**k
        n//=10
    print(total)
    return "Amstrong" if temp==n else "Not a Amstrong"
n=int(input("enter a number:"))
print(check_amstrong(n))