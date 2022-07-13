def nopsled_submenu():
  loop = True

  while loop:

    try:
      globals()["nopsled_value"] = int(input("\nPlease enter a nopsled value: "))
    except ValueError:
      print("\nInvalid nopsled value. Please enter an integer.")
    else:
      print("Nopsled value set.")
      loop = False

  globals()["nopsled_value"] = str(nopsled_value)
