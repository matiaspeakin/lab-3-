# divide function 

def divide(x,y):
    print(x/y)


# add function

def add(x,y):
    print(x+y)


    
# multiple funcion
def multiple(x,y):
    print(x*y)

#subtrucation 
def subtract(x,y):
    print(x-y)

def get_number(prompt):
    number = int(input(prompt))
    if number == 67:
        print("boi I will slime you out")
    return number

print ("welcome to the calc short for calulator")
while (True):
    print ("what we doin")
    print("Type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")
    user_choice = input(": ")
    #print(user_choice)

    if user_choice == 'a':
        x = get_number("enter first number : ")
        y = get_number("enter second number : ")
        add(x,y)
    elif user_choice == 's':
        x = get_number("enter first number : ")
        y = get_number("enter second number : ")
        subtract (x,y)

    elif user_choice == 'm':
        x = get_number("enter first number : ")
        y = get_number("enter second number : ")
        multiple (x,y)

    elif user_choice == 'd':
        x = get_number("enter first number : ")
        y = get_number("enter second number : ")
        divide (x,y)
    elif user_choice == 'q':
        break 
 
