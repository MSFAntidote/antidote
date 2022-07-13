def rhost_submenu():
    rhost = input("Please enter Target IP address: ")

    try: 
        globals()["rhost_value"] = str(ipaddress.ip_address(rhost))
    except:
        print("Invalid IP address")