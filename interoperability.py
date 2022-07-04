#!/usr/bin/env python

import subprocess

#any payload will do
random_payload = "windows/x64/vncinject/reverse_winhttps"

#reach out to msfvenom at the comand line, obfuscate the output and store it to a variable
execute_this = subprocess.getoutput("msfvenom --list-options -p " + random_payload)

#grab the architecture and save it to a variable 
arch = execute_this.split("Arch: ")[1].split("\n")[0]

#grab the platform and save it to a variable
plat = execute_this.split("Platform: ")[1].split("\n")[0]

#display the architecture and platform
print("Architecture:", arch)
print("Platform:", plat)
