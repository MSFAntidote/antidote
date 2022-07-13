def encrypt_submenu():

  try:
    globals()["encrypt_options"] = encryptions_options
  except NameError:
    print('\nImporting encryptions from msfvenom framework.  Please wait...')
    probe = [encr.lstrip().split(" ")[0] for encr in subprocess.getoutput("msfvenom --list encrypt").split("\n")[6:-1]]
    globals()["encrypt_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
    print("Complete")
        
  try:
    globals()["encrypt_value"] = encrypt_options[submenu_input(encrypt_options)]
  except KeyError:
    pass
