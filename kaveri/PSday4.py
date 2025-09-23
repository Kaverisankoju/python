#solid square 
# n=int(input('enter a number:'))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# m=3
# n=5
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

# n=int(input('enter a number:'))
# for i in range(n):
#     for j in range(i,n):
#         for k in range(i,j+1):
#            print(chr(97+k),end=" ")
#         print()
#     print()



# s='my name is python'
# s1=s[::-1]
# print(s1)
   
s = "my name is python"

# Step 1: Find positions of spaces
spaces = []
for i in range(len(s)):
    if s[i] == " ":
        spaces.append(i)

# Step 2: Reverse the string without spaces
rev = ""
for i in range(len(s)-1, -1, -1):
    if s[i] != " ":
        rev += s[i]

# Step 3: Rebuild string with spaces at same positions
result = ""
j = 0
for i in range(len(s)):
    if i in spaces:
        result += " "
    else:
        result += rev[j]
        j += 1

print(result)





