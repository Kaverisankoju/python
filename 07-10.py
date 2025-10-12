# #full diamand pattern
# # upper half
n = 5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
           print("*",end=" ")
    print()
# lower half   
for i in range(n-2,-1,-1):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
           print("*",end=" ")
    print()
         

# #square with some slope
n = 5
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(n):
        print("*",end=" ")
    else:
        print(" ",end=" ")
    print()

# #another side spaces
n = 5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range(n):
        print("*",end=" ")
    else:
        print(" ",end=" ")
    print()

# # (>) greater than pattern 
n = 5
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(n):
           print("*",end=" ")
    else:
        print(" ",end=" ")
    print()
for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range(n):
          print("*",end=" ")
    else:
        print(" ",end=" ")
    print()

# #(<) less than pattern
n = 5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range(n):
          print("*",end=" ")
    else:
        print(" ",end=" ")
    print()
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(n):
           print("*",end=" ")
    else:
        print(" ",end=" ")
    print()

# #Buterfly parttern
n = 7
for i in range(n):
    for j in range(n):
        if (i >= j and i + j <= n-1) or (i <= j and i + j >= n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #hoursglass parttern
n = 7
for i in range(n):
    for j in range(n):
        if (i <= j and i + j <= n-1) or (i >= j and i + j >= n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #full pyramid
n = 7
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(n):
        if i >= j:
            print("*",end=" ")
    else:
            print(" ",end=" ")
    print()

# #Inverted full pyramid
n = 7
for i in range(n):
    for k in range(i):
        print(" ",end="")
    for j in range(n):
        if i <= j:
            print("*",end=" ")
    else:
            print(" ",end=" ")
    print()

# #Hallow full pyramid
n = 7
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(n):
        if  j == 0 or i == n-1 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    else: 
            print(" ",end=" ")
    print()

# #number-pattern-1
n = 5
for i in range(n):
    for j in range(n):
        if i >= j:
          print(i+1,end=" ")
    else:
        print(" ",end=" ")
    print()

# #number-parttern-2

n = 5
for i in range(n):
    for j in range(n):
        if i >= j:
            print(j+1,end=" ")
    else:
            print(" ",end=" ")
    print()

# # number-parttern-3
n = 5
for i in range(n,-1,-1):
    for j in range(n,-1,-1):
        if i >= j:
          print(i,end=" ")
    else:
        print(" ",end=" ")
    print()

# #number-parttern-4
n = 5
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i <= j:
          print(i,end=" ")
    else:
        print(" ",end=" ")
    print()

#ASSIGNMENTS
#1.Square hallow pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#2.Number triangle pattern
n = 5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(n):
        if i >= j :
            print(i+1,end=" ")
        else:
            print(" ",end=" ")
    print()

#3. numbers increasing pattern
n = 5
for i in range(n):
    
    for j in range(n):
        if i >= j :
            print(j+1,end=" ")
        else:
            print(" ",end=" ")
    print()

#4.numbers increasing in reverse pyramid
n = 5
for i in range(n-1,0,-1):
    for j in range(1,i+1):
          print(j,end=" ")
    else:
        print(" ",end=" ")
    print()

#5.number changing pyramid
n = 5
curr = 1
for i in range(n):
    for j in range(1,n+1):
        if i >= j:
            print(curr,end=" ")
            curr += 1
        else:
            print(" ",end=" ")
    print()

#6.zero-one triangle parttern 
n = 5
for i in range(n):
    for j in range(1,i+1):
        if (i + j) % 2 == 0:
            if i >= j:
              print("1",end=" ")
        else:
            print("0",end=" ")
    print()

#7.Rhombus pattern 
n = 5
for i in range(n):
    for k in range(i):
        print(" ",end="")
    for j in range(n):
        print("*",end=" ")
    else:
        print(" ",end=" ")   
    print()    

#8.Diamond pattern
n = 5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
           print("*",end=" ")
    print()
# lower half   
for i in range(n-2,-1,-1):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
           print("*",end=" ")
  # print()
 
#9.Right half pyramid
n = 5
for i in range(n):
    for j in range(n):
        if i >= j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#10.Reverse Right half pyramid       
n = 5
for i in range(n):
    for j in range(n):
        if i + j <= n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#11.left-half pyramid
n = 5
for i in range(n):
    for j in range(n):
        if i + j >= n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#12.reverse left half pyramid 
n = 5
for i in range(n):
    for j in range(n):
        if i <= j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#13. K-Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i + j <= n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,n):
    for j in range(n):
        if i >= j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#14.Triangle start pattern
n = 5
for i in range(n):
    for k in range(n-1-i):
        print(" ",end="")
    for j in range(n):
        if i >= j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    

#15.reverse number triangle
n = 5
for i in range(1,n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(1,n):
        if i <= j :
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()    

#16.Mirror image
n = 5
for i in range(1,n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(1,n):
        if i <= j :
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()  
for i in range(n-1,0,-1):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(1,n):
        if i <= j :
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()  

#17.hallow triangle
n = 5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(n):
        if i == n-1 or j == 0 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#18.Hallow reverse Triangle pattern
n = 5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(n):
        if i == j or i == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
                
#19.right pascal's
n = 7
for i in range(n):
    if i % 2 == 0:
       visible = True
    else:
        visible = False
    for j in range(n):
        if ((i >= j) and (i + j <= n-1)):
            if visible == True:
               print("*",end=" ")
               visible = False
            else:
                print(" ",end=" ")
                visible = True
        else:
            print(" ",end=" ")
    print()

#Hallow Diamand Pyramid 
n = 5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        if j == 0  or i == j:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# lower half   
for i in range(n-2,-1,-1):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        if   j == 0 or i == j :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# #pascal's Triangle
n = 4
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    num = 1
    for j in range(i+1):
        if i >= j:
            print(num,end=" ")
            num = num * (i - j) // (j + 1)
    print()
 
#palindrome triangular
n = 5
for i in range(n):
    one_visited = False
    start = i+1
    for k in range(2*(n-i-1)):
        print(" ",end="")
    
    for j in range(2*i+1):
        print(start,end=" ") 
        if start == 1:
            one_visited = True
        if one_visited == False:
            start -= 1
        else:
            start += 1
        
    print()                                                                                          