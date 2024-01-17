print('Enter 1 to continue \nEnter 0 to quite')

while True:
    n=int(input('Enter the choice:-'))  

    if n==1:
        height = float(input('Enter height in meters:- '))
        weight = float(input('Enter weight in kilograms:- '))

        bmi = round(weight/(height**2),2)


        if bmi<18.5:
            print(f'your BMI is: {bmi} and you are Underweight')

        elif bmi>=18.5 and bmi<=24.9:
            print(f'your BMI is: {bmi} and you are Normalweight')

        elif bmi>=25.0 and bmi<=29.9:
            print(f'your BMI is: {bmi} and you are Overweight')

        else:
            print(f'your BMI is: {bmi} and you are Obesity')
    elif n==0:
        print('Exiting program')
        break
    else:
        print('Invalid input try again')

