#!/usr/bin/env python

selection = "0"                               #variable declaration
print("splash page code")

while selection != "q":                       #loop until input is Q/q
  print("main menu code")                     #print main menu
  selection = input("msfAntidote: ").lower()  #accept input from user and make lower case
   
  try:                                        #int() will throw an error if input is of type string or float

    if int(selection) - 1 in range(21):       #integer in range
      print("submenu code")
    else:                                     #integer out of range
      print("invalid selection")
      
  except:                                     #string or float error handling

    if selection == "c":                      #handle C/c condition
      print("clear selections code")
    elif selection == "g":                    #handle G/g condition
      print("generate payload code")
    elif selection != "q":                    #handle all non-Q/q, non-integer conditions
      print("invalid selection")
