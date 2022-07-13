def template_submenu():
    temp = input("\nPlease enter the name of the file you wish to use as a template: ")

    try: 
        globals()["template_value"] = temp
    except:
        pass