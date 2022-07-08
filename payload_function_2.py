import os, subprocess, re

##temporary platform function for testing##
def platforms_submenu():
    platforms_value = 'windows'
    return platforms_value

##Temporary architecture function for testing##
def architectures_submenu():
    architectures_value = 'x64'
    return architectures_value
    

##Get output from msfvenom --list payloads##
def payloads_submenu():

    platforms_value = platforms_submenu()
    architectures_value = architectures_submenu()
    if platforms_value is False:
        platforms_submenu()

    print('\nFetching framework payloads from msfvenom.  Please wait...\n\n')

    payload_list = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput('msfvenom --list payloads').split('\n')[6:-1]]
    
    
    payl_list = []
    for string in payload_list:
        selection = re.split(r'[/_]', string)
        
        if platforms_value in selection:
            payl = '/'.join(selection)
            payl_list.append(payl)
        payloads_options = {str(index+1):value for index, value in enumerate(payl_list)}       
            




    try:
        globals()["payloads_value"] = payloads_options[submenu_input(payloads_options)]
    except KeyError:
        pass







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
  encoders_options = {"1": "fake_encoders_option_1",
                      "2": "fake_encoders_option_2",
                      "3": "fake_encoders_option_3",
                      "4": "fake_encoders_option_4"}
  
  try:
    globals()["encoders_value"] = encoders_options[submenu_input(encoders_options)]
  except KeyError:
    pass

#--------------------------------------------------

# def payloads_submenu():
#   payloads_options = {"1": "fake_payloads_option_1",
#                       "2": "fake_payloads_option_2",
#                       "3": "fake_payloads_option_3",
#                       "4": "fake_payloads_option_4"}
  
#   try:
#     globals()["payloads_value"] = payloads_options[submenu_input(payloads_options)]
#   except KeyError:
#     pass

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
