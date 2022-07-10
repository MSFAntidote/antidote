#!/usr/bin/env python3

from colorsys import ONE_SIXTH
import os, subprocess, re

#Color Variables

black = '\u001b[30m'
red = '\u001b[31m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
cyan = '\u001b[36m'
normal = '\u001b[37m'
normal = '\u001b[00m'

black_b = '\u001b[40m'
red_b = '\u001b[41m'
green_b = '\u001b[42m'
yellow_b = '\u001b[43m'
blue_b = '\u001b[44m'
magenta_b = '\u001b[45m'
cyan_b = '\u001b[46m'
white_b = '\u001b[47m'

##temporary platform function for testing##
def platforms_submenu():
  # plat_input = input("\nenter platform:  \n\n")
  # platforms_value = plat_input
  platforms_value = 'windows'
  return platforms_value

def architectures_submenu():
  architectures_value = 'x64'
  return architectures_value

## start of payloads selection##
def payloads_submenu():

  print('\nFetching framework payloads from msfvenom.  Please wait...\n\n')

  payload_list = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput('msfvenom --list payloads').split('\n')[6:-1]]
      
##retrieve variables from platform functions##
  platforms_value = platforms_submenu()
  architectures_value = architectures_submenu()
  payl_list = []
  three_sh = ['windows']
  two_sh = ['android', 'apple_ios', 'java', 'linux', 'osx', 'php', 'python', 'unix']
  generics = ['arista', 'brocade', 'cisco', 'freebsd', 'hardware', 'hpux', 'irix', 'javascript', 'juniper', 'mikrotik', 'netbsd', 'netware', 'openbsd', 'unify', 'unknown']
  # one_sh = ['aix', 'bsd', 'bsdi', 'firefox', 'mainframe', 'multi', 'netware', 'nodejs', 'r', 'ruby', 'solaris', 'generic']
      
##Shell Selection##
  for string in payload_list:
    selection = re.split(r'[/_]', string)

    if not platforms_value and not architectures_value:      
      payl = '/'.join(selection)
      if payl not in payl_list:
        payl_list.append(payl)
      payloads_options = {str(index+1):value for index, value in enumerate(payl_list)}

    elif not platforms_value and architectures_value:
      if architectures_value in selection:
        payl = '/'.join(selection)
        payl_list.append(payl)
      payloads_options = {str(index+1):value for index, value in enumerate(payl_list)}

    elif platforms_value in three_sh:
      payloads_options = {"1": "Default",
                          "2": "Meterpreter", 
                          "3": "Powershell"}

    elif platforms_value in two_sh:
      payloads_options = {"1": "Default",
                          "2": "Meterpreter"}

    else: 
      for string in payload_list:
        selection = re.split(r'[/_]', string)      
        
        if architectures_value:
          if platforms_value in selection and architectures_value in selection and 'cmd' not in selection:
              payl = '/'.join(selection)
              payl_list.append(payl)
          payloads_options = {str(index+1):value for index, value in enumerate(payl_list)} 

        else:
          if platforms_value in selection and 'cmd' not in selection:
              payl = '/'.join(selection)
              payl_list.append(payl)
          payloads_options = {str(index+1):value for index, value in enumerate(payl_list)} 

          if platforms_value in generics:
              if 'generic' in selection and 'cmd' not in selection:
                payl = '/'.join(selection)
                payl_list.append(payl)
              payloads_options = {str(index+1):value for index, value in enumerate(payl_list)}   


      try:
        globals()["payloads_value"] = payloads_options[submenu_input(payloads_options)]
        return
      except KeyError:
        pass

  try:
    globals()["payloads_value_shell"] = payloads_options[submenu_input(payloads_options)]
  except KeyError:
    pass
  finally:
    payloads_submenu_2()                

#--------------------------------------------------

##Payload Selection##
def payloads_submenu_2():

  payload_list = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput('msfvenom --list payloads').split('\n')[6:-1]]
  platforms_value = platforms_submenu()
  architectures_value = architectures_submenu()
  payl_list = []

  if payloads_value_shell == 'Default':
    for string in payload_list:
        selection = re.split(r'[/_]', string)  
        
        if architectures_value:
          if platforms_value == 'windows' and architectures_value == 'x86':     
            if platforms_value in selection and 'x64' not in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection:
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
          
          elif platforms_value == 'windows' and architectures_value != 'x86': 
            if platforms_value in selection and architectures_value in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection:
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
          
          else:
            if platforms_value in selection and architectures_value in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection:
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
        
        else:
          if platforms_value == 'python':
            if platforms_value in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection and 'cmd' not in selection:
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}  
          
          else:
            if platforms_value in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection:
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}

  elif payloads_value_shell == 'Meterpreter':
    
    for string in payload_list:
      selection = re.split(r'[/_]', string)

      if architectures_value:
        if platforms_value == 'windows' and architectures_value == 'x86':
          if platforms_value in selection and 'x64' not in selection and 'meterpreter' in selection and 'powershell' not in selection:
            payl = '/'.join(selection)
            payl_list.append(payl)
          payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
        
        elif platforms_value == 'windows' and architectures_value != 'x86':
          if platforms_value in selection and architectures_value in selection and 'meterpreter' in selection and 'powershell' not in selection:
            payl = '/'.join(selection)
            payl_list.append(payl)
          payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
        
        else:
          if platforms_value in selection and architectures_value in selection and 'meterpreter' in selection and 'powershell' not in selection:
            payl = '/'.join(selection)
            payl_list.append(payl)
          payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}

      elif platforms_value == 'python':        
        if (platforms_value in selection and 'meterpreter' in selection) and 'powershell' not in selection and 'cmd' not in selection:
          payl = '/'.join(selection)
          payl_list.append(payl)
        payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}

      else:             
        if (platforms_value in selection and 'meterpreter' in selection) and 'powershell' not in selection:
          payl = '/'.join(selection)
          payl_list.append(payl)
        payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}

  elif payloads_value_shell == 'Powershell':
    for string in payload_list:
      selection = re.split(r'[/_]', string)

      if architectures_value:        
        if architectures_value == 'x86':
          if platforms_value in selection and 'x64' not in selection and 'patchupmeterpreter' not in selection and 'powershell' in selection:
            payl = '/'.join(selection)
            payl_list.append(payl)
          payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}

        elif architectures_value != 'x86':
          if platforms_value in selection and architectures_value in selection and 'powershell' in selection:
            payl = '/'.join(selection)
            payl_list.append(payl)
          payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}

      else:
        if platforms_value in selection and 'powershell' in selection:
          payl = '/'.join(selection)
          payl_list.append(payl)
        payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)} 

  try:
    globals()["payloads_value"] = payloads_options_2[submenu_input(payloads_options_2)]
  except KeyError:
    pass
  
#--------------------------------------------------

# def architectures_submenu():
#   architectures_options = {"1": "fake_architectures_option_1",
#                            "2": "fake_architectures_option_2",
#                            "3": "fake_architectures_option_3",
#                            "4": "fake_architectures_option_4"}
  
#   try:
#     globals()["architectures_value"] = architectures_options[submenu_input(architectures_options)]
#   except KeyError:
#     pass

#--------------------------------------------------

def encoders_submenu():
  payloads_options_2 = {"1": "fake_encoders_option_1",
                      "2": "fake_encoders_option_2",
                      "3": "fake_encoders_option_3",
                      "4": "fake_encoders_option_4"}
  
  try:
    globals()["encoders_value"] = payloads_options_2[submenu_input(payloads_options_2)]
  except KeyError:
    pass



#--------------------------------------------------

# def platforms_submenu():
#   platforms_options = {"1": "fake_platforms_option_1",
#                        "2": "fake_platforms_option_2",
#                        "3": "fake_platforms_option_3",
#                        "4": "fake_platforms_option_4"}
  
#   try:
#     globals()["platforms_value"] = platforms_options[submenu_input(platforms_options)]
#   except KeyError:
#     pass

#--------------------------------------------------

def submenu_input(options):
  selection = ""

  while selection != "b":
    submenu_display(options)
    selection = input("\nmsfAntidote: ").lower()
    
    if selection in options.keys():
      return(selection)
    elif selection != "b":
      print(invalid)

#--------------------------------------------------

def submenu_display(options):
  options_line = ""
  
  print(header)
  
  for key, value in options.items():
    options_line += "[" + key.rjust(2) + "] " + value.ljust(41)

    key = int(key)
    
    if not key % 3 or key == len(options):
      print(options_line)
      options_line = ""
  
  print(footer)

#--------------------------------------------------

def main():
  submenus = {"1": "architectures",
              "2": "encoders",
              "3": "payloads",
              "4": "platforms"}
  globals()["border"] = "-" * 137
  globals()["header"] = "\n" + border + "\nmsfAntidote v1.0 2022 Aaron Picard and Devon Meier\n" + border
  globals()["footer"] = border + "\n<footer goes here>\n" + border
  globals()["invalid"] = "\nInvalid selection. Please try again."
  
  for variable in submenus.values():
    globals()[variable + "_value"] = ""

  selection = ""
  
  while selection != "q":
    options_line, selections_line = "", ""
    print(header)
  
    for key, value in submenus.items():
      options_line += "[" + key.rjust(2) + "] " + value.ljust(41)
      selections_line += " " * 5 + globals()[value + "_value"].ljust(41)
    
      key = int(key)
    
      if not key % 3 or key == len(submenus):
        print(options_line + "\n\u001b[31m" + selections_line + "\u001b[00m")
        options_line, selections_line = "", ""
  
    print(border + "\n" + "<footer goes here>" + "\n" + border)
    selection = input("\nmsfAntidote (main): ").lower()
    
    if selection in submenus.keys():
      eval(submenus[selection] + "_submenu()")
    elif selection != "q":
      print(invalid)

#--------------------------------------------------

  ### DUNDER CHECK ###
if __name__ == "__main__":
  main()
