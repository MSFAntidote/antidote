def lport_submenu():
  bad_port = "\nInvalid port number. Please enter an integer between 0 and 65535."
  loop = True

  while loop:

    try:
      globals()["lport_value"] = int(input("\nPlease enter a port number: "))

    except ValueError:
      print(bad_port)
    else:
      if lport_value in range(65536):
        print("\nLocal port set.")
        loop = False
      else:
        print(bad_port)

  globals()["lport_value"] = str(lport_value)
