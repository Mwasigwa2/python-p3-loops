#!/usr/bin/env python3

#Question 1:
def happy_new_year(counter):
    counter = 10
    while counter >= 1:
     print ("Happy New Year!")
    counter -=1


#Question 2
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizzbuzz()
