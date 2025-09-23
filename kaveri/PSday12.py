#DOC-6
#sum of two numbers using function
# def add(a,b):
#    sum=a+b
#    print("sum of two numbers is:",sum)
# n=int(input('enter 1st number:'))
# m=int(input('enter 2nd number:'))
# add(n,m)
#check wheather even or odd 
# def check_even_odd(n):
#     if n%2==0:
#         print("even number:",n)
#     else:
#         print("odd number :",n)
# n=int(input('enter a number:'))
# check_even_odd(n)
#leap year 
# def check_year(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#         print(year,"is leap year")
#     else:
#         print(year,"is not a leap year")
# year=int(input('enter a year:'))
# check_year(year)
#print given number is prime or not
# def check_prime(n):
#     if n<2:
#         return 'not a prime'
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 return 'not a prime'
#             break
#         return f'{n} is prime'
# n=int(input('enter a number:'))
# print(check_prime(n))
#print all amstrong numbers from start to end numbers 
# def amstrong_numbers(n,m):
#     for i in range(n,m+1):
#         temp=i
#         length_num=len(str(i))
#         sum_val=0
#         while temp>0:
#             digit=temp%10
#             sum_val+=digit**length_num
#             temp//=10
#         if sum_val==i:
#             print(i,end=" ")
            

# n=int(input('enter first number:'))
# m=int(input('enter last number:'))
# amstrong_numbers(n,m)
#factorial of number using recursion 
# def factorial_num(n):
#     if n==0 or n==1:
#         return 1
#     else:
#             return n*factorial_num(n-1)
# n=int(input('enter a number:'))
# print("factorial of number is:",factorial_num(n))
#fibonacci series using recursion
# def fibonacci_num(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci_num(n-1)+fibonacci_num(n-2)
# def fibonacci_series(n):
#     for i in range(n):
#         print(fibonacci_num(i),end=" ")
# n=int(input('enter a number:'))
# fibonacci_series(n)
#without recursion function
# n=int(input('enter a number:'))
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b
#sum of digits using recursion
# def sum_of_digits(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sum_of_digits(n//10)
    
# n=int(input('enter a number:'))
# print("sum of the digits",sum_of_digits(n))
#reverse of a number using recursion
# def reverse_of_num(n,rev=0):
#     if n==0:
#         return rev
    
#     else:
#        return reverse_of_num(n//10,rev*10+n%10)
# n=123
# print("reversed numbers is :",reverse_of_num(n))
#check palindrome using recursion
def reverse_of_num(n,rev=0):
    if n==0:
        return rev
    
    else:
       return reverse_of_num(n//10,rev*10+n%10)
n=121
if n==reverse_of_num(n):

    print("palindrome numbers is :",reverse_of_num(n))
else:
    print("not a palindrome")

  