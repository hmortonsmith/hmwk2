from run import *

initial_response =input('Please press a number:\n'
                        '1. Input passenger to the system\n'
                        '2. List existing flight trips\n'
                        '3. Add an existing passenger to an existing flight trip\n'
                        'Or type cancel to exit\n'
                        '->  ')

if initial_response == 1:
    input_1 = input('You pressed 1. Input passenger to the system\n'
                    'Please enter passenger name, or type cancel to return to previous screen\n'
                    '-->  ')

    input_2 = input("Please enter the passenger's passport number\n"
                    "-->  ")

    input_3 = input("Please enter the passenger's nationality\n"
                    "-->  ")

elif initial_response == 2:
    print()

