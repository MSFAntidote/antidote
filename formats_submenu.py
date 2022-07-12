def formats_submenu():
    try:
        globals()["formats_options"] = formats_options
    except NameError:
        print('Importing formats from msfvenom framework.  Please wait...')
        probe = [form.lstrip().split(" ")[0] for form in subprocess.getoutput("msfvenom --list formats").split("\n")[6:-1]]
        exclude = ['Framework', '==============================================', '', 'Name', '----']
        final_list = list(set(probe) - set(exclude))
        globals()[formats_options] = {str(item + 1): final_list[item] for item in range(0, len(final_list))}

    try:
        globals()["formats_value"] = formats_options[submenu_input(formats_options)]
    except KeyError:
        pass