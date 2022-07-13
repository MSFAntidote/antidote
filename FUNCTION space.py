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
