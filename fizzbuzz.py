def fizz(number):
    if number % 3 == 0 and number % 15 !=0:
        print('fizz')
# if the number is divisible by 3 and NOT divisible by 15, then the function prints fizz.
# anything else, and nothing is returned

def buzz(number):
    if number % 5 ==0 and number % 15 !=0:
        print('buzz')


def fizzbuzz(number):
    if number % 15 ==0:
        print('FIZZBUZZ!')


def othernumber(number):
    if number % 3 != 0 and number % 5 != 0:
        print(number)


int = 1
while int <= 100:
    fizzbuzz(int)
    buzz(int)
    fizz(int)
    othernumber(int)
    int += 1