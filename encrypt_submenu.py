def encryptions_submenu():

    try:
        globals()["encryptions_options"] = architectures_options
    except NameError:
        print('Importing encryptions from msfvenom framework.  Please wait...')
        probe = [encr.lstrip().split(" ")[0] for encr in subprocess.getoutput("msfvenom --list encrypt").split("\n")[6:-1]]
        globals()["encryptions_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
        print("Complete")
        
    try:
        globals()["encryptions_value"] = encryptions_options[submenu_input(encryptions_options)]
    except KeyError:
        pass
