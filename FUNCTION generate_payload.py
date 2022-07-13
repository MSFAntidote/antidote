def generate_payload():

  add_code_str = ''
  bad_chars_str = ''  
  encoder_space_str = ''  
  encoding_str = ''
  encrypt_iv_str = ''
  encrypt_key_str = ''
  encrypt_str = ''
  formats_str = ''
  iterations_str = ''
  keep_str = ''
  lhost_str = ''
  lport_str = ''
  nopsled_str = ''
  pad_nops_str = ''
  rhost_str = ''
  rport_str = ''
  sec_name_str = ''
  service_name_str = ''
  smallest_str = ''
  space_str = ''
  template_str = ''
  var_name_str = ''

  if payloads_value:    
    payload_str = f"msfvenom -p {payloads_value} "
    if add_code_value:
        add_code_str = f"-c {add_code_value} "
    elif bad_chars_value:
        bad_chars_str = f"-b {bad_chars_value} "
    elif encoder_space_value:
        encoder_space_str = f"--encoder-space {encoder_space_value} "
    elif encoding_value:
        encoding_str = f"--encoder {encoding_value} "
    elif encrypt_iv_value:
        encrypt_iv_str = f"--encrypt-iv {encrypt_iv_value} "
    elif encrypt_key_value:
        encrypt_key_str = f"--encrypt-key {encrypt_key_value} "
    elif encrypt_value:
        encrypt_str = f"--encrypt {encrypt_value} "
    elif formats_value:
        formats_str = f"-f {formats_value} "
    elif iterations_value:
        iterations_str = f"-i {iterations_value} "
    elif keep_value:
        keep_str = f"--keep "
    elif lhost_value:
        lhost_str = f"LHOST={lhost_value} "
    elif lport_value:
        lport_str = f"LPORT={lport_value} "
    elif nopsled_value:
        nopsled_str = f"--nopsled {nopsled_value} "
    elif pad_nops_value:
        pad_nops_str = f"--pad-nops "
    elif rhost_value:
        rhost_str = f"RHOST={rhost_value} "
    elif rport_value:
        rport_str = f"RPORT={rport_value} "
    elif sec_name_value:
        sec_name_str = f"--sec-name {sec_name_value} "
    elif service_name_value:
        service_name_str = f"--service-name {service_name_value} "
    elif smallest_value:
        smallest_str = f"--smallest "
    elif space_value:
        space_str = f"--space {space_value} "
    elif template_value:
        template_str = f"-x {template_value} "
    elif var_name_value:
        var_name_str = f"-v {var_name_value} "

    file_name = input("Enter a file name: ")
    file_name_str = f"-o {file_name}"

    cmd = f"{payload_str}{lhost_str}{lport_str}{rhost_str}{rport_str}{add_code_str}{bad_chars_str}{encoder_space_str}{encoding_str}{encrypt_iv_str}{encrypt_key_str}{encrypt_str}{formats_str}{iterations_str}{keep_str}{nopsled_str}{pad_nops_str}{sec_name_str}{service_name_str}{smallest_str}{space_str}{template_str}{var_name_str}{file_name_str}"
    print(f"\n{cmd}")
    agree = input("\nWould you like to generate this payload?  (y/n): ")

    if agree.lower() == 'y':    
        print("\nGenerating payload. Please wait...")
        os.system(f'{cmd}')
    elif agree.lower() == 'n':
        clear_selections()
    else:
        print("\nWrong input.  Please select 'y' or 'n'")
  else:
    print("\nNo payload specified. Please select a payload.")