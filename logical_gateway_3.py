#!/usr/bin/env python

import subprocess

def display_menu(options, footer):

  num_elements = len(options)
  border = "-" * 137
  line = ""
  
  print(border + "\nmsfAntidote v1.0\n" + border)
  
  for element in range(1, num_elements + 1):
    line += "[" + str(element).rjust(2) + "] " + options[element - 1].ljust(41)

    if not (element) % 3 or element == num_elements:
      print(line)
      line = ""

  print(border + "\n" + footer + "\n" + border)

def add_code_submenu():
  print("\nadd_code submenu")
  input("Press any key to continue...\n")
  
def architecture_submenu():
  print("\narchitecture submenu")
  input("Press any key to continue...\n")

def bad_chars_submenu():
  print("\nbad-chars submenu")
  input("Press any key to continue...\n")
  
def encoder_submenu():
  print("\nencoder submenu")
  input("Press any key to continue...\n")
  
def encoder_space_submenu():
  print("\nencoder-space submenu")
  input("Press any key to continue...\n")
  
def encrypt_submenu():
  print("\nencrypt submenu")
  input("Press any key to continue...\n")
  
def encrypt_iv_submenu():
  print("\nencrypt-iv submenu")
  input("Press any key to continue...\n")
  
def encrypt_key_submenu():
  print("\nencrypt-key submenu")
  input("Press any key to continue...\n")
  
def iterations_submenu():
  print("\niterations submenu")
  input("Press any key to continue...\n")
  
def keep_submenu():
  print("\nkeep submenu")
  input("Press any key to continue...\n")
  
def nopsled_submenu():
  print("\nnopsled submenu")
  input("Press any key to continue...\n")
  
def out_submenu():
  print("\nout submenu")
  input("Press any key to continue...\n")
  
def payload_submenu():
  print("\npayload submenu")
  input("Press any key to continue...\n")
  
def platform_submenu():
  print("\nplatform submenu")
  input("Press any key to continue...\n")
  
def sec_name_submenu():
  print("\nsec-name submenu")
  input("Press any key to continue...\n")
  
def service_name_submenu():
  print("\nservice-name submenu")
  input("Press any key to continue...\n")
  
def smallest_submenu():
  print("\nsmallest submenu")
  input("Press any key to continue...\n")
  
def space_submenu():
  print("\nspace submenu")
  input("Press any key to continue...\n")
  
def template_submenu():
  print("\ntemplate submenu")
  input("Press any key to continue...\n")
  
def timeout_submenu():
  print("\ntimeout submenu")
  input("Press any key to continue...\n")
  
def var_name_submenu():
  print("\nvar-name submenu")
  input("Press any key to continue...\n")
  
def main():
  print("splash page code\n")
  selection = "0"
  submenus = ("add_code",
              "architecture",
              "bad_chars",
              "encoder",
              "encoder_space",
              "encrypt",
              "encrypt_iv",
              "encrypt_key",
              "iterations",
              "keep",
              "nopsled",
              "out",
              "payload",
              "platform",
              "sec_name",
              "service_name",
              "smallest",
              "space",
              "template",
              "timeout",
              "var_name")

  for submenu in submenus:
    globals()[submenu + "_value"] = ""
  
  while selection != "q":
    display_menu(submenus, "Enter G to generate payload, C to clear selections or Q to quit")

    selection = input("\nmsfAntidote: ").lower()

    try:
      selection = int(selection) - 1

      if selection in range(21):
        eval(submenus[selection] + "_submenu()")
      else:
        print("\ninvalid selection - integer out of range")
      
    except ValueError:

      if selection == "c":
        print("\nclear selections code")
      elif selection == "g":
        print("\ngenerate payload code")
      elif selection != "q":
        print("\ninvalid selection - string")

if __name__ == "__main__":
  main()
