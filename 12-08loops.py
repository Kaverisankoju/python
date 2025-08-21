# #PRIME NUMBER
#method-1

# num1=int(input("enter a number:"))
# count=0
# for i in range(1,num1+1):
#     if num1%i==0:
#         count+=1
# if count==2:
#     print("it is a prime number")
# else:
#     print("it is not a prime number")

#method -2
# num1=int(input("enter a number:"))
# if num1<=1:
#     print('invalid number')
# else:
#     flag=True
#     for i in range(2,num1):
#         if num1%i==0:
#             flag=False
#             print("It is not a prime...")
#             break
           
#     if flag==True:
#         print("It is Prime number...")
        
#convert same code using function
# def check_prime(num1):
#     if num1<=1:
#         return 'not a prime'
#     for i in range(2,num1):
#         if num1%i==0:
#             return 'Not a prime'
#     return 'Prime'
# n2=int(input("enter a number:"))
# print(check_prime(n2))

#method-3
# def check_prime(num1):
#     if num1<=1:
#         return 'False'
#     for i in range(2,num1//2+1):
#         if num1%i==0:
#             return 'False'
#     return 'True'
# n1=int(input('enter a number:'))
# print(check_prime(n1))


#Print prime numbers in the range 
# def prime_numbers(num1):
#     if num1<=1:
#         return 'Not a prime'
#     else:
#         for i in range(2,int(num1**0.5)+1):
#             if num1%i==0:
#                 return 'Not a prime'
#         return 'Prime'
# for n in range(10,21):
#     if prime_numbers(n):
#         print(n)
    
    
# def prime_numbers(num1):
#     if num1<=1:
#         return False
#     else:
#         for i in range(2,int(num1**0.5)+1):
#             if num1%i==0:
#                 return False
#         return True
# for n in range(10,21):
#     if prime_numbers(n):
#         print(n)
# print()

# for num in range(10,21):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#               break
#         else:
#             print(num,end=" ")
            
# primes=([n for n in range(10,21) if all(n%i!=0 for i in range(2,n))])
# print(primes)

# n=int(input("enter a number:"))
# print(f"numbers between 2 to{n}")
# for num in range(2,n):
#     for i in range(2,num):
#         if num%i==0:
#           break
#     else:
#        print(num)
    
# n=int(input("enter a number:")) 
# print("prime numbers between 2 and",n) 
# for num in range (2,n): 
#     for i in range(2,num): 
#        if num%i==0: 
#          break 
#     else: 
#       print(num,end=",")
# n=int(input("enter a number:"))
# for num in range(1,n+1):
#     if num>1:
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 break
#         else:
#             print(num)

#Fibonacci
# n1,n2=0,1
# n=int(input("enter a number:"))
# for i in range(n):
#     print(n1)
#     third_num=n1+n2
#     n1=n2
#     n2=third_num
    
# n1,n2=0,1
# n=int(input("enter a number:"))
# for i in range(n):
#     print(n1)
#     n1,n2=n2,n1+n2

#Armstrong 
# n=153
# temp=n
# sum=0
# k=len(str(n))
# while n>0:
#     digit=n%10
#     sum+=digit**k
#     n//=10
# if temp==sum:
#     print(sum,"it is amstrong number")
# else:
#     print(sum,"not a amstrong")
    
n=153

sum=0
k=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**k
    n//=10
if sum==n:
    print(sum,"it is amstrong number")
else:
    print(sum,"not a amstrong")