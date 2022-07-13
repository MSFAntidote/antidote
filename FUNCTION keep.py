def keep_submenu():

  if keep_value == "On":
    globals()["keep_value"] = ""
    print("\nPreserve template behavior and inject the payload as a new thread turned off.")
  else:
    globals()["keep_value"] = "On"
    print("\nPreserve template behavior and inject the payload as a new thread turned on.")
