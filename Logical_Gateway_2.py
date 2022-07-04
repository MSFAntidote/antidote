#!/usr/bin/env python

import subprocess

def add_code_submenu():
  print("\nadd_code submenu")

def architecture_submenu():
  print("\narchitecture submenu")

def bad_chars_submenu():
  print("\nbad-chars submenu")

def encoder_submenu():
  print("\nencoder submenu")

def encoder_space_submenu():
  print("\nencoder-space submenu")

def encrypt_submenu():
  print("\nencrypt submenu")

def encrypt_iv_submenu():
  print("\nencrypt-iv submenu")

def encrypt_key_submenu():
  print("\nencrypt-key submenu")

def iterations_submenu():
  print("\niterations submenu")

def keep_submenu():
  print("\nkeep submenu")

def nopsled_submenu():
  print("\nnopsled submenu")

def out_submenu():
  print("\nout submenu")

def payload_submenu():
  print("\npayload submenu")

def platform_submenu():
  print("\nplatform submenu")

def sec_name_submenu():
  print("\nsec-name submenu")

def service_name_submenu():
  print("\nservice-name submenu")

def smallest_submenu():
  print("\nsmallest submenu")

def space_submenu():
  print("\nspace submenu")

def template_submenu():
  print("\ntemplate submenu")

def timeout_submenu():
  print("\ntimeout submenu")

def var_name_submenu():
  print("\nvar-name submenu")

def main():

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

  print("splash page code")

  for submenu in submenus:
    globals()[submenu + "_value"] = ""
  
  while selection != "q":
    print("\nmain menu code")
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
