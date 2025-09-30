#identify the given matrix is identity matrix or not 
m = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
is_identity = True
for i in range(len(m)):
    for j in range(len(m)):
        if i == j and m[i][j] != 1:
            is_identity = False
        elif i != j  and m[i][j] != 0:
            is_identity = False
if is_identity:
    print('identity matrix')
else:
    print('not a identity matrix')

#sum of two matrixes
m1 = [
    [1,2,3],
    [3,2,4],
    [4,3,0]
]
m2 = [
    [1,1,1],
    [2,2,2],
    [3,3,3]
]

result = []
for i in range(len(m1)):
    row = []
    for j in range(len(m1[0])):
        row.append (m1[i][j] + m2[i][j])
    result.append(row)
print(result)
    
   
#sum of one diagonal elements
m1 = [
    [1,2,3],
    [3,2,4],
    [4,3,6]
]
sum_val = 0
for i in range(len(m1)):
    for j in range(len(m1)):
        if m1[i] == m1[j]:
            sum_val += m1[i][j]
print(sum_val)

#sum of another diagonal
m1 = [
    [1,2,3],
    [3,3,4],
    [4,3,6]
]
sum_val = 0
for i in range(len(m1)):
    for j in range(len(m1)):
        if (i + j == len(m1)-1) :
            sum_val += m1[i][j]
print(sum_val) 

#sum of two sides diagonal elements 
m1 = [
    [1,2,3],
    [3,3,4],
    [4,3,6]
]
sum_val = 0
for i in range(len(m1)):
    for j in range(len(m1)):
        if (i + j == len(m1)-1) or i == j :
            sum_val += m1[i][j]
print(sum_val) 

#sum of same diagonal adds two times 
m1 = [
    [1,2,3],
    [3,3,4],
    [4,3,6]
]
sum_val = 0
for i in range(len(m1)):
    for j in range(len(m1)):
        if  i == j :
            sum_val += m1[i][j]
        if i + j == len(m1)-1:
            sum_val += m1[i][j]
print(sum_val) 


#two matrix multiplication
m1 = [
    [1,2,3],
    [3,2,4],
    [4,3,0]
]
m2 = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

result = []

for i in range(len(m1)):
    row = []
    for j in range(len(m1[0])):
        row.append(m1[i][j] * m2[j][i])
    result.append(row)

print(result)

#Transpose of Matrix
m1 = [
    [1,2,3],
    [3,2,4],
    [4,3,0]
]
for i in range(len(m1)):
    for j in range(len(m1[i])):
        if i > j:
           m1[i][j],m1[j][i] = m1[j][i],m1[i][j]
for i in range(len(m1)):
    for j in range(len(m1[i])):
        print(m1[i][j],end=" ")
    print()
    
#print diagonal elements 
m1 = [
    [1,2,3],
    [3,2,4],
    [4,3,0]
]
for i in range(len(m1)):
    for j in range(len(m1)):
        if i == j:
            print(m1[i][j])
        
        else:
            print(" ",end=" ")
    print()

#second side diagonal
m1 = [
    [1,2,3],
    [3,2,4],
    [4,3,0]
]
for i in range(len(m1)):
    for j in range(len(m1)):
        if i + j == len(m1)-1:
            print(m1[i][j])
        
        else:
            print(" ",end=" ")
    print()

#Hallow matrix
m1 = [
    [1,2,3],
    [3,2,4],
    [4,3,0]
]
for i in range(len(m1)):
    for j in range(len(m1)):
        if i == 0 or j == 0 or i == len(m1)-1 or j == len(m1[i])-1:
            print(m1[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
    




