#import time
def fizz(number):
    if number % 3 == 0 and number % 5 !=0:
        print('fizz')
# if the number is divisible by 3 and NOT divisible by 5, then the function prints fizz.
# anything else, and nothing is returned

def buzz(number):
    if number % 5 ==0 and number % 3 !=0:
        print('buzz')
# if the number is divisible by 5 and NOT divisible by 3, then the function prints buzz.
# anything else, and nothing is returned

def fizzbuzz(number):
    if number % 15 ==0:
        print('FIZZBUZZ!')
# if the number is divisible by 15, then the function prints fizzbuzz.
# anything else, and nothing is returned

def othernumber(number):
    if number % 3 != 0 and number % 5 != 0:
        print(number)
# if the number is NOT divisible by 3 and NOT divisible by 5, then the function prints the number.
# anything else, and nothing is returned

int = 1
while int <= 100:
    fizzbuzz(int)
    buzz(int)
    fizz(int)
    othernumber(int)
    int += 1
#    time.sleep(1)