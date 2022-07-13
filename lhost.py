def lhost_submenu():
    lhost = input("Please enter local IP address: ")

    try: 
        globals()["lhost_value"] = str(ipaddress.ip_address(lhost))
    except:
        print("Invalid IP address")