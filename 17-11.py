# STACK AND QUEQUE
# PUSH,POP,PEEK(),SIZE,IS_Empty()
class Stack:
    def __init__(self):
        self.inner_list = []
        print("stack is created...")
    def push(self,ele):
        self.inner_list.append(ele)
    def size(self):
        return len(self.inner_list)
    def is_empty(self):
        return len(self.inner_list) == 0
    def peek(self):
        if self.is_empty():
            raise Exception('NO ELEMENTS IN THE STACK')
        return self.inner_list[len(self.inner_list)-1]
    def pop(self):
        if self.is_empty():
            raise Exception('NO ELEMENTS IN THE STACK')
        return self.inner_list.pop()
s1 = Stack()
print(s1.is_empty())
s1.push(1)
s1.push(2)
s1.push(3)

print(s1.is_empty())
print(s1.peek())
s1.push(4)
s1.push(5)
s1.push(6)
print(s1.size())
print(s1.pop())
print(s1.size())

# QUEUE
class Queue:
    def __init__(self):
        self.inner_l = []
        print("queue is created....")
    def push(self,ele):
        self.inner_l.append(ele)
    def is_empty(self):
        return len(self.inner_l) == 0
    def pop(self):
        if self.is_empty():
            raise Exception ('NO ELEMENTS IN THE QUEUE')
        return self.inner_l.pop(0)
    def peek(self):
        if self.is_empty():
            raise Exception('NO ELEMENTS IN THE QUEUE')
        return self.inner_l[0]
    def size(self):
        return len(self.inner_l)
Q1 = Queue()
print(Q1.is_empty())
Q1.push(10)
Q1.push(20)
Q1.push(30)
print(Q1.peek())
Q1.push(40)
print(Q1.size())
print(Q1.pop())
print(Q1.peek())
print(Q1.size())
print(Q1.is_empty())
    