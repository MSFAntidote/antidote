def encoding_submenu():

    print('\nFetching encoders from msfvenom framework.  Please wait...\n\n')

    probe = [enco.lstrip().split(" ")[0] for enco in subprocess.getoutput("msfvenom --list encoders").split("\n")[6:-1]]
    encoding_options = {str(item + 1): probe[item] for item in range(0, len(probe))}

    try:
        globals()["encoding_values"] = encoding_options[submenu_input(encoding_options)]
    except KeyError:
        pass
