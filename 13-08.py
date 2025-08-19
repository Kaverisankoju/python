#GLOBAL SCOPE
#LOCAL SCOPE
#enclosed
#built-in

#order is
#L
#E
#G
#B
#Topic->Local,Enclosed,Global,Built-in
#Here the below code display output as the priority of Order
# num1=10
# s1="hello python"
# def check_number():
#     num1=20
#     def number_check():
#         num1=30
#         print(num1) #Local
#     number_check()
#     print(num1) #Enclosed
# check_number()
# print(num1) #Global
# print(len(s1)) #built-in-function

#If Global and Local get the same output then
# str1='Python'
# def Same_values():
#     global str1;  
#     str1='Code'
#     print(str1)
# Same_values()
# print(str1)
# #if we want to change the global variable
# str1='Iam global-1'
# print("before changing the value of global:",str1)
# def change_global_value():
#     str1='Iam local'
#     globals()['str1']='iam global-2'
#     print(str1)
# change_global_value()
# print("after changing the value of global:",str1)
#Recursive function 
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# num = 5
# result = factorial(num)
# print(f"Factorial of {num} is {result}")


#14-08-2025
#nonlocal->
