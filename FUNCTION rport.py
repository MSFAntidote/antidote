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
