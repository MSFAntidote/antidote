#!/usr/bin/env python3


import subprocess

##temporary platform function for testing##
def platform():
    plat = 'windows'
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
    options_list =[]

##retrieve variables from platform and architecture functions##
    plat = platform()
    arch = architecture()

##Check if platform and architecture variables have been set by respective functions##
    if plat is not True:
        platform()
    elif arch is not True:
        architecture()

##Split payload strings by '/' into lists##
    for string in payload_list:
        selection = string.split('/')

##If architype and platform selections are found in list, rejoin into payload string and add to options_list##
        if plat in selection and arch in selection:
            options = '/'.join(selection)
            options_list.append(options)
            

##Start of user input##
    print('\nPlease select from compatible payloads: /n/n')
            
    
##Inner function to enumerate compatible options and list them for input##
    def let_user_pick(options):
                
        for idx, element in enumerate(options):
            print("{}) {}\n".format(idx + 1, element))

        i = input("Enter number: ")
        try:
            if 0 < int(i) <= len(options):
                return int(i) - 1
        except:
            pass
        return None


    options = options_list
    res = let_user_pick(options)

##Take selected input and set as a msfvenom command and returned##    
    payload_cmd = f'-p {options[res]}'
    print(payload_cmd)
    return payload_cmd







### MAIN FUNCTION ###
def main():
     payload()
        

  
  ### DUNDER CHECK ###
if __name__ == "__main__":
  main()