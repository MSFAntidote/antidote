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
