f = open("12-11.py","r")
print(f.read())    #it reads total file and gives output as string

f = open("12-11.py","r")
print(f.read(5))  #it reads 5 characters 
print(f.tell())   #it tells the present character number
print(f.readline())  #reads single line from cursor starts
print(f.readlines())  #reads multiple lines from cursor starts
print(f.tell())    

print(f.seek(0))     # starts from starting of file 
print(f.read(5))

f = open("12-11.py","w")    
print(f.write("hello"))   #remove all previous content and writes the characters from starting of file

f = open("9-11.py","a")
print(f.write("\nworld"))

