#1.print sum of palindrome numbers of list 
#i want output [4,9,13]
li = [121,333,421,563,454]
new_li = []
# if not li:
#     print('invalid list') 
for num in li:
    temp = num
    rev = 0
    while temp > 0:
        digit = temp%10
        rev =rev*10+digit
        temp//=10
        
    if num == rev:
        new_li.append(rev)
li2 = []
for valu in new_li:
    sum_val = 0
    
    while valu > 0:
        digit = valu%10
        sum_val += digit
        valu//=10
    li2.append(sum_val)
print(li2)


# li = [121, 333, 421, 563, 454]
# new_li = []


# for num in li:
#     temp = num
#     rev = 0
#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp //= 10
#     if num == rev:   
#         new_li.append(num)


# li2 = []
# for valu in new_li:
#     sum_val = 0     
#     while valu > 0:
#         digit = valu % 10
#         sum_val += digit
#         valu //= 10
#     li2.append(sum_val)

# print(li2) 


#2.when string values are in the same order from left to right then print True otherwise print False
# s= 'abcde'
# search_val = input('enter a string:')
# for ch in s:
#     if search_val in s:
#         print("True")
#         break
# else:
#     print("False")

#when string values are in the same order from left to right then print True otherwise print False
# s = 'abcde'
# search_val = input("enter a string: ")

# pos = 0
# for ch in search_val:
#     pos = s.find(ch, pos)  
#     if pos == -1:  
#         print("False")
#         break
#     pos += 1
# else:
#     print("True")

    
    
#3.print next character
# def next_char(s):
#     i = 0
#     while i < len(s):
#         if 'a' <= s[i] <= 'z':
#             print(chr(ord(s[i])+1),end=" ")
#         elif 'A' <= s[i] <= 'Z':
#             print(chr(ord(s[i])+1))
#         else:
#             print(s[i])
#         i +=1
# s = 'manoj'
# next_char(s)