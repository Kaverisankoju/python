#Conditional statements=>if

# n=int(input("enter a number"))
# if n%2==0:
#     print(n,'number is even')
    
# if n%2!=0:
#     print(n,'number is odd ')


# n=int(input("enter a number"))
# if n%1==0 and n%n==0:
#     print('prime number')
# if n%1==0 and n%n!=0:
#     print('not a prime')


# n=int(input("enter a number"))
# if n%7==0:
#     print(n,'is multiple of 7')
    
# if n%7!=0:
#     print(n,'not a multiple of 7 ')


# password='kaveri#123'
# if len(password)>=6:
#     print('strong password')
# if len(password)<4:
#     print('weak password')

#if-else=>

# n=int(input("enter a number"))
# if n%7==0:
#     print(n,'is multiple of 7')
    
# else:
#     print(n,'not a multiple of 7 ')



# password='kaveri#123'
# if len(password)>=6:
#     print('strong password')
# else:
#     print('weak password')


# num=int(input("enter a number:"))
# if num>0:
#     print(num,'positive number')
# else:
#     print(num,'negative number')
    
    
# num=int(input("enter a number:"))
# if num>0 :
#     print(num,'positive number')
# else:
#     if num==0:
#         print('zero')
# print(num,'negative number')


# num=int(input("enter a number:"))
# if num>0:
#     print(num,'positive number')
# if num==0:
#     print('zero')
# else:
#     print(num,'negative number')

         #or
         
# num=int(input("enter a number:"))
# if num>0:
#     print(num,'positive number')
# else:
#     if num==0:
#        print('zero')
#     else:
#         print(num,'negative number')


# n=int(input('enter a number:'))
# if n%2==0:
#     print(n,'is a even number')
# else:
#     print(n,'is an odd number')

# n=int(input('enter the year:'))
# if (n%4==0 and n%100!=0) or n%400==0:
#     print(n,'this year is a leap year')
# else:
#     print(n,'this is not a leap year ')

# num1=int(input('enter the 1st number'))
# num2=int(input('enter the 2nd number'))
# if num1>num2:
#     print(num1,'is greater then',num2)
# else:
#     print(num2,'is greater then',num1)


# age=int(input('enter the age:'))
# if age>=18:
#     print('Eligible to vote')
# else:
#     print('Not eligible')


# marks=int(input('enter the marks:'))
# if marks>=90:
#     print('Grade A')
# if marks<=89 and marks>=75:
#     print('Grade B')
# if marks<=74 and marks>=60:
#     print('Grade C')

# if marks<=59 and marks>=40:
#     print('Grade D')
# elif marks<40:
#      print('Fail')


# num1=int(input('enter the number:'))
# if num1>0:
#     if num1%2==0:
#         print(num1,'is even')
#     else:
#         print(num1,'is odd')
# else:
#     if num1==0:
#         print('zero')
#     else:
#         print('Negative number')


# num1=int(input('enter the 1st number:'))
# num2=int(input('enter the 2st number:'))
# operation=input('enter the operation(+,-,*,/):')

# if operation=='+':
#     print('addition of numbers is:',num1+num2)
# elif operation=='-':
#         print('substraction of numbers is:',num1-num2)

# elif operation=='*':
#         print('multiplication of numbers is:',num1*num2)
# elif operation=='/':
#     if num2!=0:
#         print('division of numbers is',num1/num2)
        
#     else:
#         print('can not divide by zero')



#using elif=>
# num1=int(input('enter a number:'))
# if num1>0:
#     print('positive')
# elif num1<-2:
#     print('negative')
# else:
#     if num1==-1:
#         print('it is a -1')
#     else:
#         print('zero')



#without using elif stmt=>

# num1=int(input('enter the number:'))
# if num1>0:
#     print('positive')
# else:
#     if num1==0:
#         print('zero')
#     else:
#        if num1==-1:
#            print('-1')
#        else:
#            print('negative')
           
           
 #by using multiple elif=>          
# num1=int(input('enter the number:'))
# if num1>0:
#     print('positive')
# elif num1==0:
#     print('zero')
# elif num1==-1:
#     print('-1')
# else:
#     print('negative')
    
    
#in elif if we want to perform specific condition(num1==0 etc) then so we write the first specific conditions
#then after generic (num1>0 etc)

# num1=int(input('enter the number:'))
# if num1==5:
#     print('5 star')
# elif num1==6:
#     print('six')
# elif num1>0:
#     print('positive')
# elif num1==-1:
#     print('it is -1')
# else:
#     if num1==0:
#      print('zero')
#     else:
#         print('negative')



#using by only elif=>
# marks=int(input('enter the Marks:'))
# if marks>90:
#     print('Grade A')
# elif marks>=75:
#     print('Grade B')
# elif marks>=60:
#     print('Grade C')
# elif marks>=40:
#     print('Grade D')
# else:
#     print('fail')

# current_units=float(input('enter the units:'))
# if current_units>=300:
#     bill=current_units*3
#     print(bill)
# else:
#     if current_units>=200:
#         bill=current_units*2
#         print(bill)
#     else:
#         if current_units>=100:
#             bill=current_units*1
#             print(bill)
#         else:
#               ('free current')
            
#try with 0 to 300
current_units=float(input('enter the units:'))
if current_units<=100:
    print(0)
else:
    if current_units<=200:
        print(current_units*1)
    else:
        if current_units<=300:
            print(current_units*2)
            
        else:
            if current_units<=400:
                print(current_units*3)
            else:
                print(current_units*4)