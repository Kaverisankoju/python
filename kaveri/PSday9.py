# #1.remove spaces
# s='he llo wor ld'
# result=""
# for ch in s:
#   if ch!=" ":
#       result+=ch
# print(result)  
# #2.reverse of str
# s='hello'
# rev=""
# for ch in s:
#     rev=ch+rev
# print(rev)
# #3.remove spaces and reverse the string
# s='he llo wor ld'
# result=""
# rev=""
# for ch in s:
#   if ch!=" ":
#       result+=ch
#       rev=ch+rev
# print(result)
# print(rev)

# #4.convert snake case to camel case
# s='my_variable_name'
# result=""
# i=0
# while i<len(s):
#     if s[i]=='_':
#         result+=s[i+1].upper()
#         i+=2
#     else:
#         result+=s[i]
#         i+=1
# print(result)
# #5.convert snake case to pascal
# s='my_variable_name'
# result=""
# i=0
# while i<len(s):
#     if i==0 or s[i-1]=='_':
#         if 'a'<=s[i]<='z':
#             result+=chr(ord(s[i])-32)    
#     elif s[i]!='_':
#         result+=s[i]
#     i+=1
# print(result)

# #6.camel to snake case
# s='myVariableName'
# result=""
# i=0
# while i<len(s):
#     if 'A'<=s[i]<='Z':
#         result+='_'
#         result+=chr(ord(s[i])+32)
#     else:
#         result+=s[i]
#     i+=1
# print(result)

# #7.camel to pascal
# s='myVariable'
# result=""
# i=0
# while i<len(s):
#     if i==0 :
#         if 'a'<=s[i]<='z':
#            result+=chr(ord(s[i])-32)
#     else:
#         result+=s[i]
#     i+=1
# print(result) 

# #8.pascal to camel case
# s='MyVariable'
# result=""
# i=0
# while i<len(s):
#     if i==0:
#         if 'A'<=s[i]<='Z':
#             result+=chr(ord(s[i])+32)  
#     else:
#         result+=s[i]
#     i+=1
# print(result) 

# #9.pascal to snake case
# s='MyVariable'
# result=""
# i=0
# while i<len(s):
#     if 'A'<=s[i]<='Z':
#         if i!=0:
#            result+='_'
#         result+=chr(ord(s[i])+32)
        
#     else:
#         result+=s[i]
#     i+=1
# print(result) 
     
# #10.text to camel case
# s='hello world example'
# result=""
# i=0
# while i<len(s):
#     if s[i]==" ":
#         i+=1
#         if i< len(s):
#             if 'a'<=s[i]<='z':
#               result+=chr(ord(s[i])-32)
#             else:
#                 result+=s[i]  
#     else:
#         result+=s[i] 
#     i+=1
# print(result)
#11.CONVERT TEXT TO SNAKE CASE
# s='hello world'
# result=""
# i=0
# while i<len(s):
#     if s[i]==" ":
        
#         result+='_'
#     else:
#         result+=s[i]
#     i+=1
# print(result)
#12.TEXT TO PASCAL CASE
# s='hello world'
# result=""
# i=0
# while i<len(s):
#     if i==0 or s[i-1]==' ':
#         if 'a'<=s[i]<='z':
#             result+=chr(ord(s[i])-32)
#     elif s[i]!=' ':
#         result+=s[i]
#     i+=1
# print(result)  


#13.SWAP UPPER AND LOWER CASE
# def swap_case(s):
#     result=""
#     i=0
#     while i < len(s):
#         if 'a' <= s[i] <= 'z':
#             result += chr(ord(s[i])-32)
#         elif 'A' <= s[i] <= 'Z':
#             result += chr(ord(s[i])+32)
#         else:
#             result += s[i]
#         i +=1
#     print("swacase of string result:",result)
# s = 'HeLLo'
# swap_case(s)
        
#14.SEPERATE DIGITS FROM TEXT
# def digits_from_string(s):
#     result=""
#     i = 0
#     while i < len(s):
#         if '0' <= s[i] <= '9':
#             result+=s[i]
#         i+=1
#     print(result)
# s='abc123d4'
# digits_from_string(s)

#15.PRINT UPPERCASE,LOWERCASE,DIGITS, AND SPECIAL CHARACTERS SEPERATLY
# def seperation_of_string(s):
#     uppercase_result=""
#     lowercase_result=""
#     digits_result=""
#     special_char_result=""
#     i=0
#     while i < len(s):
#         if 'A' <= s[i] <= 'Z':
#             uppercase_result+=s[i]
#         elif 'a' <= s[i] <= 'z':
#             lowercase_result+=s[i]
#         elif '0' <= s[i] <= '9':
#             digits_result+=s[i]
#         else:
#             special_char_result+=s[i]
#         i+=1
#     print("\n uppercases characters:",uppercase_result,end=" ")
#     print("\n lowercases characters:",lowercase_result,end=" ")
#     print("\n digits:",digits_result,end=" ")
#     print("\n special characters:",special_char_result,end=" ")
# s='AbC@12c3x!#'
# seperation_of_string(s)

#16. COUNT OF UPPER,LOWER,DIGITS AND SPECIAL CHARACTERS
# def seperation_of_string(s):
#     uppercase_result=""
#     upper_count=0
#     lowercase_result=""
#     lower_count=0
#     digits_result=""
#     digits_count=0
#     special_char_result=""
#     special_chr_count=0
#     i=0
#     while i < len(s):
#         if 'A' <= s[i] <= 'Z':
#             uppercase_result+=s[i]
#             upper_count+=1
#         elif 'a' <= s[i] <= 'z':
#             lowercase_result+=s[i]
#             lower_count+=1
#         elif '0' <= s[i] <= '9':
#             digits_result+=s[i]
#             digits_count+=1
#         else:
#             special_char_result+=s[i]
#             special_chr_count+=1
#         i+=1
#     print("upper count:",upper_count)
#     print("lower count:",lower_count)
#     print("digits count:",digits_count)
#     print("special charaters  count:",special_chr_count)
# s='AbC@12c3x!#'
# seperation_of_string(s)
    
#17.CHECK PASSWORD STRENGTH
# def check_password_strength(password):
#     i = 0
#     has_upper = False
#     has_lower=False
#     has_digits=False
#     has_special=False
#     while i < len(password):
       
#         if 'A' <= password[i] <= 'Z' :
#             has_upper = True
#         elif 'a' <= password[i] <= 'z':
#             has_lower = True
#         elif '0' <= password[i] <= '9':
#             has_digits = True
#         else:
#             has_special = True
#         i+=1
#     if has_upper and has_lower and has_digits and has_special:
#         print("Strong Password")
#     else:
#         print("Weak Password")
# password1='Pass123!'
# check_password_strength(password1)

#18.REMOVE DUBLICATES IN GIVEN INPUT
# def remove_dublicates(s):
#     unique=""
#     i=0
#     while i < len(s):
#         if s[i] not in unique:
#             unique+=s[i]
#         i+=1
#     print("after remove dublicates in the string:",unique)
# s='aaabbcccc'
# remove_dublicates(s)

#19.PRINT DUBLICATES IN THE STRING
# def dublicate_values(s):
#     dublicates=""
#     seen=""
#     i=0
#     while i < len(s):
#         if s[i] not in seen:
#             seen+=s[i]
#         elif s[i] not in dublicates:
#             dublicates+=s[i]
#         i+=1
#     print(dublicates)
# s='aaabbccd'
# dublicate_values(s)

#20. PRINT NEXT CHARACTER IN THE GIVEN STRING
def next_character(s):
    i=0
    while i < len(s):
        if 'a' <= s[i] <= 'z':
            print(chr(ord(s[i])+1),end=" ")
        elif 'A' <= s[i] <= 'Z':
            print(chr(ord(s[i])+1),end=" ")
        else:
            print(s[i],end=" ")
        i+=1
s='abc'
next_character(s)

# def next_character(s):
#     i = 0
#     while i < len(s):   # loop until last index
#         if 'a' <= s[i] <= 'z':  # check lowercase
#             print(chr(ord(s[i]) + 1), end=" ")  # get next character
#         elif 'A' <= s[i] <= 'Z':  # check uppercase also
#             print(chr(ord(s[i]) + 1), end=" ")
#         else:   # for non-alphabets, just print as is
#             print(s[i], end=" ")
#         i += 1

# s = 'abc'
# next_character(s)
