#all zero's in the matrix
#method-1
l = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] > 0:
            l[i][j] = 0
print(l)

#method-2
l = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]
for i in range(len(l)):
    for j in range(len(l)):
        
            l[i][j] = 0
print(l)

#method-3 
l = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]
for i in range(len(l)):
    for j in range(len(l)):
        print(0,end=" ")
    print()

#sum of matrix
l = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]

for i in l:
    sum_val = 0
    for j in i:
        sum_val += j
    print(sum_val)

#diagonal value zero
l = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]
for i in range(len(l)):
    l[i][i] = 0
print(l)

#method-2
l = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]
for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            l[i][j] = 0
print(l)

#another side of diagonal values zero
#method-1
l = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]
n = len(l)
for i in range(n):
    l[i][n-1-i] = 0
print(l)

#method-2
l = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]
n = len(l)-1
for i in range(len(l)):
    for j in range(len(l)):
        if j == n:
            print(0,end=" ")
            n -= 1
        else:
            print(l[i][j],end=" ")
    print()
    
