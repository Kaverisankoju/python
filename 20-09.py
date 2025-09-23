#unique and dublicate
li = [1,2,3,2,1,3,4,5,6]
u = []
d = []
for i in li:
    if li.count(i) == 1:
        u.append(i) 
    else:
        if li.count(i) > 1:
            if i not in d:
                d.append(i)
        
print("unique",u)
print("dublicates",d)

#reverse of array or list
li = [1,2,3,4,5]
low = 0
high = len(li)-1
while low < high:
     li[low],li[high] = li[high],li[low]
     low += 1
     high -=1
print(li)

# #check arr1 is subarray of arr2
# #method-1
arr1 = [1,2,3]
arr2 = [1,2,3,6,9]
print(set(arr1).issubset (set(arr2)))

# #Method -2
arr1 = [1,2,3]
arr2 = [1,2,3,6,9]
c = 0
for i in arr1:
    if i in arr2:
        c += 1
if c ==  len(arr1):
    print("subset")
else:
    print("not a subset")
    
# #print the prime number character value
# #method-1
for i in range(65,90):
    flag = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            flag = False
            break
    if flag:
       print(chr(i))

# #method -2
for i in range(ord('a'),ord('z')+1):
    # print(i)
    c = 0
    for j in range(1,i+1):
        if i % j ==0:
            c += 1
    if c == 2:
        print(chr(i),end=" ")
    
#finding next prime number of given number

n = 4
while True:
    flag = True
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            flag = False
            break
    
    if flag:
       print(n)
       break
    n += 1
# upto that number print fibonacci series
a,b = 0,1
for j in range(n):
    print(a,end=" ")
    a,b = b,a+b

# fibonacci series upto given number
n = 7
a,b =0,1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b
    
#Assignment
#Wap to check if each number in an  list contains duplicate digits, returning true for duplicates and false for unique digits.
#Input: [202,89,112,88]       	Output:[true ,false ,true ,true]

li =  [202,89,112,88] 
li1 = []   
for i in li:
    s = str(i) 
    has_dublicate = False
    for digits in s:
        if s.count(digits) > 1:
            has_dublicate = True
            break
    li1.append(has_dublicate)
print(li1)

#Sum of all numbers in a matrix.
matrix = [[1,2,3],
          [5,6,7],
          [2,3,1]
]
sum_val = 0
for row in matrix:
    for num in row:
        sum_val += num
print(sum_val)
        
matrix = [[1,2,3],
          [5,6,7],
          [2,3,1]
]
sum_val = 0
for row in range(0,len(matrix)):
    for num in range(len(matrix[row])):
        sum_val += matrix[row][num]
print(sum_val)
        