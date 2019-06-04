from run import *

initial_response =input('Please press a number:\n'
                        '1. Input passenger to the system\n'
                        '2. List existing flight trips\n'
                        '3. Add an existing passenger to an existing flight trip\n'
                        '->  ')

if initial_response == 1:
    input_1 = input('You pressed 1. Input passenger to the system\n'
                    'Please enter passenger name')