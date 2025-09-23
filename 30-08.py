# def check_prime(n):
#     if n<2:
#         return False
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 return False
#         return True
# n1=int(input('enter a number:'))
# print(check_prime(n1))

# def check_prime(n):
#     if n>2:
#         return False
#     count=0
#     for i in range(2,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return True
#     return False        
# n=int(input('enter a number')) 
# print(check_prime(n))

# def check_prime(n):
#     if n>2:
#         return False
    
#     for i in range(2,n):
#         if n%i==0:
#             return False
    
#     return True        
# n=int(input('enter a number')) 
# print(check_prime(n))

# def check_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True      
# n=int(input('enter a number:')) 
# next_num=n+1
# while True:
#     if check_prime(next_num):
#         print('next prime number of given number is',next_num)
#         break
#     next_num+=1



#METHOD-1
# a,b,c=2,1,3
# if a<=b and a<=c:
#     print(b+c)
# elif b<=c and b<=a:
#     print(a+c)
# else:
#     print(a+b)

#METHOD-2    
# a,b,c=5,1,2
# if a>=b and a>=c:
#     if b>=c: 
#      print(a+b)
#     else:
#       print(a+c)
# elif b>=a and b>=c:
#     if a>=c:
#         print(b+a)
#     else:
#         print(b+c)
# else:
#     if a>=b:
#         print(c+a)
#     else:
#         print(c+b)
 
# s="aaabbaaaccbb" 
# res=s[0]
# count=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         count+=1
#     else:
#         res=res+str(count)+s[i]
#         count=1
# res+=str(count)
# print(res)