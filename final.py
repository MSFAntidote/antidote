#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys

### HELPER FUNCTIONS (IF NECESSARY) ###
def function(param):
        

### MAIN FUNCTION ###
def main():
    arg=sys.argv[1]
    with open(arg) as opened_file:
        function(opened_file)
        

  
  ### DUNDER CHECK ###
if __name__ == "__main__":
  main()