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
