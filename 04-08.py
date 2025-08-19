# def connect_to_db(*args):
#     print(args)
#     for i in args:
#         print(i)
# connect_to_db("db_loc:localhost:1008","password:1234","db_port:8790")


# def connect_to_db2(**kargs):
#       return kargs
# result=connect_to_db2(db_loc="localhost:1008",password="1234",db_port="8790")
# print(result["password"])
# print(result['db_loc'])


# def even_or_odd(num):
#     if num%2==0:
#         return 'even'
#     else:
#         return 'odd'
    
# result=even_or_odd(9)
# print(result)
# print(result+' '+'number')  #here we can reuse



# def even_or_odd(num):
#     if num%2==0:
#         return 'even'
#     else:
#         return 'odd'
    
# print(even_or_odd(9)+' '+"number") #here no reuse

# #return can accept multiple operations or tasks
# def simple_arth(a,b):
#     return a+b,a-b,a*b  #this can output like in tuple way 
# r2=simple_arth(3,6)
# print(r2)
# print(type(r2))
 
# #return statement once executed is the end of function
# def sum(num1,num2):
#     return num1+num2
#     print('hello')  #it is not executed