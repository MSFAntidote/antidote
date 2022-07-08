#!/usr/bin/env python

import inspect, subprocess

#--------------------------------------------------

def architectures_submenu():
  try:
    globals()["architectures_value"] = architectures_options[submenu_input(architectures_options)]
  except KeyError:
    pass

#--------------------------------------------------

def payloads_submenu():
  try:
    globals()["payloads_value"] = payloads_options[submenu_input(payloads_options)]
  except KeyError:
    pass

#--------------------------------------------------

def platforms_submenu():
  try:
    globals()["platforms_value"] = platforms_options[submenu_input(platforms_options)]
  except KeyError:
    pass

#--------------------------------------------------

def submenu_input(options):
  selection = ""

  while selection != "r":
    submenu_display(options)
    selection = input("\nmsfAntidote (" + inspect.stack()[1][3].split("_")[0] + "): ").lower()
    
    if selection in options.keys():
      return(selection)
    elif selection != "r":
      print(invalid)

#--------------------------------------------------

def submenu_display(options):
  options_line = ""
  
  print(header)
  
  for key, value in options.items():
    options_line += "[" + key.rjust(3) + "] " + value.ljust(51)

    key = int(key)
    
    if not key % 3 or key == len(options):
      print(options_line)
      options_line = ""
  
  print(footer)

#--------------------------------------------------

def clear_selections():
  for submenu in submenus.values():
    globals()[submenu + "_value"] = ""

#--------------------------------------------------

def generate_payload():
  file_name = input("Enter a file name: ")
  print("Generating payload. Please wait...")
  print(subprocess.getoutput("msfvenom -p " + payloads_value + " --platform " + platforms_value + " -a " + architectures_value + " -o " + file_name))
  clear_selections()
  
#--------------------------------------------------

def main():
  globals()["border"] = "-" * 170
  globals()["header"] = "\n" + border + "\nmsfAntidote v1.0 2022 Aaron Picard and Devon Meier\n" + border
  globals()["footer"] = border + "\n[R]eturn the main menu.\n" + border
  globals()["invalid"] = "\nInvalid selection. Please try again."
  globals()["submenus"] = {"1": "architectures",
                           "2": "payloads",
                           "3": "platforms"}
  print("Importing architectures from msfvenom. Please wait...")
  probe = [arch.lstrip() for arch in subprocess.getoutput('msfvenom --list archs').split('\n')[6:-1]]
  globals()["architectures_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
  print("Complete.\nImporting payloads from msfvenom. Please wait...")  
  probe = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput("msfvenom --list payloads").split("\n")[6:-1]]
  globals()["payloads_options"] = {str(item + 1): probe[item] for item in range(0, 36)}
  print("Complete.\nImporting platforms from msfvenom. Please wait...")  
  probe = [plat.lstrip() for plat in subprocess.getoutput("msfvenom --list platforms").split("\n")[6:-1]]
  globals()["platforms_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
  print("Complete.")
  clear_selections()
  selection = ""
  
  while selection != "q":
    options_line, selections_line = "", ""
    print(header)
  
    for key, value in submenus.items():
      options_line += "[" + key.rjust(3) + "] " + value.ljust(51)
      selections_line += " " * 6 + globals()[value + "_value"].ljust(51)
    
      key = int(key)
    
      if not key % 3 or key == len(submenus):
        print(options_line + "\n\u001b[31m" + selections_line + "\u001b[00m")
        options_line, selections_line = "", ""
  
    print(border + "\n" + "[C]lear selections, [G]enerate payload or [Q]uit." + "\n" + border)
    selection = input("\nmsfAntidote (main): ").lower()
    
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
