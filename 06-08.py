# def triangle_check(a,b,c):
#     if a+b>c and b+c>a and c+a>b :
#         if a==b==c:
#             return 'equalitral triangle'
#         elif a==b!=c or b==c!=a or c==a!=b:
#             return 'isolated triangle '
#         elif a!=b!=c or b!=c!=a or c!=a!=b:
#             return 'scaling triangle'
#     else:
#         return 'invalid triangle'
# def triangle_angle_check(a,b,c):
#     if a+b>c and b+c>a and c+a>b:
#         if (a**2+b**2==c**2) or (b**2+c**2==a**2) or (a**2+c**2==b**2):
#             return 'right-angled triangle'
#         elif (a**2+b**2>c**2) or (b**2+c**2>a**2) or (c**2+a**2>b**2):
#             return 'Acute-angled'
#         elif (a**2+b**2<c**2) or (b**2+c**2<a**2) or (c**2+a**2<b**2):
#             return 'Obuse-angled '
#     else:
#         return 'no angle type(invalid triangle)'
# side1=int(input("enter 1st side of triangle:"))
# side2=int(input("enter 2st side of triangle:"))
# side3=int(input("enter 3st side of triangle:"))
# print("your given input sides are:",side1,side2,side3,)
# print(triangle_check(side1,side2,side3))
# print(triangle_angle_check(side1,side2,side3))

# arr=[20,22,36,121,303]
# for num in arr:
#     new_num=num+1
#     if new_num>1:
#         for i in range(2,int(new_num*0.5)+1):
#             if new_num%i==0:
#                 break
#         else:
#             print(num,end=' ')

# def numbers_from_1_to_100():
#     for i in range(1,101):
#         print(i,end=" ")
# numbers_from_1_to_100()

# def sum_of_numbers(num):
#     sum=0
#     for i in range(1,num+1):
#         sum+=i
#     print("sum of numbers",sum)
# sum_of_numbers(30)

# def even_numbers(limit):
#     even=[]
#     num=1
#     while num<=limit:
#         if num%2==0:
#             even.append(num)
#         num+=1
#     print("even numbers are:",even)
# even_numbers(50)

# def multiplication_of_a_number(num):
#     for i in range(1,21):
#         print(num*i, end=" ")
# multiplication_of_a_number(3)

# def reverse_and_sum_of_number(num):
#     sum=0
#     rev=0
#     temp=num
#     while temp>0:
        
#         digit=temp%10
#         sum+=digit
#         rev=rev*10+digit
#         temp//=10
#     print("sum of the number is:",sum)
#     print("reverse of number is:",rev)
# # reverse_and_sum_of_number(234)

# def count_number_of_digits(num):
#     count=0
#     while num>0:
        
#         count+=1
#         num//=10
#     print("number of digits in a number:",count)
# count_number_of_digits(345)

# def ask_number_until_negative():
#     while 'True':
#         num=int(input("enter a number:"))
#         if num<0:
#             print("u r entered negative number so stopped")
#             break
#         else:
#             print("you entered number:",num)
# ask_number_until_negative()

# start=1
# while start<=100:
#     if start%2==0:
#         print(start)
#     start+=1

# n=56
# for i in range(1,n+1):
#     pass
# print((n*(n+1))/2)

# n=56
# while n>=1:
#     print((n*(n+1))/2)
#     n-=1

# n = 56
# while n >= 1:
#     print((n * (n + 1)) / 2)
#     break


    
# n=1
# sum=0
# while n<=56:
#     sum+=n
#     n+=1
# print(sum)

# while 'True':
#     n=int(input("enter a number:"))
#     if n<0:
#         print("u r enterder negative number, stopped..")
#         break
#     else:
#         print(f"your number is :{n}")

# n=1
# while n>0:
#     n=int(input("enter a number:"))
#     if n<0:
#         print("u r enterder negative number, stopped..")
#         break
#     else:
#         print(f"your number is :{n}")
        
# num=int(input("enter a number:"))

# while num>0:
#     num=int(input("enter a number"))
#     if num<=0:
#         print("negative number entered so it is ended...")

# input_operator=input("enter a operation(+,-,*,/):")
# while 'True':
#     if input_operator not in ['+', '-', '*', '/']:
#         print("Invalid operation. Exiting the program.")
#         break
#     print("your operator is",input_operator)
#     n1=int(input("enter 1st number:"))
#     n2=int(input("enter 2nd number:"))
    
#     if input_operator=='+':
#         print("addition of two numbers is :",n1+n2)
#         input_operator=input("enter a operation(+,-,*,/):")
#     elif input_operator=='-':
#         print("subtraction of two numbers is:",n1-n2)
#         input_operator=input("enter a operation(+,-,*,/):")
#     elif input_operator=='*':
#         print("multiplication of two numbers is:",n1*n2)
#         input_operator=input("enter a operation(+,-,*,/):")
#     elif input_operator=='/':
#         if n2!=0:
#             print("division of two numbers is:",n1/n2)
#         else:
#             print("zero can not divided")
#             input_operator=input("enter a operation(+,-,*,/):")
       
    
# import math
# def find_factorial_position(arr,num):
#     factorial=math.factorial(num)
#     if factorial in arr:
#         position=arr.index(factorial)+1
#         print(f"The factorial of {num} is {factorial} at the index {position}")
#     else:
#         print(f"The factorial of {num} not present")
# find_factorial_position([120,625,780,654,10],5)   
    