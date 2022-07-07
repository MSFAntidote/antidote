#!/usr/bin/env python3


import subprocess, re

##temporary platform function for testing##
def platform():
    plat = 'linux'
    return plat

##Temporary architecture function for testing##
def architecture():
    arch = 'x64'
    return arch

##Get output from msfvenom --list payloads##
def payload():
    # platforms_list = [plat.lstrip().split(" ")[0] for plat in subprocess.getoutput('msfvenom --list platforms').split('\n')[6:-1]]
    # archs = [arch.lstrip().split(" ")[0] for arch in subprocess.getoutput('msfvenom --list archs').split('\n')[6:-1]]
    payload_list = [payl.lstrip().split(" ")[0] for payl in subprocess.getoutput('msfvenom --list payloads').split('\n')[6:-1]]
    
    
##Inner function to enumerate compatible options and list them for input##
    def multiple_choice(options):
                
        for idx, element in enumerate(options):
            print("{}) {}\n".format(idx + 1, element))

        i = input("Enter number: \n\n")
        try:
            if 0 < int(i) <= len(options):
                return int(i) - 1
        except:
            pass
        return None
        
##retrieve variables from platform and architecture functions##
    plat = platform()
    arch = architecture()
    no_arch = ['android', 'aix', 'firefox', 'java', 'mainframe', 'multi', 'netware', 'nodejs', 'php', 'python', 'r', 'ruby','unix', 'generic']

##Check if platform and architecture variables have been set by respective functions##
    if plat is not True:
        platform()
    elif arch is not True and arch not in no_arch:
        architecture()

##Windows x86 shell selection##
    if plat == 'windows' and arch == 'x86':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter', 'Powershell']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                
                if plat in selection and 'x64' not in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                
                if plat in selection and 'x64' not in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Powershell':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                
                if plat in selection and 'x64' not in selection and 'meterpreter' not in selection and 'powershell' in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Windows x64 shell selection##
    elif plat == 'windows' and arch == 'x64':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter', 'Powershell']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Powershell':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Linux x64 shell selection##
    elif plat == 'linux' and arch == 'x64':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Linux x86 shell selection##
    elif plat == 'linux' and arch == 'x86':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Linux zarch selection##
    elif plat == 'linux' and arch == 'zarch':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)

##Linux aarch64 selection##    
    elif plat == 'linux' and arch == 'aarch64':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Linux armbe selection##    
    elif plat == 'linux' and arch == 'armbe':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Linux armle selection##    
    elif plat == 'linux' and arch == 'armle':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Linux mips64 selection##
    elif plat == 'linux' and arch == 'mips64':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)  

##Linux mipsbe selection##    
    elif plat == 'linux' and arch == 'mipsbe':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options) 

##Linux mipsle selection##    
    elif plat == 'linux' and arch == 'mipsle':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)   

##Linux ppc selection##    
    elif plat == 'linux' and arch == 'ppc':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Linux ppc64 selection##
    elif plat == 'linux' and arch == 'ppc64':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)         

##Linux ppc64le selection##
    elif plat == 'linux' and arch == 'ppc64le':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)     

##Aix selection##
    elif plat == 'aix':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)  

##Android selection##    
    elif plat == 'android' and arch == '':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Apple_ios aarch64 selection##    
    elif plat == 'apple' and arch == 'aarch64':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)     

##BSD Sparc selection##
    elif plat == 'bsd' and arch == 'sparc':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)   

##BSD vax selection##
    elif plat == 'bsd' and arch == 'vax':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)     

##BSD x64 selection##
    elif plat == 'bsd' and arch == 'x64':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)   

##BSD x86 selection##
    elif plat == 'bsd' and arch == 'x86':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)        

##BSDi x86 selection##
    elif plat == 'bsdi' and arch == 'x86':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)    

##Firefox selection##
    elif plat == 'firefox' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)   

##Java selection##    
    elif plat == 'java' and arch == '':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##Mainframe selection##
    elif plat == 'mainframe' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)      

##Multi selection##
    elif plat == 'multi' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)      

##Netware selection##
    elif plat == 'netware' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options) 

##Nodejs selection##
    elif plat == 'nodejs' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and 'cmd' not in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)  

##OSX armle selection##
    elif plat == 'osx' and arch == 'armle':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)  

##OSX ppc selection##
    elif plat == 'osx' and arch == 'ppc':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
     
##OSX x64 selection##    
    elif plat == 'osx' and arch == 'x64':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and arch in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

##OSX x86 selection##
    elif plat == 'osx' and arch == 'x86':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)   

##PHP selection##
    elif plat == 'php' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and 'cmd' not in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)  

##Python selection##    
    elif plat == 'python' and arch == '':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and 'meterpreter' not in selection and 'powershell' not in selection and 'cmd' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and 'meterpreter' in selection and 'powershell' not in selection and 'cmd' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)  

##r selection##
    elif plat == 'r' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and 'cmd' not in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)       

##Ruby selection##
    elif plat == 'ruby' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and 'cmd' not in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)   

##Solaris sparc selection##
    elif plat == 'solaris' and arch == 'sparc':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)    

##Solaris x86 selection##
    elif plat == 'solaris' and arch == 'x86':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and arch in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)    

##Unix selection##    
    elif plat == 'unix' and arch == '':
        options_list =[]
        print('\nSelect from available shells:  \n\n')
        shells = ['Default', 'Meterpreter']
        options = shells
        res = multiple_choice(options)

        if options[res] == 'Default':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and 'meterpreter' not in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)

        if options[res] == 'Meterpreter':
            for string in payload_list:
                selection = re.split(r'[/_]', string)
                    
                if plat in selection and 'meterpreter' in selection and 'powershell' not in selection:
                    options = '/'.join(selection)
                    if options not in options_list:
                        options_list.append(options)  

##Ruby selection##
    elif plat == 'generic' and arch == '':
        options_list =[]
        for string in payload_list:
            selection = re.split(r'[/_]', string)
            if plat in selection and 'cmd' not in selection:
                options = '/'.join(selection)
                if options not in options_list:
                        options_list.append(options)                                                                                                                                                                                                           
    
            
##Payload user input##
    print('\nPlease select from compatible payloads: \n\n')
    options = options_list
    res = multiple_choice(options_list)

##Take selected input and set as a msfvenom command and return##    
    payload_cmd = f'-p {options[res]}'
    payload_str = f'{options[res]}'
    

##Choose another payload or return to main##
    return_input = input(f'\nKeep current payload?:  {payload_str}  (y/n)\n\n')
    if return_input.lower == 'y':
        return payload_cmd, payload_str
        main()
    else:
        payload()







### MAIN FUNCTION ###
def main():
     payload()
        

  
  ### DUNDER CHECK ###
if __name__ == "__main__":
  main()