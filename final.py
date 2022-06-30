import os

platform = ''
ip = ''
port = ''
stage = ''
LHOST = ''
LPORT = ''

platform = input('\nSelect Target Platform #: \n\n1) Linux\n2) Windows\n\n')

if platform == '1':
  platform = 'msfvenom -p Linux/'
elif platform == '2':
  platform = 'msfvenom -p Windows/'

## TEST PRINT##
print(platform)

ip = input('\nEnter Target IP: \n\n')
LHOST = f'LHOST={ip}'

##TEST PRINT##
print(LHOST)

        
