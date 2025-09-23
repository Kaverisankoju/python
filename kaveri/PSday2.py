# def prime_numbers(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#            return False
#     return True    
# for n in range(1,5):
#     if prime_numbers(n):
#         print(n,end=" ")

#DOC-3

#01=>
# input_num=int(input('enter a number:'))
# for i in range(1,input_num+1):
#     print(i,end=" ")

#02=>        
# start_num=int(input('enter start number:'))
# end_num=int(input('enter end number:'))
# for i in range(start_num,end_num+1):
#     print(i,end=" ")

#03=>
# input_num=int(input('enter a number:'))
# for i in range(input_num,0,-1):
#     print(i,end=" ")

#04=>
# start_num=int(input('enter start number:'))
# end_num=int(input('enter end number:'))
# for i in range(start_num,end_num-1,-1):
#     print(i,end=" ")

#05=>
# n=int(input('enter a number:'))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

#06=>
# n=int(input('enter a number:'))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#07=>
# n1=int(input('enter start number:'))
# n2=int(input('enter end number:'))
# sum=0
# for i in range(n1,n2+1):
#     sum+=i
# print(sum)

#08=>
# n1=int(input('enter start number:'))
# n2=int(input('enter end number:'))
# product=1
# for i in range(n1,n2+1):
#    product*=i
# print(product)

#09=>
# n=int(input('enter a number:'))
# print("factors of",n,"are",end=" ")
# for i in range(1,n+1):
#     if n%i==0:  
#       print(i, end=" ")

#10=>
# n=int(input('enter a number:'))
# factors=0
# for i in range(1,n+1):
#     if n%i==0:
#         factors+=1
# print(factors)

#11=>        
# def prime_check(n):
#     if n<2:
#         return 'not a prime'
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#            return 'not a prime'
#     return 'prime'
# n=int(input('enter a number:'))
# print(prime_check(n))

#12=>
# n1=int(input('enter start number:'))
# n2=int(input('enter end number:'))
# for i in range(n1,n2+1):
#     if i%2==0:
#         print(i,end=" ")

#13=>
# n1=int(input('enter start number:'))
# n2=int(input('enter end number:'))
# for i in range(n1,n2+1):
#     if i%2!=0:
#         print(i,end=" ")

#14=>
# n1=int(input('start:'))
# n2=int(input('end:'))
# even_count=0
# odd_count=0
# for i in range(n1,n2+1):
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print('total even numbers within give range are:',even_count)
# print('total odd numbers within give range are:',odd_count)

#15=>
# s='python'
# print(s[::-1])

# s='hello'
# res=""
# for ch in s:
#     res=ch+res
# print(res)
    
# s='python'
# print("".join(reversed(s)))

#16=>
# s='madam'
# res=""
# for ch in s:
#     res=ch+res
# if res==s:
#     print('palindrome')
# else:
#     print('not palindrome')

#17=>
# n=int(input('enter a number:'))
# prod=1
# while n>0:
#     digit=n%10
#     prod=prod*digit
#     n//=10
# print(prod)

#18=>
# n=int(input('enter a number:')) 
# temp=n
# sum=0
# count=0
# while temp>0:
#       count+=1
#       temp//=10
# print(count) 
# temp=n
# while temp>0:
#     digit=temp%10
#     sum+=digit**count
#     temp//=10    
# if sum==n:
#     print(n,'is amstrong')
# else:
#     print('not a amstrong')

#print amstrong numbers in the given range
# n=int(input('enter a number:')) 
# for i in range(1,n+1):
#     temp=i
#     sum=0
#     count=0
#     while temp>0:
#         count+=1
#         temp//=10
    
#     temp=i
#     while temp>0:
#         digit=temp%10
#         sum+=digit**count
#         temp//=10    
#     if sum==i:
#         print(i,end=" ")
        
#20=>
# n=int(input('enter a number:'))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print('reverse of a number is',rev)

#21=>
# n=int(input('enter a number:'))
# temp=n
# rev=0
# while temp>0:
#     digit=temp%10
#     rev=rev*10+digit
#     temp//=10
# if rev==n:
#     print(n,'is palindrome')
# else:
#     print(n,'not a palindrome')

#22=>
# s=input('enter a string:')
# vowels='aeiouAEIOU'
# count=0
# for ch in s:
#     if ch in vowels:
#         count+=1
# print('count of vowels in the string',count)

#23=>
# s=input('enter a string:')
# vowels='aeiouAEIOU'
# count=0
# for ch in s:
#     if ch not in vowels:
#         count+=1
# print('count of consonates in the string',count)

#24=>
# n=int(input('enter a number:'))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print(n,'is perfect number')   
# else:
#     print(n,'is not a perfect number')

#to find factors of a given number
# n=int(input('enter a number:'))
# factors=[]
# for i in range(1,n+1):
#     if n%i==0:
#         factors.append(i)
# print(factors)

#26=>
# n=int(input('enter a number:'))
# square=n*n
# digit_sum=0
# while square>0:
#     digit=square%10
#     digit_sum+=digit
#     square//=10
# if digit_sum==n:
#     print(n,'is neon number')
# else:
#     print(n,'not a neon number')

#27=>
# import math
# n=int(input('enter a number:'))
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=math.factorial(digit)
#     temp//=10
# if sum==n:
#     print(n,'is strong number')
# else:
#     print(n,'is not a strong number')

#28=>
# n=int(input('enter a number:'))
# digit_sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     digit_sum+=digit
#     temp//=10
# if n%digit_sum==0:
#     print(n,'harshad number')
# else:
#     print(n,'not a harshad number')

#29=>
# n=int(input('enter a number:'))
# a,b=0,1
# for i in range(n):
#     print(a, end=" ")
#     a,b=b,a+b

#30=>
# n=int(input('enter a number:'))
# square=n*n
# digit_sum=0
# while square>0:
#     digit=square%10
#     digit_sum+=digit
#     square//=10
# if digit_sum==n:
#     print(n,'is neon number')
# else:
#     print(n,'not a neon number')
