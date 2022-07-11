#!/usr/bin/env python
#Integrate this with Aaron's code - Devon 7/9/22

import inspect, math, subprocess

def encryptions_submenu():

    print('\nFetching encryptions from msfvenom framework.  Please wait...\n\n')

    probe = [encr.lstrip().split(" ")[0] for encr in subprocess.getoutput("msfvenom --list encrypt").split("\n")[6:-1]]
    encryptions_options = {str(item + 1): probe[item] for item in range(0, len(probe))}

    try:
        globals()["encryptions_value"] = encryptions_options[submenu_input(encryptions_options)]
    except KeyError:
        pass

def encodings_submenu():

    print('\nFetching encoders from msfvenom framework.  Please wait...\n\n')

    probe = [enco.lstrip().split(" ")[0] for enco in subprocess.getoutput("msfvenom --list encoders").split("\n")[6:-1]]
    encodings_options = {str(item + 1): probe[item] for item in range(0, len(probe))}

    try:
        globals()["encodings_value"] = encodings_options[submenu_input(encodings_options)]
    except KeyError:
        pass

#--------------------------------------------------

def architectures_submenu():
  try:
    globals()["architectures_value"] = architectures_options[submenu_input(architectures_options)]
  except KeyError:
    pass

#--------------------------------------------------

def payloads_submenu():
      
  payl_list = []
  three_sh = ['windows']
  two_sh = ['android', 'apple_ios', 'java', 'linux', 'osx', 'php', 'python', 'unix']
  generics = ['arista', 'brocade', 'cisco', 'freebsd', 'hardware', 'hpux', 'irix', 'javascript', 'juniper', 'mikrotik', 'netbsd', 'netware', 'openbsd', 'unify', 'unknown']
  # one_sh = ['aix', 'bsd', 'bsdi', 'firefox', 'mainframe', 'multi', 'netware', 'nodejs', 'r', 'ruby', 'solaris', 'generic']
      
##Shell Selection##
  for string in payloads_list:
    selection = string.split('/')

    if not platforms_value and not architectures_value:      
      payl = '/'.join(selection)
      if payl not in payl_list:
        payl_list.append(payl)
      payloads_options = {str(index+1):value for index, value in enumerate(payl_list)}

    elif not platforms_value and architectures_value :
      if architectures_value in selection or ('generic' in selection and 'cmd' not in selection):
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
      for string in payloads_list:
        selection = string.split('/')      
        
        if architectures_value:
          if platforms_value in selection and architectures_value in selection and 'cmd' not in selection or ('generic' in selection and 'cmd' not in selection):
              payl = '/'.join(selection)
              payl_list.append(payl)
          payloads_options = {str(index+1):value for index, value in enumerate(payl_list)} 

        else:
          if platforms_value in selection and 'cmd' not in selection or ('generic' in selection and 'cmd' not in selection):
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
    globals()["payloadsshell_value"] = payloads_options[submenu_input(payloads_options)]
  except KeyError:
    pass
  else:
    payloads2_submenu()                

#--------------------------------------------------

##Payload Selection##
def payloads2_submenu():

  payl_list = []

  if payloadsshell_value == 'Default':
    for string in payloads_list:
        selection = string.split('/')  
        
        if architectures_value:
          if platforms_value == 'windows' and architectures_value == 'x86':     
            if platforms_value in selection and 'x64' not in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection or ('generic' in selection and 'cmd' not in selection):
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
          
          elif platforms_value == 'windows' and architectures_value != 'x86': 
            if platforms_value in selection and architectures_value in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection or ('generic' in selection and 'cmd' not in selection):
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
          
          else:
            if platforms_value in selection and architectures_value in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection or ('generic' in selection and 'cmd' not in selection):
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

  elif payloadsshell_value == 'Meterpreter':
    
    for string in payloads_list:
      selection = string.split('/')

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

  elif payloadsshell_value == 'Powershell':
    for string in payloads_list:
      selection = string.split('/')

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

def platforms_submenu():
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
                           "3": "platforms",
                           "4": "encodings",
                           "5": "encryptions"}
  print("Importing architectures from msfvenom. Please wait...")
  probe = [arch.lstrip() for arch in subprocess.getoutput('msfvenom --list archs').split('\n')[6:-1]]
  globals()["architectures_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
  print("Complete.\nImporting payloads from msfvenom. Please wait...")  
  probe = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput("msfvenom --list payloads").split("\n")[6:-1]]
  globals()["payloads_list"] = probe
  globals()["payloadsshell_value"] = ""
  globals()["encodings_value"] = ""
  globals()["payloads_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
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
