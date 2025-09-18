#LINEAR SEARCH
#Method-1
#T.C = O(n), S.C = O(1)
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
#T.C = O(n)
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
# T.C = O(n)
def linear_serach(li,search_val):
    for i in range(len(li)):
        if li[i] == search_val:
            return i
    return 'no element found'
li = [23,36,3,6]
search_val = 36
print(linear_serach(li,search_val))

#using bubble sort decending order
# T.C = O(n*n), S.C = O(1)
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
# T.C = O(n*n), S.C = O(1)
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
# T.C = O(n*n), S.C = O(1)
s = 'akhjstj'
li_s = list(s)
for j in range(len(li_s)):
    for i in range(0,len(li_s)-j-1):
        if li_s[i] > li_s[i+1]:
            li_s[i],li_s[i+1] = li_s[i+1],li_s[i]
print(str(li_s))

#SORTING USING BUBBLE SORT
# T.C = O(n*n), S.C = O(1)
nested_li = [[3,4],[8,9],[96,35],[30,4],[6,30],[4,6]]
for j in range(len(nested_li)):
    flag = False
    for i in range(0,len(nested_li)-1-j):
        if nested_li[i][0] > nested_li [i+1][0]:
            flag = True
            nested_li[i],nested_li[i+1] = nested_li[i+1],nested_li[i]
    if flag:
        break
print(nested_li)


#number of swapcount in the list using bubble sort
#T.C = O(n*n) and S.C = O(1)
def number_of_swaps(li):
    swap_count = 0
    for i in range(len(li)):
        for j in range(0,len(li)-1-i):
            if li[j] < li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                swap_count += 1
    print("swaped list",li)
    print("swapcount is",swap_count)
li = [65,89,90,35,46,30,43,12,3]
number_of_swaps(li)

#Binary serach
# T.C = O(logn), S.C = O(1)
li = [1,2,3,20,30,90]
search_val = 3
low = 0
high = len(li)-1
while low < high:
    mid = (low + high)//2
    if li[mid] == search_val:
        print(mid,'element found')
        break
    elif li[mid] > search_val:
        high = mid - 1
    else:
            low = mid + 1
else:
    print('element not found')
    
    
#using binary search find first half of element
#T.C = O(logn) and S.C =O(1)
def binary_search_on_first_half(li,search_val):
    low = 0
    high = (len(li)//2)-1
    while low < high:
        mid = (low + high)//2
        if li[mid] == search_val:
            print(f"found value at index {mid}")
            return
        elif li[mid] < search_val:
            low = mid+1
        else:
            high = mid-1
    print("element not found")

li = [3, 12, 30, 35, 43, 46, 65, 89, 90]
search_val = 12
binary_search_on_first_half(li,search_val)     

