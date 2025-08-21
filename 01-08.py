#FUNCTIONS=>
# def name_of_student(): # FUNCTION DEFINE
#     print("hello ravi")
#     print("welcome to python")#FUNCTION BODY
# name_of_student()
# print("how are you")
# name_of_student() #FUNCTION CALL
# name_of_student()

# def area_of_circle(r):
#     print("area of circle")
#     print(3.14*r*r)
# area_of_circle(20)
# area_of_circle(10)
# area_of_circle(30)

# def simple_calculator(a,b):
#     print("the sum of values are:")
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     if b!=0:
#         print(a/b)
#         print(a%b)
#         print(a//b)
#     else:
#         print("it is not divisible b")
    
# simple_calculator(10,20)
# simple_calculator(6,0)
# simple_calculator(0,3)
# simple_calculator(11,13)


# def table_of_a_number(a):
#     print("the given value table is:")
#     for i in range(1,21):
#        print(a,"x",i ,"=", a*i)
      
# table_of_a_number(2)
# table_of_a_number(25)

# def sum_of_n_numbers(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     print("sum of first 4 numbers:")
#     print(sum)
# sum_of_n_numbers(4)


# def factorial_number(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(f"factorial of number {n} is {fact}")
#     print(fact)
# factorial_number(4)
    
    
# def factorial_number(n):
#     count=0
#     for i in range(1,n+1):
#         count+=1
#     print(f"count of {n} is {count}")
#     print(count)
# factorial_number(10)


# def char_count(word):
#     count=0
#     for i in range(1,word+1):
#         count+=1
#     print(f"count of {word} is {count}")
#     print(count)
# char_count()
    
# marks=int(input("enter the marks:"))
# if marks>=95:
#     print(marks,"Grade O")
# elif marks>=75:
#     print(marks,"Grade A")
# elif marks>=65:
#     print(marks,"Grade B")
# elif marks>=45:
#     print(marks,"Grade C")
# else:
#     print("fail")

# n=float(input("enter a int value:"))
# print(n)

# x="5"
# y=2
# print(x * y)

# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(a,b)

# i=10
# print(i>5)
# print(i>20)

# n1=10
# n2=20
# print(n1&n2)
# print(n1|n2)
# print(n1^n2)
# print(~10)
# print(~-11)
# print(5<<1)
# print(5>>1)


# def check_numbers(num1=10,num2=6):
#     if num1==num2:
#         print("num1 and num2 are equal numbers")

#     elif num1!=num2:
#         print("num1 and num2 are different values")
#     else:
#         print("invalid number")
# check_numbers()


# def check_numbers(num1,num2=6):
#     if num1==num2:
#         print("num1 and num2 are equal numbers")

#     elif num1!=num2:
#         print("num1 and num2 are different values")
#     else:
#         print("invalid number")
# check_numbers(10)


# def check_numbers(num1,num2):
#     if num1==num2:
#         print("num1 and num2 are equal numbers")

#     elif num1!=num2:
#         print("num1 and num2 are different values")
#     else:
#         print("invalid number")
# check_numbers(num2=10,num1=10)

# def sum_numbers(a,b):
#     print("sum of two numbers:")
#     print(a+b)
# def sum_numbers(a,b,c):
#     print("sum of three numbers")
#     print(a+b+c)
# def sum_numbers(a,b,c,d):
#     print("sum of four numbers:")
#     print(a+b+c+d)
# sum_numbers(20,8)
# sum_numbers(6,7,9)
# sum_numbers(10,20,8,9)

#arbitary arguments 
# def sum(a,*b):
#     temp=a
#     for i in b:
#         temp=temp+i 
#     print(temp)
# sum(2,3)
# sum(2)
# sum(3,4,5,6,7,9)
# sum(8,9,0)   


# def sum_of_numbers(a,b):
   
#     print(f"sum of the number{a} and {b} is",a+b)  
# sum_of_numbers(10,20)                                              

# def squre_of_number(a):
#     print(f"squre of the {a} is",a*a)
# squre_of_number(6)

# def check_even_odd(k):
#     if k%2==0:
#         print(f"{k} is even number")
#     else:
#         print(f"{k} is odd number")
# check_even_odd(3)

# def factorial_num(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(f"factorial of {n} is ",fact)
# factorial_num(6)


# def Max_num(a,b,c):
#     if a>b and a>c:
#         print(f"{a} is maximum number")
#     elif b>c and b>a:
#         print(f"{b} is maximum number")
#     else:
#         print(f"{c} is maximum number")
# Max_num(6,2,10)

# def max_num(a,b,c):
#     maximum_number=max(a,b,c)
#     print("The maximum number is",maximum_number)
# max_num(30,90,10)

# def count_vowel_word(word):
#     vowels="aeiouAEIOU"
#     count=0
#     for ch in word:
#         if ch in vowels:
#             count+=1
#     print("count of vowels",count)
# count_vowel_word("hello python")

# def sum_of_list(list):
#     sum=0
#     for i in list:
#         sum+=i
#     print("The sum of the list items is",sum)
# sum_of_list([1,2,3,9,70,44,39])

# def reverse_of_string(str):
#     for i in range(len(str)-1,-1,-1):
#         print(str[i],end="")
# reverse_of_string("python") layman term

# 
# def string_reverse(str):
#     reversedstr=str[::-1]
#     print("reversed string is",reversedstr)
# string_reverse("python")

# def string_reverse(str):
#     reversedstr=str[::-1]
#     if str==reversedstr:
#         print(str," is a palindrome")
#         print("reversed string is",reversedstr)
#     else:
#         print("it is not a palindrome",str)
        
# string_reverse("madam")

# def even_list(list):
#     for i in list:
#         if i%2==0:
#             print(i,end=",")
        
# even_list([7,8,9,0,4,3,2])

# def area_of_circle(r):
#     area=3.14*r*r
#     print("area of circle is:",area)
# area_of_circle(5)

# def len_of_string(str):
#     count=0
#     for i in str:
#         count+=1
#     print("length of string is:",count)
# len_of_string("python")

def avg_numbers(*args):
    total=0
    for num in args:
        total+=num
    if len(args)==0:
        print("no numbers are provided")
    else:
        avg=total/len(args)
    print("average of args is:",avg)
avg_numbers(10,50,30)


# def avg_numbers(*args):
#     total = 0
#     for num in args:
#         total += num  # Correct: add the number, not just 1
#     if len(args) == 0:
#         print("No numbers provided.")
#     else:
#         avg = total / len(args)
#         print("Average of args is:", avg)

# # Example usage
# avg_numbers(10, 20, 30)  # Output: Average of args is: 20.0
