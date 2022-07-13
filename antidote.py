#!/usr/bin/env python
#Revision 7/11/2022 - Devon's alternate payload method

import inspect, math, re, subprocess, ipaddress, os
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------



#--------------------------------------------------

def var_name_submenu():
  globals()["var_name_value"] = input("\nEnter a custom variable name: ")
  print("Custom variable name set.")


#--------------------------------------------------

def iterations_submenu():
  globals()["iterations_value"] = ""  

  while iterations_value == "":

    try:
      globals()["iterations_value"] = int(input("\nPlease enter a number of times to encode the payload: "))
    except ValueError:
      print("\nInvalid number of times to encode the payload. Please enter an integer.")
    else:
      print("Number of times to encode the payload set.")

  globals()["iterations_value"] = str(iterations_value)


#--------------------------------------------------

def encoder_space_submenu():
  globals()["encoder_space_value"] = ""  

  while encoder_space_value == "":

    try:
      globals()["encoder_space_value"] = int(input("\nPlease enter a maximum encoded payload size in bytes: "))
    except ValueError:
      print("\nInvalid maximum encoded payload size. Please enter an integer.")
    else:
      print("Maximum encoded payload size set.")

  globals()["encoder_space_value"] = str(encoder_space_value)


#--------------------------------------------------

def bad_chars_submenu():
  globals()["bad_chars_value"] = input("\nEnter characters to avoid: ")
  print("Characters to avoid set.")


#--------------------------------------------------

def encrypt_key_submenu():
  globals()["encrypt_key_value"] = input("\nEnter an encryption key: ")
  print("Encryption key set.")


#--------------------------------------------------

def encrypt_iv_submenu():
  globals()["encrypt_iv_value"] = input("\nEnter an initialization vector: ")
  print("Initialization vector set.")


#--------------------------------------------------

def add_code_submenu():
  globals()["add_code_value"] = input("\nEnter a win32 shellcode file name: ")
  print("Win32 shellcode file name set.")

#--------------------------------------------------

def required_options_submenu():
  if payloads_value:
    try:
      options = subprocess.getoutput(f"msfvenom --list-options -p {payloads_value}").split('\n\nAdvanced options')[0]
      print(options)
    except:
      pass
  else:
    print("\nPlease select a payload first.")

#--------------------------------------------------

def space_submenu():
  globals()["space_value"] = ""  

  while space_value == "":

    try:
      globals()["space_value"] = int(input("\nPlease enter a maximum payload size in bytes: "))
    except ValueError:
      print("\nInvalid maximum payload size. Please enter an integer.")
    else:
      print("Maximum payload size set.")

  globals()["space_value"] = str(space_value)


#--------------------------------------------------

def keep_submenu():

  if keep_value == "On":
    globals()["keep_value"] = ""
    print("\nPreserve template behavior and inject the payload as a new thread turned off.")
  else:
    globals()["keep_value"] = "On"
    print("\nPreserve template behavior and inject the payload as a new thread turned on.")


#--------------------------------------------------

def smallest_submenu():

  if smallest_value == "On":
    globals()["smallest_value"] = ""
    print("\nSmallest possible payload feature turned off.")
  else:
    globals()["smallest_value"] = "On"
    print("\nSmallest possible payload feature turned on.")


#--------------------------------------------------

def service_name_submenu():
  globals()["service_name_value"] = input("\nEnter a service name: ")
  print("Service name set.")


#--------------------------------------------------

def sec_name_submenu():
  globals()["sec_name_value"] = input("\nEnter a section name: ")
  print("Section name set.")

#--------------------------------------------------

def pad_nops_submenu():

  if pad_nops_value == "On":
    globals()["pad_nops_value"] = ""
    print("\nPad-nops feature turned off.")
  else:
    globals()["pad_nops_value"] = "On"
    print("\nPad-nops feature turned on.")


#--------------------------------------------------

def nopsled_submenu():
  globals()["nopsled_value"] = ""  

  while nopsled_value == "":

    try:
      globals()["nopsled_value"] = int(input("\nPlease enter a nopsled value: "))
    except ValueError:
      print("\nInvalid nopsled value. Please enter an integer.")
    else:
      print("Nopsled value set.")

  globals()["nopsled_value"] = str(nopsled_value)


#--------------------------------------------------

def template_submenu():
    temp = input("\nPlease enter the name of the file you wish to use as a template: ")

    try: 
        globals()["template_value"] = temp
    except:
        pass

#--------------------------------------------------

def encrypt_submenu():

    try:
        globals()["encrypt_options"] = encrypt_options
    except NameError:
        print('\nImporting encryptions from msfvenom framework.  Please wait...')
        probe = [encr.lstrip().split(" ")[0] for encr in subprocess.getoutput("msfvenom --list encrypt").split("\n")[6:-1]]
        globals()["encrypt_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
        print("Complete")
        
    try:
        globals()["encrypt_value"] = encrypt_options[submenu_input(encrypt_options)]
    except KeyError:
        pass


#--------------------------------------------------

def encoding_submenu():

    try:
        globals()["encoding_options"] = encoding_options
    except NameError:

        print('Importing encoders from msfvenom framework.  Please wait...')
        probe = [enco.lstrip().split(" ")[0] for enco in subprocess.getoutput("msfvenom --list encoders").split("\n")[6:-1]]
        globals()["encoding_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
        print("Complete")
        
    try:
        globals()["encoding_value"] = encoding_options[submenu_input(encoding_options)]
    except KeyError:
        pass


#--------------------------------------------------

def rport_submenu():
  bad_rport = "\nInvalid port number. Please enter an integer between 0 and 65535."
  loop = True

  while loop:

    try:
      globals()["rport_value"] = int(input("\nPlease enter a port number: "))

    except ValueError:
      print(bad_rport)
    else:
      if rport_value in range(65536):
        print("\nTarget port set.")
        loop = False
      else:
        print(bad_rport)

  globals()["rport_value"] = str(rport_value)

#--------------------------------------------------

def rhost_submenu():

  globals()["rhost_value"] = ""

  while rhost_value == "":

    try:
      rhost = input("\nPlease enter a target IP address: ")
      rhost_test = ipaddress.ip_address(rhost)

    except ValueError:
      print("\nInvalid IP address.")

    else:
      print("Target IP set.")
      globals()["rhost_value"] = rhost

#--------------------------------------------------

def lport_submenu():
  bad_lport = "\nInvalid port number. Please enter an integer between 0 and 65535."
  loop = True

  while loop:

    try:
      globals()["lport_value"] = int(input("\nPlease enter a port number: "))

    except ValueError:
      print(bad_lport)
    else:
      if lport_value in range(65536):
        print("\nLocal port set.")
        loop = False
      else:
        print(bad_lport)

  globals()["lport_value"] = str(lport_value)


#--------------------------------------------------

def lhost_submenu():
  globals()["lhost_value"] = ""

  while lhost_value == "":
    
    try:
      lhost = input("\nPlease enter a local IP address: ")
      lhost_test = ipaddress.ip_address(lhost)
    except:
      print("\nInvalid IP address.")
    else:
      print("Local host set.")
      globals()["lhost_value"] = lhost

#--------------------------------------------------

def formats_submenu():
    try:
        globals()["formats_options"] = formats_options
    except NameError:
        print('\nImporting formats from msfvenom framework.  Please wait...')
        probe = [form.lstrip().split(" ")[0] for form in subprocess.getoutput("msfvenom --list formats").split("\n")[6:-1]]
        exclude = ['Framework', '==============================================', '', 'Name', '----']
        final_list = list(set(probe) - set(exclude))
        globals()["formats_options"] = {str(item + 1): final_list[item] for item in range(0, len(final_list))}

    try:
        globals()["formats_value"] = formats_options[submenu_input(formats_options)]
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

      payloads_options = {str(index+1):value for index, value in enumerate(payloads_list)}

      try:
        globals()["payloads_value"] = payloads_options[submenu_input(payloads_options)]
      except KeyError:
        pass
      finally:
        return

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
      except KeyError:
        pass
      finally:
        return

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
            if platforms_value in selection and 'x64' not in selection and 'cmd' not in selection and 'meterpreter_bind_named_pipe' not in selection and 'meterpreter_bind_tcp' not in selection and 'meterpreter_reverse_http' not in selection and 'meterpreter_reverse_https' not in selection and 'meterpreter_reverse_ipv6_tcp' not in selection and 'meterpreter_reverse_tcp' not in selection and 'powershell_bind_tcp' not in selection and 'powershell_reverse_tcp' not in selection and 'powershell_reverse_tcp_ssl' not in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection or ('generic' in selection and 'cmd' not in selection):
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
          
          elif platforms_value == 'windows' and architectures_value != 'x86': 
            if platforms_value in selection and architectures_value in selection and 'cmd' not in selection and 'meterpreter_bind_named_pipe' not in selection and 'meterpreter_bind_tcp' not in selection and 'meterpreter_reverse_http' not in selection and 'meterpreter_reverse_https' not in selection and 'meterpreter_reverse_ipv6_tcp' not in selection and 'meterpreter_reverse_tcp' not in selection and 'powershell_bind_tcp' not in selection and 'powershell_reverse_tcp' not in selection and 'powershell_reverse_tcp_ssl' not in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection or ('generic' in selection and 'cmd' not in selection):
              payl = '/'.join(selection)
              payl_list.append(payl)
            payloads_options_2 = {str(index+1):value for index, value in enumerate(payl_list)}
          
          else:
            if platforms_value in selection and architectures_value in selection and 'cmd' not in selection and 'meterpreter_bind_named_pipe' not in selection and 'meterpreter_bind_tcp' not in selection and 'meterpreter_reverse_http' not in selection and 'meterpreter_reverse_https' not in selection and 'meterpreter_reverse_ipv6_tcp' not in selection and 'meterpreter_reverse_tcp' not in selection and 'powershell_bind_tcp' not in selection and 'powershell_reverse_tcp' not in selection and 'powershell_reverse_tcp_ssl' not in selection and 'powershell_bind_tcp' not in selection and 'powershell_reverse_tcp' not in selection and 'powershell_reverse_tcp_ssl' not in selection and 'meterpreter' not in selection and 'patchupmeterpreter' not in selection and 'powershell' not in selection or ('generic' in selection and 'cmd' not in selection):
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

  add_code_str = ''
  bad_chars_str = ''  
  encoder_space_str = ''  
  encoding_str = ''
  encrypt_iv_str = ''
  encrypt_key_str = ''
  encrypt_str = ''
  formats_str = ''
  iterations_str = ''
  keep_str = ''
  lhost_str = ''
  lport_str = ''
  nopsled_str = ''
  pad_nops_str = ''
  rhost_str = ''
  rport_str = ''
  sec_name_str = ''
  service_name_str = ''
  smallest_str = ''
  space_str = ''
  template_str = ''
  var_name_str = ''
  architectures_str = ''
  platforms_str = ''

  if payloads_value:    
    payload_str = f"msfvenom -p {payloads_value} "
    if add_code_value:
      add_code_str = f"-c {add_code_value} "
    if platforms_value:
      platforms_str = f"--platform {platforms_value} "
    if architectures_value:
      architectures_str = f"--arch {architectures_value} "
    if bad_chars_value:
        bad_chars_str = f"-b {bad_chars_value} "
    if encoder_space_value:
        encoder_space_str = f"--encoder-space {encoder_space_value} "
    if encoding_value:
        encoding_str = f"--encoder {encoding_value} "
    if encrypt_iv_value:
        encrypt_iv_str = f"--encrypt-iv {encrypt_iv_value} "
    if encrypt_key_value:
        encrypt_key_str = f"--encrypt-key {encrypt_key_value} "
    if encrypt_value:
        encrypt_str = f"--encrypt {encrypt_value} "
    if formats_value:
        formats_str = f"-f {formats_value} "
    if iterations_value:
        iterations_str = f"-i {iterations_value} "
    if keep_value:
        keep_str = f"--keep "
    if lhost_value:
        lhost_str = f"LHOST={lhost_value} "
    if lport_value:
        lport_str = f"LPORT={lport_value} "
    if nopsled_value:
        nopsled_str = f"--nopsled {nopsled_value} "
    if pad_nops_value:
        pad_nops_str = f"--pad-nops "
    if rhost_value:
        rhost_str = f"RHOST={rhost_value} "
    if rport_value:
        rport_str = f"RPORT={rport_value} "
    if sec_name_value:
        sec_name_str = f"--sec-name {sec_name_value} "
    if service_name_value:
        service_name_str = f"--service-name {service_name_value} "
    if smallest_value:
        smallest_str = f"--smallest "
    if space_value:
        space_str = f"--space {space_value} "
    if template_value:
        template_str = f"-x {template_value} "
    if var_name_value:
        var_name_str = f"-v {var_name_value} "


    file_name = input("Enter a file name: ")
    file_name_str = f"-o {file_name}"

    cmd = f"{payload_str}{platforms_str}{architectures_str}{lhost_str}{lport_str}{rhost_str}{rport_str}{add_code_str}{bad_chars_str}{encoder_space_str}{encoding_str}{encrypt_iv_str}{encrypt_key_str}{encrypt_str}{formats_str}{iterations_str}{keep_str}{nopsled_str}{pad_nops_str}{sec_name_str}{service_name_str}{smallest_str}{space_str}{template_str}{var_name_str}{file_name_str}"
    print(f"\n{cmd}")
    agree = input("\nWould you like to generate this payload?  (y/n): ")

    if agree.lower() == 'y':    
        print("\nGenerating payload. Please wait...")
        os.system(f'{cmd}')
    elif agree.lower() == 'n':
        clear_selections()
    else:
        print("\nWrong input.  Please select 'y' or 'n'")
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
                           "4": "lhost",
                           "5": "lport",
                           "6": "rhost",
                           "7": "rport",
                           "8": "encoding",
                           "9": "encrypt",
                           "10": "formats", 
                           "11": "nopsled",
                           "12": "pad_nops",
                           "13": "template",
                           "14": "smallest",
                           "15": "sec_name",
                           "16": "service_name",
                           "17": "keep",
                           "18": "space",
                           "19": "add_code",
                           "20": "bad_chars",
                           "21": "encoder_space",
                           "22": "iterations",
                           "23": "var_name",
                           "24": "encrypt_key",
                           "25": "encrypt_iv",
                           "0": "required_options",}
                        

  print("\nStarting msf antidote.  Please wait...") 
                            
  #print("Importing architectures from msfvenom. Please wait...")
  #probe = [arch.lstrip() for arch in subprocess.getoutput('msfvenom --list archs').split('\n')[6:-1]]
  #globals()["architectures_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
  #print("Complete.\nImporting payloads from msfvenom. Please wait...")  
  probe = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput("msfvenom --list payloads").split("\n")[6:-1]]
  globals()["payloads_list"] = probe
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
