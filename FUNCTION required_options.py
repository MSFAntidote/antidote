def required_options_submenu():
  if payloads_value:
    try:
      print('\nReticulating splines...\n\n')
      options = subprocess.getoutput(f"msfvenom --list-options -p {payloads_value}")
      sliced = options.split("Basic options:")[1].split('Name                        Current Setting  Required  Description')[0]
      print(sliced)
    except:
      pass
  else:
    print("\nPlease select a payload first.")


