#LOOPS=>

# str1='python'
# for i in str1:
#     print(i)

# list1=[10,30,60]
# for n in list:
#     print(n)

# tup1=(3,6,9)
# for k in tup1:
#     print(k)

# set1={'hello',9.0,-7,6}
# for s in set1:
#     print(s,end=" ") #to get in same line
#     print(s,end=",") #TO GET VALUES WITH SEPERATED BY COMMA

# dict={
#   1:'kavya',
#   2:'Sankoju'  
# }
# for a in dict:
#     print(a)   if gets only keys

# dict={
#   1:'kavya',
#   2:'Sankoju'  
# }
# for a in dict.values():  # if gets values only
#     print(a) 

# dict={
#   1:'kavya',
#   2:'Sankoju'  
# }
# for a in dict.items(): # it gets key and value paires
#     print(a) 

# n='hello'
# for i in n[::-1]:
#     print(i) #reverse of str

# s='hello'
# count=0
# for i in s:
#     count+=1
# print(count)  #for counting the no.of characters in str

# n=20
# for i in range(0,n+1,2):
#     print(i)   #to print even numbers


# for i in range(1,11):
#      print("5 *" + str(i)+'='+str(5*i))  #to print multiples of 5

# n=2
# for i in range(1,11):
#     print(f"{n}x {i}={n*i}") #to print multiples of 2 in another method

# s='hello python'
# vowels='aeiou'

# for i in range(len(s)):
#     if s[i] in vowels:
        
         
#      print(s[i],end=",")

# s='hello python'
# vowels='aeiou'

# for i in s:
#     if i in vowels:
        
         
#      print(i,end=",") #another way

# n='hello world'
# for i in n:
#     if i in 'aeiouAEIOU':
#         print(i)  # in another way

# n='hello world'
# count=0
# for i in n:
#     if i in 'aeiouAEIOU':
#         count+=1
# print(count)  #to print count

# list=[2,3,5,0,9]
# total=0
# for i in range(len(list)):
#     total+=list[i]
# print(total)  # to print all the total value in the list

# n=int(input('enter a number:'))
# if n<=1:
#     print('not a prime')
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print('not a prime')
#             break
#     else:
#             print('prime')

# lit1=[3,9,66,79,34,20,99,87,45]
# total=0
# for i in lit1:
#     total+=i
# print(total)

# list1=[55,46,78,99,98,30,4,13,17,67,90]
# for i in list1:
#     if i%2==0:
#         print('even numbers are:',i, end=",")
#         i+=1
        
#     elif i%2!=0:
#         print('odd numbers are:',i, end=",")

# list1=[55,46,78,99,98,30,4,13,17,67,90]
# even_numbers=[]
# for i in list1:
#     if i%2==0:
#         even_numbers.append(i)
# print('even numbers are:',even_numbers)


# even_count=0
# odd_count=0
# for i in range(1,11):
#     if i%2==0:
        
#         even_count+=1
#     else:
        
#         odd_count+=1
# print('number of even numbers are:',even_count)
# print('number of odd numbers are:',odd_count)


n=list(map(int,input('enter the digits:').split()))
product=1
for i in n:
     product*=i
print('product of all digits is :',product)