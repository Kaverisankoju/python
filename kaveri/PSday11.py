#print all  primes from start to end 
# n=int(input('enter start number:'))
# m=int(input('enter last number:'))
# for i in range(n,m+1):
#     if i<2:
#         is_prime=False
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#     if is_prime:
#         print(i,end=" ")

#count number of primes in between start to end     
# n=int(input('enter start number:'))
# m=int(input('enter last number:'))
# count=0
# for i in range(n,m+1):
#     if i<2:
#         is_prime=False
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#     if is_prime:
#         print(i,end=" ")
#         count+=1        
# print("\n count no of primes",count)

#print all amstrong numbers from strat to end 
# n=int(input('enter start number:'))
# m=int(input('enter last number:'))

# for i in range(n,m+1):
#     length_num=len(str(i))
#     temp=i
#     sum_val=0
#     while temp>0:
#         digits=temp%10
#         sum_val+=digits**length_num
#         temp//=10
#     if i==sum_val:
#         print(i,end=" ")
        
#print first prime numbers in the range        
# n=int(input('enter start number:'))
# m=int(input('enter last number:'))
# for i in range(n,m+1):
#     if i<2:
#         is_prime=False
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#     if is_prime:
#         print(i,end=" ")
#         break


#print last prime 
# n=int(input('enter start number:'))
# m=int(input('enter last number:'))
# last_prime=-1
# for i in range(n,m+1):
#     if i<2:
#         is_prime=False
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#     if is_prime:
#         last_prime=i
# if last_prime!=-1:
#     print(last_prime)
# else:
#     print('no primes are present in the range')

#first vowel in a string
# s='krishna'
# vowels='aeiouAEIOU'
# for ch in s:
#     if ch in vowels:
#         print(ch)
#         break

#last vowel
# s='krishna'
# vowels='aeiouAEIOU'
# last_vowel=-1
# for ch in s:
#     if ch in vowels:
#         last_vowel=ch
# if last_vowel!=-1:
#     print(last_vowel)
# else:
#     print('their are no vowels in the string')

#print all even numbers using continue 
# n=int(input('enter a number:'))
# for i in range(1,n+1):
#     if i%2!=0:
#         continue
#     print(i,end=" ")

#print all odd numbers using continue
# n=int(input('enter a number:'))
# for i in range(1,n+1):
#     if i%2==0:
#         continue
#     print(i,end=" ")

#print all primes and composite numbers 
n=int(input('enter a number:'))
primes=[]
composite=[]
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        primes.append(i)
    else:
        composite.append(i)
print("primes are:",primes)
print("composite numbers are:",composite)
