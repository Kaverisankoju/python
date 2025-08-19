# char='k'
# print(char.upper())
# print(char.isupper())

# char='k'
# for i in char:
#     if char.isupper():
#         print(f"{char} is upper")
#     elif char.islower():
#        print(f"{char} is lower")
#     else:
#         print(f"{char} it is in number")

# n='k'
# for i in n:
#     if 'a'<= i<='z':
#         print('lower case')
#     else:
#         print('upper case')

# n='K'
# for i in n:
#     if n.upper():
#       print(n.lower())
#     else:
#         print(f'{n} is upper')
        
# #without using built in functions code       
# n='k'
# for i in n:
#     if 'A'<=i<='Z':
#         print(n.upper())
#     else:
#         print('it is lower case')
        
# text=input('enter the text')        
# i=0
# while i<=len(text):
#     char=text[i]
#     if 

# print(ord('A'))
# print(ord('a'))

# n=input('enter the str:')
# for i in n:
#     if 'A'<=i<='Z':
#         res=chr(ord(i)+32) # every same(A,a)(K,k)etc character difference is 32
#         print(res)
#     else:
#         print('already it is lower case')    



# lis1=[6,7,9,0,3,2,1]
# even_numbers=[]
# for i in lis1:
#     if i%2==0:
#         even_numbers.append(i)
# print(even_numbers)


# lis1=[6,7,9,0,3,2,1]
# even_numbers=[]
# count=0
# for i in lis1:
#     if i%2==0:
#         even_numbers.append(i)
#         count+=1
# print(even_numbers)
# print(count)

# l=[87,39,99,90,45,34]
# for i in l:
#     if i%2==0:
#         print(i,end=",")

# for i in range(1, 11):
#     if i % 7 == 0 and i % 9 == 0:
#           print(i)


# n=int(input('enter any number:'))
# factors=[]
# for i in range(2,n):
# #     if  n%i==0:
# #         factors.append(i)
# # print(factors)


# i=1
# even_numbers=[]
# while i<=10:
#     if i%2==0:
#         even_numbers.append(i)
#     i+=1
# print(even_numbers)


# total=0
# for i in range(1,6):
#     total+=i
# print('sum of first 5 numbers is:',total)


# str=input('enter the string:')
# if str.isupper():
#     print('it is in upper case')
# else:
#     print('it is in lower case')
  
char=input('enter a single character:')
for i in char:
    if 'A'<=i<='Z':
        result=chr(ord(i)+32)
        print(result)
    else:
        print('it is already in lower case')
        
    