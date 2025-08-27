#STRING=> built-in functions

#Accessing string elements
str1='python'
print(str1[0])
print(str1[-1])
# print(str1[10]) #error=>IndexError: string index out of range

#string slicing
str2='python'
print(str2[0:3])
print(str2[:3])
print(str2[2:])
print(str2[:-3])
print(str2[-2:])
print(str2[16:16]) #o/p=>empty string

#Concatenation
s1="hello"
s2="python"
result=s1+" "+s2
print(result)

#Repetation
s1="HI! "
print(s1*3)
s1="HI!"
print(s1*3)

#Strip()
text="    python    "
print(text.strip())
text="    python    programming    "
print(text.strip())

#lower()
text="HELLO world"
print(text.lower())

#upper()
text="python world"
print(text.upper())

#find(substring)
text="python world"
print(text.find('o'))
print(text.find('world'))
print(text.find('k')) #o/p:gives -1
print(text.find('hello')) #o/p:gives -1

#replace(old,new)
text="python world"
print(text.replace('python','hello'))
print(text.replace('o','a'))
print(text.replace('b','k')) #o/p:gives original string

#split(delimiter)
text='a,b,c'
print(text.split(','))
text='a ,b ,c '
print(text.split(' '))
text='a,b,c,ce '
print(text.split('c'))

#startwith(prefix)
text='hello'
print(text.startswith('h'))
text='hello'
print(text.startswith('H'))
text='hello'
print(text.startswith('e'))
text='hello'
print(text.startswith('hel'))

#endswith(suffix)
text='hello'
print(text.endswith('o'))
text='hello'
print(text.startswith('lo'))
text='hello'
print(text.startswith('llo'))
text='hello'
print(text.startswith('ello'))

#count(substring)
text='python world'
print(text.count('o'))
text='python world'
print(text.count('s')) 
text='python world'
print(text.count('orl'))


