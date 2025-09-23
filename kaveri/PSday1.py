#DOC-2
#Check even or Odd
n=int(input('enter a number:'))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")


def check_even(n):
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
n1=int(input('enter a number:'))
check_even(n1)

#Divisible by 5 but Not by 10
n=int(input('enter a number:'))
if n%5==0 and n%10!=0:
    print('satisfy')
else:
    print('not satisfy')

#Biggest Among Two Numbers
n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
if n1>n2:
    print('Biggest is',n1)
else:
    print('Biggest is',n2)

#Smallest Among Two Numbers
n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
if n1<n2:
    print('Smallest is',n1)
else:
    print('Smallest is',n2)

#Divisible by 2, 3, and 6
n1=int(input('enter 1st number:'))
if n1%2==0 and n1%3==0 and n1%6==0:
    print('number =',n1)
    print('Satisfy')
else:
    print('not satisfy')

#Voting Eligibility
age=int(input('enter age:'))
if age>=18:
    print('Age =',age)
    print('Eligible to vote')
else:
    print('Not eligible')

#Student Pass/Fail Based on All Subjects >= 35
maths=int(input('enter maths marks:'))
Physics=int(input('enter physics marks:'))
chemistry=int(input('enter chemistry marks:'))
if maths>=35 or Physics>=35 or chemistry>=35:
    print('maths =',maths)
    print('physics =',Physics)
    print('chemistry =',chemistry)
    print('pass')
else:
    print('fail')

#Student Pass if Passed Any Two Subjects
maths=int(input('enter maths marks:'))
Physics=int(input('enter physics marks:'))
chemistry=int(input('enter chemistry marks:'))
if (maths>=35 and Physics>=35 or chemistry>=35) or (maths>=35 or Physics>=35 and chemistry>=35) or (maths>=35 and chemistry>=35 or Physics>=35):
    print('maths =',maths)
    print('physics =',Physics)
    print('chemistry =',chemistry)
    print('pass')
else:
    print('fail')

#Biggest Among Three Numbers
n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
n3=int(input('enter 3rd number:'))
if n1>n2 and n1>n3:
    print('Biggest is',n1)
elif n2>n3:
    print('Biggest is',n2)
else:
    print('Biggest is',n3)

#Smallest Among Three Numbers    
n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
n3=int(input('enter 3rd number:'))
if n1<n2 and n1<n3:
    print('Smallest is',n1)
elif n2<n3:
    print('Smallest is',n2)
else:
    print('Smallest is',n3)
    
# Perfect Square or Not
n=int(input('enter a number:'))
m=n**0.5
if n==(m*m):
    print('perfect square')
else:
    print('not a perfect square')

n=int(input('enter a number:'))
if n%(n**0.5)==0:
    print('perfect square')
else:
    print('not a perfect square')

#Cars Required for Members (Max 5 per car)
n1=int(input('enter a members:'))
if n1%5==0:
   print(n1//5)
else:
    print(n1//5+1)

#Second Biggest Among Three Numbers
n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
n3=int(input('enter 3rd number:'))
nums=[n1,n2,n3]
sort_nums=nums.sort()
print(nums[-2])

#Leap Year or Not
n1=int(input('enter a year:'))
if n1%4==0 and n1%100!=0 or n1%400==0:
    print(n1,'is leap year')
else:
    print(n1,'not a leap year')

#DOC-1
#AREA OF SQUARE    
# n=int(input('enter one side:'))
# Area=n*n
# print("Area of square is:",Area)
# #AREA OF RECTANGLE
# l=int(input('enter l of rectangle:'))
# b=int(input('enter b of rectangle:'))
# Area=l*b
# print("Area of square is:",Area)
# #AREA OF TRIANGLE
# base=float(input('enter base of triangle:'))
# height=float(input('enter height of triangle:'))
# Area=1/2*base*height
# print("Area of square is:",Area)
# #AREA OF PERIMETER
# n=int(input('enter one side:'))
# perimeter=4*n
# print("perimeter of square is:",perimeter)
# #PERIMETER OF RECTANGLE
# l=int(input('enter l of rectangle:'))
# b=int(input('enter b of rectangle:'))
# perimeter=2*(l+b)
# print("perimeter of square is:",perimeter)
# #PERIMETER OF TRIANGLE
# n=int(input('enter a side of triangle:'))
# perimeter=n+n+n
# print("perimeter of triangle:",perimeter)
# #BREAK AMOUNT INTO 1000s, 500s, and REMAINING CHANGE
# amount=int(input("enter amount:"))
# thousands=amount//1000
# amount=amount%1000
# five_hundreds=amount//500
# amount=amount%500
# remaining=amount
# print('1000s:',thousands)
# print('500s:',five_hundreds)
# print('remaining:',remaining)
# #CONVERT SECONDS INTO HOURS, MINUTES, AND SECONDS
# sec=int(input('enter the number of seconds:'))
# hours=sec//3600
# sec=sec%3600
# min=sec//60
# sec=sec%60
# seconds=sec
# print('Hours:',hours)
# print('min:',min)
# print('seconds:',seconds)
# #SUM OF MARKS (MATHS, PHYSICS, CHEMISTRY)   
# math=int(input('enter math marks:'))
# phy=int(input('enter phy marks:'))
# che=int(input('enter che marks:'))
# sum=math+phy+che
# print('total marks:',sum)
# #AVERAGE OF MARKS (MATHS, PHYSICS, CHEMISTRY)
# math=int(input('enter math marks:'))
# phy=int(input('enter phy marks:'))
# che=int(input('enter che marks:'))
# sum=math+phy+che
# avg=sum/3
# print('total marks:',avg)









