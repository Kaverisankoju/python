# #Solid Square Pattern/ canvas
n = 5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
    

# #Middle Row Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #Middle Column Pattern
n = 5
for i in range(n):
    for j in range(n):
        if j == n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# #Left-Aligned Right-Angled Triangle
n = 5
for i in range(n):
    for j in range(n):
        if i > j or i == j:
            print("*",end=" ") 
    print()


# #Inverted Left-Aligned Triangle
n = 5
for i in range(n):
    for j in range(n):
        if i < j or i == j:
            print("*",end=" ") 
    print()

# #Right-Aligned Right-Angled Triangle
n = 5
for i in range(n):
    for j in range(n):
        if i < j or  i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()

# #Inverted Right-Aligned Triangle
n = 5
for i in range(n):
    for j in range(n):
        if i + j > n-1 or  i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()


# #Hollow Right Arrow Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i < j or  i == j or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()

# #Filled Down Arrow Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i + j > n-1 or  i + j == n-1 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()

# #Filled Up Arrow Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i + j < n-1 or i + j == n-1 or i == j: 
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()

# #Filled “X” Shape
n = 5
for i in range(n):
    for j in range(n):
        if i > j or i == j or i + j == n-1:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()


# #South-East Arrow Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i + j > n-1  or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #North-West Arrow Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i + j < n-1  or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# #Hollow “X” with Top and Bottom Borders
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i == j or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #Hollow “X” with Left and Right Borders
n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == j or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# #Hollow “X” with Bottom and Left Border
n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1 or i == j or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #Hollow “X” with Top and Right Border
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == n-1 or i == j or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# #Hollow “X” with Left and Top Border
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == j or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# #
n = 5
for i in range(n):
    for j in range(n):
        if i == n-1 or j == n-1 or i == j or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# #hallow square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# #hallow triangle all types right-aligned and left-aligned
n = 5
for i in range(n):
    for j in range(n):
        if i == n-1 or j == 0 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #Hollow “X” with Right and Bottom Border
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #Hollow Square Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == n-1 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #Hollow Left-Aligned Right-Angled Triangle
n = 5
for i in range(n):
    for j in range(n):
        if i == n-1 or j == n-1 or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#alphabates
#1.A
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n-1 or i == n//2:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#2.B
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n-1 or i == n-1 or i == n//2:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#3.C
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#4.D
n = 5
for i in range(n):
    for j in range(n):
        if (i == 0 or j == 0 or i == n-1 or j == n-1) and not((j == n-1 and i == n-1) or (i == 0 and j == n-1)):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#5.O
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#5.E
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or i == n//2:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#6.F
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0  or i == n//2:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#7.G
n = 5
mid = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or (j == n-1 and i >= mid) or (i == mid and j >= mid):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#8.H
n = 5
for i in range(n):
    for j in range(n):
        if  j == 0 or j == n-1 or i == n//2:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#9.I
n = 5
for i in range(n):
    for j in range(n):
        if  i == 0 or j == n//2 or i == n-1:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#10.J
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == n//2 or (i == n-1 and j <= n//2) or (j == 0 and i >= n//2):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#11.K
n = 4
for i in range(n):
    for j in range(n):
        if  j == 0 or i + j == n-1:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(1,n):
    for j in range(n):
        if  j == 0 or i == j:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#12.L
n = 5
for i in range(n):
    for j in range(n):
        if  j == 0 or i == n-1:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#13. M (i== j and j <= mid)
n = 5
mid = n//2
for i in range(n):
    for j in range(n):
        if  j == 0 or j == n-1 or (i == j and j <= mid) or (i + j == n-1 and j >= mid ):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#14.N
n = 5
for i in range(n):
    for j in range(n):
        if  j == 0 or j == n-1 or i == j:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#15.O
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#16.P
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n//2 or (j == n-1 and i < n//2):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#17.Q
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1 or (i == j and j >= n//2):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n+1):
    if i == n:
        print("*",end=" ")
    else:
        print(" ",end=" ")


#18.R
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or (i == n//2 and j >= n//2) or (i == j and j >= n//2) or (j == n-1 and i <= n//2):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#19.S
n = 5
mid = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or (j == 0 and i <= mid) or i == mid or (j == n-1 and i >= mid) or i == n-1 :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#20.T
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == n//2 :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#21.U
n = 5
for i in range(n):
    for j in range(n):
        if i == n-1 or j == 0 or j == n-1 :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#22.V
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == 0 or i + j == n-1 :
#            print(" *",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n = 5
for i in range(n):
    for j in range(n):
        if (j == 0 and i < n -2) or (i + j == n-1 and i > n//2) or (j == n-2 and i < n-2) or (i == n - 1 and j == n // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



#23.W
n = 5
mid = n//2
for i in range(n):
    for j in range(n):
        if  j == 0 or j == n-1 or (i == j and j >= mid) or (i + j == n-1 and j <= mid ):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#24.X
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n-1 :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#25.Y
n = 5
for i in range(n):
    for j in range(n):
        if (i == j and j <= n//2) or i + j == n-1 :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#26.Z
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i + j == n-1 :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
