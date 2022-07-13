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
  architectures_str = ''
  platforms_str = ''

  if payloads_value:    
    payload_str = f"msfvenom -p {payloads_value} "
    if add_code_value:
      add_code_str = f"-c {add_code_value} "
    if platforms_value:
      platforms_str = f"--platform {platforms_value} "
    if architectures_value:
      architectures_str = f"--arch {architectures_value} "
    if bad_chars_value:
        bad_chars_str = f"-b {bad_chars_value} "
    if encoder_space_value:
        encoder_space_str = f"--encoder-space {encoder_space_value} "
    if encoding_value:
        encoding_str = f"--encoder {encoding_value} "
    if encrypt_iv_value:
        encrypt_iv_str = f"--encrypt-iv {encrypt_iv_value} "
    if encrypt_key_value:
        encrypt_key_str = f"--encrypt-key {encrypt_key_value} "
    if encrypt_value:
        encrypt_str = f"--encrypt {encrypt_value} "
    if formats_value:
        formats_str = f"-f {formats_value} "
    if iterations_value:
        iterations_str = f"-i {iterations_value} "
    if keep_value:
        keep_str = f"--keep "
    if lhost_value:
        lhost_str = f"LHOST={lhost_value} "
    if lport_value:
        lport_str = f"LPORT={lport_value} "
    if nopsled_value:
        nopsled_str = f"--nopsled {nopsled_value} "
    if pad_nops_value:
        pad_nops_str = f"--pad-nops "
    if rhost_value:
        rhost_str = f"RHOST={rhost_value} "
    if rport_value:
        rport_str = f"RPORT={rport_value} "
    if sec_name_value:
        sec_name_str = f"--sec-name {sec_name_value} "
    if service_name_value:
        service_name_str = f"--service-name {service_name_value} "
    if smallest_value:
        smallest_str = f"--smallest "
    if space_value:
        space_str = f"--space {space_value} "
    if template_value:
        template_str = f"-x {template_value} "
    if var_name_value:
        var_name_str = f"-v {var_name_value} "


    file_name = input("Enter a file name: ")
    file_name_str = f"-o {file_name}"

    cmd = f"{payload_str}{platforms_str}{architectures_str}{lhost_str}{lport_str}{rhost_str}{rport_str}{add_code_str}{bad_chars_str}{encoder_space_str}{encoding_str}{encrypt_iv_str}{encrypt_key_str}{encrypt_str}{formats_str}{iterations_str}{keep_str}{nopsled_str}{pad_nops_str}{sec_name_str}{service_name_str}{smallest_str}{space_str}{template_str}{var_name_str}{file_name_str}"
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