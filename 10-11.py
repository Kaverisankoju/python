# try except else finally;
try:
    a = int(input('enter a number1:'))
    b = int(input('enter a number2:'))
    print(a/b)
except ZeroDivisionError as e:
    print(e)
    print('can not divide...')
except ValueError as e:
    print(e)
    print('give proper value...')
except Exception as e:
    print(e)
    print('check the code once again...')
else:
    print('GREAT JOB....,It is successufull....!')
finally:
    print('Finished.....')


# try and except is mandatory... but else and finally these are may have or not no problem at all...



# nested try and exceptions 

# 1

try:
    a = int(input('enter a number1:'))
    b = int(input('enter a number2:'))
    try:
        result = a/b
        print('result is:',result)
    except ZeroDivisionError as e:
        print(e)
        print('can not divide')
    
except ValueError as e:
    print(e)
    print('check the code once again...')
else:
    print('GREAT JOB....,It is successufull....!')
finally:
    print('Finished.....')

# 2
try:
    numbers = [10, 20, 30]
    index = int(input("Enter index number: "))

    try:
        print("Value =", numbers[index])
    
    except IndexError:
        print("Error: Index out of range!")

except ValueError:
    print("Error: Invalid index! Please enter numbers only.")

    