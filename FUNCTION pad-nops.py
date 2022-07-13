def pad_nops_submenu():

  if pad_nops_value == "On":
    globals()["pad_nops_value"] = ""
    print("\nPad-nops feature turned off.")
  else:
    globals()["pad_nops_value"] = "On"
    print("\nPad-nops feature turned on.")
