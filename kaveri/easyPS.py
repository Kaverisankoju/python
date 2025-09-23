#VOWELS IN REVERSE OF A STRING
def vowels_in_rev(s):
    vowels='aeiouAEIOU'
    extracted_vowels=[ch for ch in s if ch in vowels]
    reversed_vowels="".join (extracted_vowels[::-1])
    print(reversed_vowels)
s=input('enter a string:')
vowels_in_rev(s)

#Unique vowels in the string
def unique_vowels(s):
    vowels='aeiouAEIOU'
    seen=set()
    unique=[]
    for ch in s:
        if ch in vowels and ch not in seen:
           unique.append(ch)
           seen.add(ch)
    print("".join(unique))
unique_vowels('helloworld')

#Remove dublicates/repeated values in the string
def remove_dublicates(s):
    unique=[]
   
    for ch in s:
        if s.count(ch)==1:
            unique.append(ch)
        
    print("".join(unique))
remove_dublicates('helloworld')

#convert Upper to Lower and Lower to Upper
#Method-1
def swap_case(s):
    result=s.swapcase()
    print(result)
s=input('enter a string combination of Upper and Lower:')
swap_case(s)
#method-2
def convertion_of_character_using_ASCII(s):
    result=""
    for ch in s:
        
        if 'A'<= ch <= 'Z':
            result+=chr(ord(ch)+32)
        elif 'a' <= ch <= 'z':
            result+=chr(ord(ch)-32)
        else:
            result+=ch
    print("after conversion of string",result)
convertion_of_character_using_ASCII('HeLLoWorLd')

#method-3
def convertion_of_character_using_ASCII(s):
    result=""
    for ch in s:
        ASCII_val=ord(ch)
        if 65<= ASCII_val <= 90:
            result+=chr(ASCII_val+32)
        elif 97<= ASCII_val<=122:
            result+=chr(ASCII_val-32)
        else:
            result+=ch
    print("after conversion of string",result)
convertion_of_character_using_ASCII('HeLLoWorLd')

#Uppercase characters comes first in reverse order
def rearrange_string(s):
    upper=[]
    lower=[]
    for ch in s:
        if ch.isupper():
            upper.append(ch)
        elif ch.islower():
            lower.append(ch)
    upper.reverse()
    print("".join(upper)+"".join(lower))
s=input('enter a string')
rearrange_string(s)
  
