#LINEAR SEARCH
#Method-1
li = [2,3,36,90,46,54,32]
x = 36
for idx in range(0,len(li)-1):
    if li[idx] == x:
        print(f"{x} is fount at {idx}")
        break
else:
    print("element not found")

#using flag variable 
#Method-2
li = [2,3,36,90,46,54,32]
x = 100
flag = True
for idx in range(0,len(li)-1):
    if li[idx] == x:
        flag = False
        print(idx)
        break
    
if flag:
    print("element not found")

#using bubble sort decending order
li = [1,90,67,84,56,43,23,45,96]
for j in range(len(li)):
    flag = False
    for i in range(0,len(li)-1):
        if li[i] < li[i+1]:
            flag = True
            li[i],li[i+1] = li[i+1],li[i]
    if flag == False:
        break
print(li)
    
#using bubble sort to string based on length of string
    
str_li = ['python','java','os','DBMS','C','Data science']
for j in range(len(str_li)):
    flag = False
    for i in range(0,len(str_li)-1-j):
        if len(str_li[i]) > len(str_li[i+1]):
            falg = True
            str_li[i],str_li[i+1] = str_li[i+1],str_li[i]
    if not falg:
        break
print(str_li)
        
#bubble sort on nested list based on first element
nested_li = [[3,4],[8,9],[96,35],[30,4],[6,30],[4,6]]
for j in range(len(nested_li)):
    flag = False
    for i in range(0,len(nested_li)-1-j):
        if nested_li[i][0] > nested_li [i+1][0]:
            nested_li[i][0],nested_li[i+1][0] = nested_li[i+1][0],nested_li[i][0]
    if flag:
        break
print(nested_li)

