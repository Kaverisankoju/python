#addig two maximum numbers in the given three variables
# #method-1
# a,b,c = 55,2,98
# if (a > b or a > c) and (b > c):
#     print(a+b)
# elif (c > a or c > b) and  (b > a):
#     print(b+c)
# else:
#     print(c+a)
    
# #method-2
# a,b,c=5,25,50
# if a > b and a > c:
#     if b > c: 
#         print(a + b)
#     else:
#         print(a + c)
# elif b > c and b > a:
#     if a > c:
#         print(a+b)
#     else:
#         print(b+c)
# else:
#     if a > b:
#         print(c+a)
#     else:
#         print(c+b)

#matrix rotation
m = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    for j in range(len(m)-1,-1,-1):
        print(m[i][i],end=" ")
    print()