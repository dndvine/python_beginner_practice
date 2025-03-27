

# This execise can be found on www.practicepython.org
# We are to creat a program that asks the user to enter their
# name, their age, and than it should print out a message
# that tell them the year that they will turn 100 year old.
import datetime  # this brings in python's buil-in module to work with dates and times

# this will promote user to enter their name.
name = input("What is your name? ")
# this will promote user to enter their age
age = int(input("What is your age? "))
# this is declaring the current time and year and asking to just provide the year
current_year = datetime.datetime.now().year
# this calculate the year and their age. to determine what year they will turn 100 years old
year = current_year - age + 100
print(f'Hello {name}, you will be 100 years old in {year}')
