#!/usr/bin/env python3

import sys, os, subprocess


#Command Variables
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

#Color Variables

black = '\u001b[30m'
red = '\u001b[31m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
Cyan = '\u001b[36m'
white = '\u001b[37m'

black_b = '\u001b[40m'
red_b = '\u001b[41m'
green_b = '\u001b[42m'
yellow_b = '\u001b[43m'
blue_b = '\u001b[44m'
magenta_b = '\u001b[45m'
cyan_b = '\u001b[46m'
white_b = '\u001b[47m'


def main():

    #OS Detection
    detect_input = input('\nWelcome to MSF Antidote.  Would you like to enable OS detection? [Requires Nmap] (y/n)  ')

    if detect_input.lower() == 'y':
        ip_input = input('\nPlease enter the target IP: ')
        command = ['sudo', 'nmap', '-O', f'{ip_input}']
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        text = p.stdout.readlines()
        retcode = p.wait()

    #Platform Selection
    elif detect_input.lower() == 'n':
        platform_input = input('\nSelect your target platform:\n\n1) Windows\n\n2) Linux\n\n3) OSX\n\n4) Apple ios\n\n5) Android\n\n')
        os.system('clear')



    ### WINDOWS-----------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '1':
            platform = 'msfvenom -p windows/' 
            form = '-f exe'
            
        #Windows Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) x86\n\n2) x64')
            os.system('clear')
            if architecture_input == '1':
                architecture = 'x86'

        #Windows x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = '/Payload Placeholder 1'
                elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
                elif payload_input == '3':
                    payload = '/Payload Placeholder 3'

        #Windows x64 Payload Input
            elif architecture_input == '2':
                architecture = 'x64'

        #Windows x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = '/Payload Placeholder 1'
                elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
                elif payload_input == '3':
                    payload = '/Payload Placeholder 3'   



    ### LINUX-------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '2':
            platform = 'msfvenom -p linux/' 
            form = '-f elf'                 
    
        #Linux Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) x86\n\n2) x64')
            os.system('clear')
            if architecture_input == '1':
                architecture = 'x86'

        #Linux x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = '/Payload Placeholder1'
                elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
                elif payload_input == '3':
                    payload = '/Payload Placeholder 3'

        #Linux x64 Payload Input
            elif architecture_input == '2':
                architecture = 'x64'

        #Linux x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = '/Payload Placeholder 1'
                elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
                elif payload_input == '3':
                    payload = '/Payload Placeholder 3'



    ### OSX-----------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '3':
            platform = 'msfvenom -p osx/' 
            form = '-f macho'
            
        #OSX Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) x86\n\n2) x64')
            os.system('clear')
            if architecture_input == '1':
                architecture = 'x86'

        #OSX x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = '/Payload Placeholder 1'
                elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
                elif payload_input == '3':
                    payload = '/Payload Placeholder 3'

        #OSX x64 Payload Input
            elif architecture_input == '2':
                architecture = 'x64'

        #OSX x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = '/Payload Placeholder 1'
                elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
                elif payload_input == '3':
                    payload = '/Payload Placeholder 3'                    



    ### Apple ios-----------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '4':
            platform = 'msfvenom -p apple_ios/' 
            form = '-f exe'
            
        #Apple ios Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) aarch64\n\n2) armle')
            os.system('clear')
            if architecture_input == '1':
                architecture = 'aarch64'

        #Apple ios x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = '/Payload Placeholder 1'
                elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
                elif payload_input == '3':
                    payload = '/Payload Placeholder 3'

        #Apple ios x64 Payload Input
            elif architecture_input == '2':
                architecture = 'armle'

        #Apple ios x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = '/Payload Placeholder 1'
                elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
                elif payload_input == '3':
                    payload = '/Payload Placeholder 3'                                    



    ### ANDROID-----------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '5':
            platform = 'msfvenom -p android/' 
            form = '-f exe'  
        
        #Android Payload Input
            payload_input = input('Select from available payloads:\n\n1) Payload Placeholder1\n\n2) Payload Placeholder2\n\n3) Payload Placeholder3\n\n')
            os.system('clear')  

            if payload_input == '1':
                    payload = '/Payload Placeholder 1'
            elif payload_input == '2':
                    payload = '/Payload Placeholder 2'
            elif payload_input == '3':
                    payload = '/Payload Placeholder 3'



    #Port and IP Input
    ip_input = input('\nEnter Target IP: \n\n')
    LHOST = f'LHOST={ip_input}'
    os.system('clear')

    port_input = input('\nEnter Target Port: \n\n')
    LPORT = f'LPORT={port_input}'   
    os.system('clear')




    #File Output
    output = input('\nPlease Name Your File: ')
    output = f'> {output}'
    os.system('clear')

    #Final Command       
    cmd = f'{platform}{architecture}{payload} {LHOST} {LPORT} {form} {output}'

    # os.system(cmd)
    print(cmd)

    #Repeat or exit
    repeat = input('\n\nWould you like to create another payload?  (y/n): \n\n')
    if repeat.lower() == "y":
        main()
    else:
        print('Good Bye')
        exit()
  
  
  ### DUNDER CHECK ###
if __name__ == "__main__":
  main()