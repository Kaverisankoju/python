# #LAMBDA FUNCTIONS=>anonymous one line functions in python are called
# #Only has one expression in their function body
# #return is not explicitive 
# def square(a):
#     return a**2
# print(square(6))
# #Lambda function
# #No arguments
# lam1=lambda:'Good Morning'
# print(lam1())
# print()
# #With one argument
# lam2=lambda x:x**2
# print(lam2(6))
# print()
# #with two arguments
# lam3=lambda x,y:x+y
# print(lam3(3,3))
# print()
# #In-built higher order functions=>map,filter
# #map syntax=>map(function,iterable)
# def square(x):
#     return x**2
# def cube(x):
#     return x**3
# def qudratic(x):
#     return x**4
# print(list(map(square,[1,2,3,4,5,6])))
# print(list(map(cube,[1,2,3,4,5,6])))
# print(list(map(qudratic,[1,2,3,4,5,6])))
# print()
# #filter syntax=>filter(function,iterable)
# def even(x):
#     return x%2==0
# def odd(x):
#     return x%2!=0
# def mulple_of_5(x):
#     return x%5==0
# print(list(filter(even,[60,67,98,34,23,67,53,99,90,5,10,25,36,75])))
# print(list(filter(odd,[60,67,98,34,23,67,53,99,90,5,10,25,36,75])))
# print(list(filter(mulple_of_5,[60,67,98,34,23,99,90,5,10,25,30])))
# print()
# #to remove dependency we simply use lambda function for map and filter
# #lambda function for map
# print(list(map(lambda x:x**2,[1,2,3,4,5,6])))
# print(list(map(lambda x:x**3,[1,2,3,4,5,6])))
# print(list(map(lambda x:x**4,[1,2,3,4,5,6])))
# print()
# #lambda function for filter
# print(list(filter(lambda a:a%2==0,[60,67,98,34,23,67,53,99,90,5,10,36])))
# print(list(filter(lambda a:a%2!=0,[60,67,98,34,23,67,53,99,90,5,10,25,36,75])))
# print(list(filter(lambda a:a%5==0,[60,67,98,34,23,99,90,5,10,25,30])))

#Reduce
from functools import reduce
print(reduce(lambda a,b: a if a>b else b,[8,20,60,89,34,56]))
print(reduce(lambda a,b: a if a<b else b,[8,20,60,89,34,56]))

#high order in-built function
#REDUCE syntax=>reduce(function,iteration)
from functools import reduce
#mathematical operations 
print(reduce(lambda a,b:a+b,[3,6,8,98,56,34]))
print(reduce(lambda a,b:a-b,[3,6,8,98,56,-34,-100,-200]))
print(reduce(lambda a,b:a*b,[3,6,8]))
print(reduce(lambda a,b:a/b,[3,6,2,3,1,6]))
print()
#max,min values
print(reduce(lambda a,b:a if a>b else b,[3,6,8,98,56,34]))
print(reduce(lambda a,b:a if a<b else b,[3,6,8,98,56,34]))
print()
#concatenation
print(reduce(lambda a,b:a+" "+b,["python","is","user","friendly"]))
print()
#logical operations
#And operator
list=[2,4,6,8,0]
print(reduce(lambda a,b:a and b, [i%2==0 for i in list]))
list=[2,4,6,8,3]
print(reduce(lambda a,b:a and b, [i%2==0 for i in list]))
#or operator
list=[15,1,3,7,5,9]
print(reduce(lambda a,b:a or b, [i%2!=0 for i in list]))
list=[2,4,6,8,0,9]
print(reduce(lambda a,b:a or b, [i%2==0 for i in list]))
list=[15,1,3,7,5,9]
print(reduce(lambda a,b:a or b, [i%2==0 for i in list]))



