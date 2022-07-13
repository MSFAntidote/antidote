def smallest_submenu():

  if smallest_value == "On":
    globals()["smallest_value"] = ""
    print("\nSmallest possible payload feature turned off.")
  else:
    globals()["smallest_value"] = "On"
    print("\nSmallest possible payload feature turned on.")
