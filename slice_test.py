from asyncio.subprocess import PIPE
import os, sys, subprocess, re


       
command = ['msfvenom', '--list', 'payloads']
cmdpipe = subprocess.Popen(command, stdout=subprocess.PIPE)
output = str(cmdpipe.communicate())

pattern = re.compile(r'')
strings = re.findall(pattern, output)
print(strings)

# print(text)

# out = subprocess.Popen(['msfvenom', '--list', 'payloads'],
# stdout=subprocess.PIPE,
# stderr=subprocess.STDOUT)

# stdout,stderr = out.communicate()
# print(stdout)

# cmd = "msfvenom --list payloads | cut -d ' ' -f 5"
# payloads = (os.system(cmd))
