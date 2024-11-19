def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

first_number = get_number('Enter first number: ')
second_number = get_number('Enter second number: ')

def calculation():    
    operation=input('Enter the operation for the calculation(+,-,*,/):')
    if operation=='+':
        result=first_number+second_number
        print(first_number,'+',second_number,'=',result)
    elif operation=='-':
        result=first_number-second_number
        print(first_number,'-',second_number,'=',result)
    elif operation=='*':
        result=first_number*second_number
        print(first_number,'*',second_number,'=',result)
    elif operation=='/':
        if second_number==0:
            print('Error!Division by zero is not allowed')
        else:
            result=first_number/second_number
            print(first_number,'/',second_number,'=',result)
    else:
        print('invlaid input!')
calculation()
        

