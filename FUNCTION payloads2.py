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