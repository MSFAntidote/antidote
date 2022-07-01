import os

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

platform = input('\nSelect Target Platform #: \n\n1) Linux\n2) Windows\n\n')

if platform == '1':
  platform = 'msfvenom -p Linux/'
  form = '-f elf'
elif platform == '2':
  platform = 'msfvenom -p Windows/'
  form = '-f exe'


architecture = input('\nSelect Platform architecture #: \n\n1) x86\n2) x64\n\n')

if architecture == '1':
  architecture = 'x86/'
elif architecture == '2':
  architecture = 'x64/'


ip = input('\nEnter Target IP: \n\n')
LHOST = f'LHOST={ip}'


port = input('\nEnter Target Port: \n\n')
LPORT = f'LPORT={port}'


payload = input('\nSelect Payload: \n\n1) payload1\n2) payload2\n\n')

if payload == '1':
  payload = 'payload1'
elif payload == '2':
  payload = 'payload2'


output = input('\nPlease Name Your File: ')
output = f'> {output}'

        
cmd = f'{platform}{architecture}{payload} {LHOST} {LPORT} {form} {output}'

# os.system(cmd)

print(cmd)