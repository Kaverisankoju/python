# check the the second string is subset of first string or not, if it is substring find the starting index of second string in first string
s1 = 'helloworld'
s2 = 'rld'
if s2 in s1:
    print("index of sub string is:",s1.index(s2))
else:
    print('not a sub string')

#  find the largest word in given string without using split menthod
s = 'hello how are you'
l = []
s1 = ""
for ch in s:
    if ch == " ":
        l.append(s1)
        s1 = ""
    else:
        s1 += ch
l.append(s1)
print(l)
b = 0
for i in l:
    count = 0
    for j in i:
        count += 1
    if b < count:
        b = count
print(b)
for i in l:
    if b == len(i):
        print("largest word in the string is:",i)
    
        