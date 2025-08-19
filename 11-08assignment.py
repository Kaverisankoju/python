# def check_reverse_and_palindrome(s):
#     num=int(s)
#     original=num
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num//=10
#     print(rev)
#     if original==rev:
#         print("Lucky ticket and it is a palindrome number")    
#     else:
#         print("Not a lucky , it is not a palindrome number")
# check_reverse_and_palindrome('1234')
# check_reverse_and_palindrome('121')


# def sum_of_square_numbers(n):
#     total=0
#     for i in range(1,n+1):
#         total+=i**2
#     print("The sum of digits:",total)
# n1=int(input("enter a number:"))
# sum_of_square_numbers(n1)

    
# def secret_number(secret):
  
#      while True:
#         guess=int(input("enter a number:"))
#         if guess==secret:
#             print("Treasure Found!")
#             break
#         else:
#             print("Try again!")
# secret_number(30)

# def perfect_squares():
#     perfect_square=[]
#     for i in range(1,501):
#         if int(i**0.5)**2==i:
#            perfect_square.append(i)
       
#     print(perfect_square)
# perfect_squares()    

# def cubes_of_number(n):
#     for i in range(1,n+1):
#         cube=i**3
#         print(cube)
# cubes_of_number(5)

#PRIME NUMBER
        