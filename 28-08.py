n=input("enter a roman number:")
dict1={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}
print(dict1.get(n))


#DICTIONARY built-in functions        
        
dict={'name':'kaveri','age':21}
print(dict)

dict={'name':'kaveri','age':21}
dict.update({'city':'hyderabad','country':'hyd'})
print(dict)

dict={'name':'kaveri','age':21}
print(dict.get('age','name')) #only it give one value


dict={'name':'kaveri','age':21}
print(dict.keys())


dict={'name':'kaveri','age':21}
print(dict.values())

dict={'name':'kaveri','age':21}
print(dict.items())


dict={'name':'kaveri','age':21}
print(dict.pop('age'))
print(dict)

dict={'name':'kaveri','age':21}
print(dict.popitem())
print(dict)

dict={'name':'kaveri','age':21}
print(dict.setdefault('gender','F'))
print(dict)

dict={'name':'kaveri','age':21}
copy_dict=dict.copy()
print(dict)
print(copy_dict)
    
    
