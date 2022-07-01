#!/usr/bin/env python

import subprocess

payloads = open("msfvenom_payloads.txt").readlines()
architectures = open("msfvenom_architectures.txt").readlines()
database = open("msfantidote_pay_arch.db", "a")

for payload in payloads:
  payload = payload.rstrip("\n")

  for architecture in architectures:
    architecture = architecture.rstrip("\n")
    line = "msfvenom -p " + payload + " -a " + architecture
    print("Trying: " + line)

    try:
      output = subprocess.getoutput(line)
    except:
      print(payload + " is compatible with " + architecture + "! Payload/architecture pair added to database.")
      database.write(payload + ";" + architecture + "\n")

database.close()
