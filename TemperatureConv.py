import random 
from colorama import Fore

red = Fore.RED
black = Fore.BLACK
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE

def tempertureconverter(user_input):
     FAHRRENHIGHT_TO_CELCIUS = (user_input - 32) * 5/9
     if(user_input >=90):
          print("Fahrenheit:  ", red, user_input, black)
          print("Celcius:  ", red, "{0:4.1f}".format(FAHRRENHIGHT_TO_CELCIUS), black)
     elif(user_input >= 75) & (user_input <=89):
          print("Fahrenheit:  ", yellow, user_input, black)
          print("Celcius:  ", yellow, "{0:4.1f}".format(FAHRRENHIGHT_TO_CELCIUS), black)
     elif(user_input >= 64) & (user_input <=74):
          print("Fahrenheit:  ", green, user_input, black)
          print("Celcius:  ", green, "{0:4.1f}".format(FAHRRENHIGHT_TO_CELCIUS), black)
     else:
          print("Fahrenheit:  ", blue, user_input, black)
          print("Celcius:  ", blue, "{0:4.1f}".format(FAHRRENHIGHT_TO_CELCIUS), black)

user=int(input ("Enter tempeture to convert to Celcius: ") )

for x in range(5):
     tempertureconverter(user)
     user=int(input ("Enter a tempeture in Fahrenheit to convert to Celcius: ") )
