def iterations_submenu():
  globals()["iterations_value"] = ""  

  while iterations_value == "":

    try:
      globals()["iterations_value"] = int(input("\nPlease enter a number of times to encode the payload: "))
    except ValueError:
      print("\nInvalid number of times to encode the payload. Please enter an integer.")
    else:
      print("Number of times to encode the payload set.")

  globals()["iterations_value"] = str(iterations_value)
