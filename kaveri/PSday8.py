# n = int(input('Enter a number: '))
# primes = []

# for i in range(2, n+1):  
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(i)

# print("Prime numbers:", primes)

# n = int(input('Enter a number: '))
# primes = []
# count = 0

# for i in range(2, n+1):   
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(i)
#         count += 1

# print("Prime numbers:", primes)
# print("Total prime count:", count)

#primes without using append method 
# n=int(input('enter a number:'))
# primes=[i for i in range(2,n+1) if all(i%j!=0 for j in range(2,int(i**0.5)+1))]
# print("primes",primes)
# print("count",len(primes))

#Amstrong numbers from 1 to given number
# n=int(input('enter a number:'))
# ams=[]
# for i in range(1,n+1):
#     length_i=len(str(i))
#     temp=i
#     sum_val=0
#     while temp>0:
#         digits=temp%10
#         sum_val+=digits**length_i
#         temp//=10
#     if i==sum_val:
#         ams.append(i)
# print("amstrong numbers are:",ams)
        
#all even numbers  from 1 to 100
#method-1
# n=int(input('enter a number:'))
# even=0
# even_number=[i for i in range(1,n+1) if (i%2==0)]
# print(even_number)

# #method-2      
# n=int(input('enter a number:'))
# even=[]
# for i in range(1,n+1):
#     if i%2==0:
#         even.append(i)

# print("even numbers are",even)

n=int(input('enter a number:'))
even=0
even_number=[i for i in range(1,n+1) if (i%2==0)]
print("even numbers are",even_number) 
print(len(even_number))       