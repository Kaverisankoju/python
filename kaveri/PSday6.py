#1.solid square 
# n=int(input('enter a number:'))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

#2.Solid Rectangle Pattern	
# m=3
# n=5
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

#3.Right-Angled Triangle (Left-Aligned)
# n=5
# for i in range(1,n+1):
#        print("*" * i)
# print()
#4. Right-Angled Triangle (Right-Aligned)
# n=5
# for i in range(1,n+1):
#        print(" "*(n-i)+"*"*i)
# print()

#5.Inverted Triangle (Left-Aligned)
# n=5
# for i in range(n,0,-1):
#        print("*" * i)
# print()

#6.Inverted Triangle (Right-Aligned)
# n=5
# for i in range(n,0,-1):
#        print(" "*(n-i)+"*"*i)
# print()

#7.Centered Pyramid Pattern
# n=5
# for i in range(1,n+1):
#        print(" "*(n-i)+"*"*(2*i-1))  
# print()

#8. Diamond Pattern
# n=5
# for i in range(1,n+1):
#        print(" "*(n-i)+"*"*(2*i-1))  
# for i in range(n-1,0,-1):
#        print(" "*(n-i)+"*"*(2*i-1))
# print()

#9.i)Butterfly Pattern
# n=4
# for i in range(1,n+1):
#        print("*"*i+" "*(2*(n-i))+"*"*i)
# for i in range(n-1,0,-1):
    #    print("*"*i+" "*(2*(n-i))+"*"*i)

#ii)Butterfly Pattern
# n = 3   

# # Upper half
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print("  " * (n-i) * 2, end="")  
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # Lower half
# for i in range(n-1, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print("  " * (n-i) * 2, end="") 
#     for j in range(i):
#         print("*", end=" ")
#     print()

#10.Left-Aligned Half Diamond
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print("*"*i)

#11.Right-Aligned Half Diamond
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*i)

#Sandglass Star Pattern   
# n=int(input("enter a number:"))
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))
# for i in range(2,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))


#12.Sandglass Pattern
# n=int(input("enter a number:"))
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*i)
# for i in range(2,n+1):
#     print(" "*(n-i)+"*"*i)

#Practice
#square
#by using while loop
# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     print(" * "*n)
#     i+=1
#by using for loop
# n=int(input("enter a number:"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

#rectangle
# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     print(" * "*(n*2))
#     i+=1

#triangle 
# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     print(" * "*i)
#     i+=1
#inverted triangle 
# n=1
# i=5
# while i>=n:
#     print("*"*i)
#     i-=1

#right angled triangle(right aligned)    
# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     print(" "*(n-i)+"*"*i)
#     i+=1

#triangle pyramid
# n=5
# i=1
# while i<=n:
#     print(" "*(n-i)+"* "*i)
#     i+=1

#or
# n=5
# i=1
# while i<=n:
#     print(" "*(n-i)+"*"*(2*i-1))
#     i+=1

#inverted priramid
# n=5
# i=n
# while i>=1:
#     print(" "*(n-i)+"* "*i)
#     i-=1

#hallow square
# n=4
# for i in range(1,n+1):
#     if i==1:
#         print("* "*n)
#     if i==n:
#         print("* "*n)
#     else:
#         # print("* "+" "+" "+" "+" "+"* " )
#         print("* "+"  "*(n-2)+"* ")

#or
# n=4
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("* "*n)
#     else:
#         print("* "+" "+" "+" "+" "+"* " )
        # print("* "+"  "*(n-2)+"* ") #2spaces
  
#rectangle hallow rectangle      
n=4
for i in range(1,n+1):
    if i==1:
        print("* "*(2*n))
    if i==n:
        print("* "*(2*n))
    else:
        # print("* "+" "+" "+" "+" "+"* " )
        print("* "+"      "*(n-2)+"* ") #6spaces

