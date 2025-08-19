# def day_of_week(day):
#     return 'Sunday' if day==1 else 'Monday' if day==2 else 'Tuesday' if day==3 else 'wednesday' if day==4 else 'Thursday' if day==5 else 'friday' if day==6  else 'saturday' if day==7\
# day_no=int(input("enter a number:"))
# print(day_of_week(day_no))


# def day_of_week(day):
#     return 'Sunday' if day == 1 else \
#            'Monday' if day == 2 else \
#            'Tuesday' if day == 3 else \
#            'Wednesday' if day == 4 else \
#            'Thursday' if day == 5 else \
#            'Friday' if day == 6 else \
#            'Saturday' if day == 7 else \
#            'Invalid day'

# day_no = int(input("Enter a number: "))
# print(day_of_week(day_no))



# def name_of_the_month(month):
#     return 'january' if month == 1 else \
#            'february' if month == 2 else \
#            'march' if month == 3 else \
#            'april' if month== 4 else \
#            'may' if month == 5 else \
#            'june' if month == 6 else \
#            'july' if month== 7 else \
#             'August' if month==8 else\
#             'sepembar' if month==9 else\
#             'October' if month==10 else\
#             'november'if month==11 else\
#             'december' if month==12 else\
#            'Invalid day'

# month_no = int(input("Enter a number: "))
# print(name_of_the_month(month_no))



# def greatest_of_three_numbers(a,b,c):
#     return   'a is greater' if a>b and a>c else \
#              'b is greater' if b>c and b>a else\
#              'c is greter' if c>a and c>b else\
#              'three numbers are same'
# num1=int(input("enter 1st number:"))
# num2=int(input("enter 2nd number:"))
# num3=int(input("enter 3rd number:"))
# print(greatest_of_three_numbers(num1,num2,num3))

# def leap_year_check(year):
#     return f"{year} is a leap year" if (year%4==0) and (year%100!=0) or year%400==0 else \
#            f"{year} is not a leap year"
# year_value=int(input("enter a year:"))
# print(leap_year_check(year_value))


# def char_check_vowel_or_not(chr):
#     vowels='aeiouAEIOU'
#     return f"{chr} is vowel" if chr in vowels else\
#            f"{chr} is a consonat" if chr not in vowels else\
#             'invalid character'
# char=input("enter a charcter:")
# print(char_check_vowel_or_not(char)) 

# def triangle_check(a,b,c):
#     if (a+b>c) and (b+c>a) and (c+a>b): # or=>angle1+angle2+angle3=180
#         print('correct triangle')
#     else:
#         print('not a triangle')
# triangle_check(3,6,4)                                             


# def  grade_check(marks):
#     return 'Grade A ' if marks>=90 and marks==100 else\
#            'Grade B'  if marks>=80 and marks<=89 else\
#             'Grade C' if marks>=70 and marks<=79 else\
#             'Fail' if marks<70 else\
#                 'result not found'
# marks_input=int(input("enter the marks:"))
# print(grade_check(marks_input))

#isolated
#equalater triangle
#pythagoras 


def char_check_vowel_or_not(chr):
    if len(char)!=1:
        return 'invalid input'
    #if char in ['A','E','I','O','U']:
    if char in 'AEIOU':
        return 'vowel'
    else:
        return 'consonant'
           
char=input("enter a charcter:")
print(char_check_vowel_or_not(char)) 


