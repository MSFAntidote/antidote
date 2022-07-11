def encryptions_submenu():

    print('\nFetching encrypts from msfvenom framework.  Please wait...\n\n')

    probe = [encr.lstrip().split(" ")[0] for encr in subprocess.getoutput("msfvenom --list encrypt").split("\n")[6:-1]]
    encryptions_options = {str(item + 1): probe[item] for item in range(0, len(probe))}

    try:
        globals()["encryptions_value"] = encryptions_options[submenu_input(encryptions_options)]
    except KeyError:
        pass
