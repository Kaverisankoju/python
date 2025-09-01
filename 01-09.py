#OOPS=>
class Calculator:
    def add(self,a,b):
        print('addition',a+b)
    def sub(self,a,b):
        print('substraction',a-b)
    def mul(self,a,b):
        print('multiplication',a*b)
    def div(self,a,b):
        if b!=0:
          print('division',a/b)
        else:
            print('division is not possible')
    def module(self,a,b):
        if b!=0:
            print('module',a%b)
        else:
            print('module operation not done by zero')
    def display(self):
        print("model number",self.model_num)
        print("model In",self.made_in)
        print("color",self.color)
        print("discount",self.discount)
        
c1=Calculator()
c2=Calculator()

print("\n---All arthemetic operations of calculater 1---")
c1.add(6,3)
c1.sub(6,3)
c1.mul(6,3)
c1.div(6,3)

print("\n---All arthemetic operations of calculater 2---")
c2.add(30,40)
c2.sub(30,35)
c2.mul(50,34)
c2.div(20,40)


c1.model_num='electronic'
c1.made_in='india'
c1.color='black'
c1.discount='20%'

c2.model_num='scientific'
c2.made_in='china'
c2.color='blue'
c2.discount='30%'
print("\n--- Calculator 1 Details ---")
c1.display()
print("\n--- Calculator 2 Details ---")
c2.display()


