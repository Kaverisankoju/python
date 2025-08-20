#Amstrong numbers in the given range
num1=int(input("enter the upper limit:"))
for i in range(100,num1+1):
    temp=i
    sum=0
    count=len(str(i))

    while temp>0:
        digit=temp%10
        sum+=digit**count
        temp//=10 
    if i==sum:
        print(i,"amstrong")

# print prime numbers in the given range
num1=int(input("enter a number:"))
for i in range(2,num1+1):
    is_prime=True
        
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i) 
        