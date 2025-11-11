
# Range BY USING ITERATORS

class RangeIterator():
    def __init__(self,limit):
        self.curr_val = 5
        self.limit = limit 
    def __iter__(self):
        return self
    def __next__(self):
        if self.curr_val > self.limit:
            raise StopIteration
        temp = self.curr_val
        self.curr_val += 1
        return temp
e1 = RangeIterator(12)
print(next(e1))    
print(next(e1))    
print(next(e1))    
print(next(e1))    
print(next(e1))    
print(next(e1))    
print(next(e1))    
print(next(e1))    
print(next(e1))  

# print Infinite even numbers using iterators
class EvenIterator():
    def __init__(self):
        self.curr_val = 0
    def __iter__(self):
        return self
    def __next__(self):
        temp = self.curr_val
        self.curr_val += 2
        return temp
e2 = EvenIterator()
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))

# print even numbers with limit using iterator
class EvenIterator():
    def __init__(self,limit):
        self.curr_val = 0
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.curr_val > self.limit:
            raise StopIteration
        temp = self.curr_val
        self.curr_val += 2
        return temp
e2 = EvenIterator(20)
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))

# print factorial of numbers using iterators
class FactorialIterator():
    def __init__(self):
        self.num1 = 1
        self.fact = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.fact = self.num1 * self.fact
        self.num1 += 1
        return self.fact
        
e3 = FactorialIterator()
print(next(e3))
print(next(e3))
print(next(e3))
print(next(e3))
print(next(e3))
print(next(e3))

# print Infinite even numbers with generator
def gen3():
    num1 = 0
    while True:
        temp = num1
        num1 += 2
        yield temp
var3 = gen3()
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))

# print limit even numbers using generator
def gen3(limit):
    
    num1 = 0
    while (num1 < limit):
        temp = num1
        num1 += 2
        yield temp
var3 = gen3(10)
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))
print(next(var3))


# Range BY USING GENERATORS
def gen1(limit):
    num1 =  1
    while(num1<limit):
        temp = num1
        num1 += 1
        yield temp
var1 = gen1(10)
print(next(var1)) 
print(next(var1)) 
print(next(var1)) 
print(next(var1)) 
print(next(var1)) 
print(next(var1)) 
print(next(var1)) 
print(next(var1)) 
print(next(var1)) 
 
#Infinite Fibonacci series
def gen2():
    num1= 0
    num2 = 1
    while True:
        temp = num1
        num1,num2 =num2, num1 + num2
        yield temp
var2 = gen2()
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))

# Infinate factorial by using generator
def gen4():
    num1 = 1
    fact =  1
    while True:
        fact = fact * num1
        yield fact
        num1 += 1
var4 = gen4()
print(next(var4))
print(next(var4))
print(next(var4))
print(next(var4))
print(next(var4))
print(next(var4))


# print factorial with limit using generators
def gen4(limit):
    num1 = 1
    fact =  1
    while num1 < limit:
        fact = fact * num1
        yield fact
        num1 += 1
var4 = gen4(6)
print(next(var4))
print(next(var4))
print(next(var4))
print(next(var4))
print(next(var4))
