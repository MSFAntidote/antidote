def encoding_submenu():

    try:
        globals()["encoding_options"] = encoding_options
    except NameError:

        print('Importing encoders from msfvenom framework.  Please wait...')
        probe = [enco.lstrip().split(" ")[0] for enco in subprocess.getoutput("msfvenom --list encoders").split("\n")[6:-1]]
        globals()["architectures_options"] = {str(item + 1): probe[item] for item in range(0, len(probe))}
        print("Complete")
        
    try:
        globals()["encoding_value"] = encoding_options[submenu_input(encoding_options)]
    except KeyError:
        pass
