def nopsled_submenu():

  try:
    nopsled = int(input("\nEnter an integer for the nopsled value: "))
  except:
    print("Invalid nopsled value.")
  else:
    globals()["nopsled_value"] = str(nopsled)
    print("Nopsled value set.")
