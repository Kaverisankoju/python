# reverse of string=>
# str1=input("enter the string:")

# print("reversed string:",str1[::-1])

#sum of digits=>
# n=int(input("enter the number:"))
# sum=0
# while n>0:
#     sum+=n%10
#     n//=10
# print("sum of digits is:" ,sum)

#palidrome check=>
# str1=input("enter the string:")
# if str1==str1[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

#fibonacci series
# n=int(input("enter the items:"))
# a,b=0,1
# for i in range(n):
#     print(a,end='')
#     a,b=b,a+b

#factorial number
# n=int(input("enter the number:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#max value of array=>
# arr=list(map(int,input("enter array elements  seperted by space").split()))
# print(max(arr))

#count vowels=>
# s=input("enter the string:")
# vowel='aeiou'
# count=0
# for ch in s:
#     if ch in vowel:
#         count+=1
# print(count)

#prime number check=>
# n=int(input("enter a number:"))
# if n<2:
#     print("not a prime")
#     for i in range(2,n):
#         if i%n==0:
#             print("not a prime")
# else:
#     print("it is a prime") 
        
#count of character=>
# s=input("enter the string:").strip()
# ch=input("enter the character:").strip()
# count=s.count(ch)
# print(count)

#amstrong number=>
# n=int(input("enter the number:"))
# original=n
# order=len(str(n))
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit**order
#     n//=10
# if sum==original:
#     print("armstrong")
# else:
#     print("not a armstrong")

#string manipulation(original to reversed sentence)=>
# s=input("enter the sentence")
# words=s.split()
# reversed_words=" ".join(words[::-1])
# print(reversed_words)

#duplicate handling=>
# arr=list(map(int,input("enter the numbers:").split()))
# unique=[]
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# print("unique values:",unique)

#array rotation=>
# arr=list(map(int,input("enter the numbers:").split()))
# arr.append(arr.pop(0))
# print("after rotation:"arr)

#sum and average of numbers=>
# arr=list(map(int,input("enter the numbers:").split()))
# total=sum(arr)
# average=total/len(arr)
# print("the sum is:",total)
# print("avg is:",average)

#serching=>
# arr=list(map(int,input("enter the numbers:").split()))
# key=int(input("enter the serching element"))
# found=False
# for i in range(len(arr)):
#     if arr[i]==key:
#         print("found at index:",i)
#         break;
#     else:
#         print("not found")


#sorting=>
# arr=list(map(int,input("enter the numbers:").split()))
# for i in range(len(arr)):
#     for j in range(0,len(arr)-i-1):
#        if arr[j]>arr[j+1]:
#            arr[j],arr[j+1]=arr[j+1],arr[j]    

# s='hello'
# s=s[::-1]
# print(s)

# n=int(input("enter the numbers:"))
# sum=0
# while n>0:
#     sum+=n%10
#     n//=10
# print(sum)

# str1=input("enter the string:")
# if str1==str1[::-1]:
#     print("it is a palindrome")
# else:
#     print("not a polindrome")

# n=int(input("enter the number:"))
# a,b=0,1
# for i in range(n):
#   print(a,end=' ')
#   a,b=b,a+b

# n=int(input("enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# arr=list(map(int,input("enter the numbers:").split()))
# print(max(arr))

# str1=input("enter the string:")
# vowel='aeiou'
# count=0
# for ch in str1:
#     if ch in vowel:
#         count+=1
# print(count)

# n=int(input("enter a number"))
# if n<2:
#     print("not a prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime")
#     else:
#         print("  prime")

# str1=input("enter the string:").strip()
# ch=input("enter the character:").strip()
# count=str1.count(ch)
# print(count)

# n=int(input('enter the number:'))
# original=n
# order=len(str(n))
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit**order
#     n//=10
# if sum==original:
#     print("amstrong")
# else:
#     print("not")

# def factorial(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# num=int(input('enter the number:'))
# temp=num
# sum_fact=0
# while temp>0:
#     digit=temp%10
#     sum_fact+=factorial(digit)
#     temp//=10
# if sum_fact==num:
#      print("strong")
# else:
#      print("not strong")

# str1=input("enter the sentence:")
# words=str1.split()
# reversed_words=' '.join(words[::-1])
# print("reversed_words:",reversed_words)

# n=list(map(int,input('enter the numbers:').split()))
# unique=[]
# for num in n:
#     if num not in unique:
#         unique.append(num)
# print('unique numbers are:',unique)

# arr=list(map(int,input('enter the arr').split()))
# arr.append(arr.pop(0))
# print("after rotation:",arr)

# n=list(map(int,input('enter number:').split()))
# total=sum(n)
# average=total/len(n)
# print('sum',total)
# print('avg',average)

# arr=list(map(int,input('enter number:').split()))
# key=int(input('enter the number:'))
# found=False
# for i in range(len(arr)):
#     if arr[i]==key:
#         print('found at index',i)
#         fount=True
#         break
# else:
#     print('not found')

# arr=list(map(int,input('enter number:').split()))
# n=len(arr)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print('sorted array',arr)


for i in range(0,200):
    if i%7==0 and i%9==0:
       print(i)