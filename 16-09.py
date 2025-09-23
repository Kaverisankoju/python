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
    
#by using def function to search an element
def linear_serach(li,search_val):
    for i in range(len(li)):
        if li[i] == search_val:
            return i
    return 'no element found'
li = [23,36,3,6]
search_val = 36
print(linear_serach(li,search_val))

# def linear_search(li, search_val):
#     for i in range(len(li)):
#         if li[i] == search_val:
#             return i   # return index where element is found
#     return 'no element found'

# li = [23, 36, 3, 6]
# search_val = 36
# print(linear_search(li, search_val))

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
            flag = True
            str_li[i],str_li[i+1] = str_li[i+1],str_li[i]
    if not flag:
        break
print(str_li)

# bubble sort on string
s = 'akhjstj'
li_s = list(s)
for j in range(len(li_s)):
    for i in range(0,len(li_s)-j-1):
        if li_s[i] > li_s[i+1]:
            li_s[i],li_s[i+1] = li_s[i+1],li_s[i]
print(str(li_s))

       
#bubble sort on nested list based on first element
# nested_li = [[3,4],[8,9],[96,35],[30,4],[6,30],[4,6]]
# for j in range(len(nested_li)):
#     flag = False
#     for i in range(0,len(nested_li)-1-j):
#         if nested_li[i] > nested_li [i+1]:
#             nested_li[i],nested_li[i+1] = nested_li[i+1],nested_li[i]
#     if flag:
#         break
# print(nested_li)

#SORTING USING BUBBLE SORT
nested_li = [[3,4],[8,9],[96,35],[30,4],[6,30],[4,6]]
for j in range(len(nested_li)):
    flag = False
    for i in range(0,len(nested_li)-1-j):
        if nested_li[i][0] > nested_li [i+1][0]:
            nested_li[i],nested_li[i+1] = nested_li[i+1],nested_li[i]
    if flag:
        break
print(nested_li)

#sorted nested list
# nested_li = [[3,4],[8,9],[96,35],[30,4],[6,30],[4,6]]
# for nestes_li in nested_li:
#     for j in range(len(nested_li)):
#         for i in range(0,len(nested_li)-1-j):
#             if nested_li[i] > nested_li [i+1]:
#                 nested_li[i],nested_li[i+1] = nested_li[i+1],nested_li[i]
# for k in range(len(nested_li)):
#         for g in range(0,len(nested_li)-1-k):
#             if nested_li[g] > nested_li [g+1]:
#                 nested_li[g],nested_li[g+1] = nested_li[g+1],nested_li[g]
    
# print(nested_li)
