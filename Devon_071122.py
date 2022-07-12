#!/usr/bin/env python
#Revision 7/11/2022 - Devon's alternate payload method

import inspect, math, re, subprocess

#--------------------------------------------------

def architectures_submenu():

  try:
    globals()["architectures_options"] = architectures_options
  except NameError:
    print("Importing architectures from msfvenom. Please wait...")
    probe = [arch.lstrip() for arch in subprocess.getoutput('msfvenom --list archs').split('\n')[6:-1]]
    globals()["architectures_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
    print("Complete.")

  try:
    globals()["architectures_value"] = architectures_options[submenu_input(architectures_options)]
  except KeyError:
    pass

#--------------------------------------------------

def payloads_submenu():
  
  try:
    globals()["payloads_options"] = payloads_options
  except NameError:
    print("\nImporting payloads from msfvenom. Please wait...")  
    probe = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput("msfvenom --list payloads").split("\n")[6:-1]]
    globals()["payloads_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
    print("Complete.")

  limited_payloads = []

  if platforms_value:                             #only do this if the platform has been selected

    for option in payloads_options.values():      #iterate through all payload options

      if platforms_value in option:               #return a list of all payloads containing the currently selected platform
        limited_payloads.append(option)

    default = []
    meterpreter = []
    powershell = []
    shell_options = []
  
    for option in limited_payloads:

      if "meterpreter" not in option and "powershell" not in option:
        default.append(option)
      else:

        if "meterpreter" in option:
          meterpreter.append(option)

        if "powershell" in option:
          powershell.append(option)

    if len(limited_payloads):
      shell_options.append("Default")

    if len(meterpreter):
      shell_options.append("Meterpreter")

    if len(powershell):
      shell_options.append("PowerShell")

    default_dict = {str(item + 1): default[item] for item in range(0, len(default))}

    meterpreter_dict = {str(item + 1): meterpreter[item] for item in range(0, len(meterpreter))}

    powershell_dict = {str(item + 1): powershell[item] for item in range(0, len(powershell))}

    shell_dict = {}

    for number in range(len(shell_options)):
      shell_dict[str(number + 1)] = shell_options[number]

    next_dict = shell_dict[submenu_input(shell_dict)].lower() + "_dict"

    try:
      globals()["payloads_value"] = eval(next_dict)[submenu_input(eval(next_dict))]
    except KeyError:
      pass

  else:

    try:
      globals()["payloads_value"] = payloads_options[submenu_input(payloads_options)]
    except KeyError:
      pass

#--------------------------------------------------

def platforms_submenu():

  try:
    globals()["platforms_options"] = platforms_options
  except NameError:
    print("\nImporting platforms from msfvenom. Please wait...")  
    probe = [plat.lstrip() for plat in subprocess.getoutput("msfvenom --list platforms").split("\n")[6:-1]]
    globals()["platforms_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
    print("Complete.")

  try:
    globals()["platforms_value"] = platforms_options[submenu_input(platforms_options)]
  except KeyError:
    pass

#--------------------------------------------------

def submenu_input(options):
  selection = ""
  number_of_options = len(options)
  options_per_page = 36
  number_of_pages = math.ceil(number_of_options / options_per_page)
  current_page = 1
  
  while selection != "r":
    start = (current_page - 1) * options_per_page + 1
    end = min(current_page * options_per_page, number_of_options)
    submenu_display(options, start, end)
    selection = input("\nmsfAntidote: " + inspect.stack()[1][3].split("_")[0].capitalize() + " menu (page " + str(current_page) + " of " + str(number_of_pages) + ")> ").lower()
    
    if selection in options.keys():
      return(selection)
    elif selection == "p":
      
      if current_page > 1:
        current_page -= 1
      else:
        print("\nYou have reached the first page.")
    
    elif selection == "n":
      
      if current_page < number_of_pages:
        current_page += 1
      else:
        print("\nYou have reached the last page.")
    
    elif selection != "r":
      print(invalid)

#--------------------------------------------------

def submenu_display(options, start, end):
  options_line = ""
  print(header)
  
  for option in range(start, end + 1):

    options_line += "[" + str(option).rjust(3) + "] " + options[str(option)].ljust(51)
    if not option % 3 or option == end:
      print(options_line)
      options_line = ""

  print(footer)

#--------------------------------------------------

def clear_selections():
  for submenu in submenus.values():
    globals()[submenu + "_value"] = ""

#--------------------------------------------------

def generate_payload():
  if payloads_value:
    file_name = input("Enter a file name: ")
    print("Generating payload. Please wait...")
    print(subprocess.getoutput("msfvenom -p " + payloads_value + " --platform " + platforms_value + " -a " + architectures_value + " -o " + file_name))
    clear_selections()
  else:
    print("\nNo payload specified. Please select a payload.")
  
#--------------------------------------------------

def main():
  globals()["border"] = "-" * 170
  globals()["header"] = "\n" + border + "\nmsfAntidote v1.0 2022 Aaron Picard and Devon Meier\n" + border
  globals()["footer"] = border + "\n[R]eturn to the main menu, [N]ext page or [P]revious page.\n" + border
  globals()["invalid"] = "\nInvalid selection. Please try again."
  globals()["submenus"] = {"1": "architectures",
                           "2": "payloads",
                           "3": "platforms"}
  #print("Importing architectures from msfvenom. Please wait...")
  #probe = [arch.lstrip() for arch in subprocess.getoutput('msfvenom --list archs').split('\n')[6:-1]]
  #globals()["architectures_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
  #print("Complete.\nImporting payloads from msfvenom. Please wait...")  
  #probe = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput("msfvenom --list payloads").split("\n")[6:-1]]
  #globals()["payloads_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
  #print("Complete.\nImporting platforms from msfvenom. Please wait...")  
  #probe = [plat.lstrip() for plat in subprocess.getoutput("msfvenom --list platforms").split("\n")[6:-1]]
  #globals()["platforms_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
  #print("Complete.")
  clear_selections()
  selection = ""
  
  while selection != "q":
    options_line, selections_line = "", ""
    print(header)
  
    for key, value in submenus.items():
      options_line += "[" + key.rjust(3) + "] " + value.capitalize().ljust(51)
      selections_line += " " * 6 + globals()[value + "_value"].ljust(51)
      key = int(key)
    
      if not key % 3 or key == len(submenus):
        print(options_line + "\n\u001b[31m" + selections_line + "\u001b[00m")
        options_line, selections_line = "", ""
  
    print(border + "\n" + "[C]lear selections, [G]enerate payload, [N]ext page, [P]revious page or [Q]uit." + "\n" + border)
    selection = input("\nmsfAntidote: Main menu (page 1 of 1)> ").lower()
    
    if selection in submenus.keys():
      eval(submenus[selection] + "_submenu()")
    elif selection == "c":
      clear_selections()
      print("\nSelections cleared.")
    elif selection == "g":
      generate_payload()
    elif selection != "q":
      print(invalid)

#--------------------------------------------------

if __name__ == "__main__":
  main()
