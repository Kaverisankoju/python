# for class_no in range(1,11):
#     roll_no=1
#     while roll_no<31:
#         print('class',class_no,'roll,',roll_no)
#         roll_no+=1
        
# class_no=1
# while class_no<11:
#     roll_no=1
#     while roll_no<31:
#         print('class',class_no,'roll,',roll_no)
#         roll_no+=1
#     class_no+=1

#jump statements=>
# for i in range(1,31):
#     print(i * 2567)
#     break
    
# for i in range(0,31):
#     if i<i *(-1):
#         break
#     print(i**2)
    
# for i in range(0,31):
#     if i<i *(-1) or i%5==0:
#         break
#     print(i**2)
# for i in range(1,11):
#     if i==6:
#          continue
#     print(i)
   
   
# n=int(input('enter a number:'))
# if n%2==0:
#      print("Given number is even number")
# else:
#      print("Given number is Odd number  ")

# num1=int(input("enter 1st number:"))
# num2=int(input("enter 2nd number:"))
# num3=int(input("enter 3rd number:"))
# if num1>num2 and num1>num3:
#      print("num1 is greater number...")
# elif num1<num2 and num2>num3:
#      print("num2 is greater number....")
# elif num3>num1 and num3>num2:
#      print("num3 is greater number....")
# else:
#      print("three numbers are equal ....")

# num=int(input("enter a Number:"))
# if num>0:
#      print("Positive Number")
# else:
#      if num==0:
#           print("Zero")
#      else:
#           print("Negative Number")

# 
# n=int(input("enter a number:"))
# sum=0
# for i in range(1,n+1):
#      sum+=i
# print(f"the sum of first {n} natural numbers is {sum}")


# n=int(input("enter a number:"))
# even=[]
# for i in range(1,n+1):
#      if i%2==0:
#           even.append(i)
# print(f"the even numbers of first {n} natural numbers is {even}")

# num1=int(input("enter a number:"))
# print(f"\nMultiplication Table of {num1}:\n")
# for i in range(1,11):
#      print(f"{num1}x{i}={num1*i}")

# i=1
# count=0
# while i<=10:
#      print(i)
#      count+=1
#      i+=1
# print()
# print("count is",count)


# i = 1
# count = 0
# while i <= 10:
#     print(i)
#     count += i
#     i += 1

# print("Sum:", count)

# n=int(input("enter a number:"))
# sum=0
# while n>0:
#     digit=n%10
    
#     sum+=digit
#     n//=10
# print(sum)

# Original_password="Python@123"
# for i in range(3): 
    
#     password=input("enter your password:")

# if Original_password==password:
#     print("Login successfully...")
# else:
#      print("Account Locked..")


# for i in range(1,21):
#     if i==3:
#         continue
#     for j in range(1,11):
#         if j==3:
#             continue
#         print(f"{i}x{j}={i*j}")

# for i in range(100):
#   n=int(input("enter a number:"))
#   if n==0:
#       print('existing the program')
#       break
#   print("your number is",n)

# Break on input zero using for loop

# for _ in range(100):  # Arbitrary large range to keep the loop running
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         print("Zero entered. Exiting the program.")
#         break
#     print(f"You entered: {num}")

# Break on input zero

# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         print("Zero entered. Exiting the program.")
#         break
#     print(f"You entered: {num}")

# Count even and odd numbers in a list of 5 inputs

# even_count = 0
# odd_count = 0
# print("Enter 5 numbers:")
# for i in range(5):
#     num = int(input(f"Number {i+1}: "))
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"\nEven numbers count: {even_count}")
# print(f"Odd numbers count: {odd_count}")

# str1="Python"
# for i in str1:
#     print(i)

n=int(input("enter a number:"))
if n%2==0 and n%5==0:
    print(f"{n} is divisible by 2 and 5")
else:
    print(f"{n} is not divisible by 2 and 5")