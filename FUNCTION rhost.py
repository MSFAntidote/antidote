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