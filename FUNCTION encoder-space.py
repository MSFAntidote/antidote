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
