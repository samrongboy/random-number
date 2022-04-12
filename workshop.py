# #It is important  to use function when there are many tasks
# #variable declaratoin
# #
# #function to multiply
# #function to divide
# #variable decaration
# number1=0
# number2=0
# result =new_num = 0
# operator = input('select the operator: ')
# #initiaizing values for variables

# #validate number1
# #function to check number1
# test = True
# try:
#     number1 = int(input('put yor first number'))
# except:
#         while test == True:
#             print('it must be a number')
#             test = False

# #validate number2

# #validate operator
# def operation(op):
#     try:
#         if operator == '+':
#             result = number1+number2 
#             print('{} + {} = '.format(number1,number2),result)
#         elif operator == '-':
#             result = number1-number2
#             print('{} - {} = '.format(number1,number2),result)
#         elif operator == '*':
#             result = number1*number2
#             print('{} * {} = '.format(number1,number2),result)
#         elif operator == '/':
#             result = number1/number2
#             print('{} / {} = '.format(number1,number2),result)    
#     except:
#             print('something wrong')



# #calculate
# #def calculator=(n1,n2)

import sys

result = 0
num_1 = 0
num_2 = 0
new_num = 0

def Num1 ():
    global num_1
    try:
        num_1 = float(input('Put your first number : '))

    except ValueError :
        print('you must enter a number!!')
        Num1()

def Num2():
    global num_2
    try:
        num_2 = float(input('Put your second number : '))
    except ValueError :
            print('you must enter a number!!')
            Num2 ()

def NewNum ():
    global new_num
    try:
        new_num = float(input('Put new number that your want to calculates : '))
    
    except ValueError :
            print('you must enter a number!!')
            NewNum ()
 
def Oprt():
    global result
    operation = input("Select operator '+' , '-' , '*' , '/' : ")
    if (operation == '+' or operation == '-' or operation == '*' or operation == '/'):
        if operation == '+':
            if result <= 0 :
                print('{} + {} '.format(num_1, num_2),'= ', "{:.2f}".format(num_1 + num_2))
                result = num_1 + num_2
            else :
                print('{} + {} '.format(result, new_num),'= ', "{:.2f}".format(result + new_num))
                result = result + new_num
            
        elif operation == '-':
            if result <= 0 :
                print('{} -{} '.format(num_1, num_2),'= ', "{:.2f}".format(num_1 - num_2))
                result = num_1 - num_2
            else :
                print('{} - {} '.format(result, new_num),'= ', "{:.2f}".format(result - new_num))
                result = result - new_num

        elif operation == '*':
            if result <= 0 :
                print('{} * {} '.format(num_1, num_2),'= ', "{:.2f}".format(num_1 * num_2))
                result = num_1 * num_2
            else :
                print('{} * {} '.format(result, num_2),'= ', "{:.2f}".format(result * new_num))
                result = result * new_num
        elif operation == '/':
            if result <= 0 :
                print('{} / {} '.format(num_1, num_2),'= ', "{:.2f}".format(num_1 / num_2))
                result = num_1 / num_2
            else :
                print('{} / {} '.format(result, num_2),'= ', "{:.2f}".format(result / new_num))
                result = result / new_num
    else :
        print ("Invalid operator. Try again!!")
        Oprt ()

def ClearResulat ():
    global result
    global num_1
    global num_2
    global new_num
    result = 0
    num_1 = 0
    num_2 = 0
    new_num = 0
    print (result)
    Calculation ()

def Calculation ():
    Num1 ()
    Num2 ()
    Oprt ()
    AddCal ()

def ContinueCal ():
    NewNum ()
    Oprt ()
    AddCal ()

def AddCal ():
    add = input ("""Add more oparator 'Y' 
Stop this program 'N'
Clear result 'cls' : """)
    
    if add.upper() == 'Y':
        ContinueCal ()
    elif add == "cls" :
        ClearResulat ()
    elif add.upper() == 'N' :
        sys.exit("You're welcome,see you again")
    else :
        AddCal ()

Calculation ()



