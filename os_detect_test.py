import sys, os, subprocess

platform = ''
architecture =''
ip = ''
port = ''
stage = ''
LHOST = ''
LPORT = ''
form= ''
payload = ''
output = ''

detect = input('\nWelcome to MSF Antidote.  Would you like to enable OS detection? [Requires Nmap] (y/n)  ')
if detect.lower() == 'y':
    ip = input('\nPlease enter the target IP: ')
    command = ['sudo', 'nmap', '-O', f'{ip}']
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    text = p.stdout.read()
    retcode = p.wait()
    print(text)

 




