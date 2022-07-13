def required_options_submenu():
  if payloads_value:
    try:
      cmd = f"msfvenom --list-options -p {payloads_value}"
      os.system(cmd)
    except:
      pass
  else:
    print("\nPlease select a payload first.")