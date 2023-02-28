import elftools
from elftools.elf.elffile import ELFFile
from importlib import reload

# https://stackoverflow.com/questions/1250103/attributeerror-module-object-has-no-attribute
reload(elftools)
import capstone

# reading the ELF file
with open('elf-Linux-x86-bash', 'rb') as f:
    elffile = ELFFile(f)

    # Going through all sections of ELF File
    # inspired by https://medium.com/analytics-vidhya/exploring-elf-files-using-pyelftools-93bb7665cce3
    for section in elffile.iter_sections():

        # Disessemble the executable code
        if section['sh_flags'] & 4:  # Use integer value of SHF_EXECINSTR flag
            # Read the section contents and set the starting address
            code = section.data()
            address = section['sh_addr']

            # Make sure the ELF matches the correct Arch from the python library
            if elffile['e_machine'] == 'EM_X86_64':
                md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
            elif elffile['e_machine'] == 'EM_386':
                md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
            else:
                print("Unsupported architecture")
                continue  # https://www.geeksforgeeks.org/break-continue-and-pass-in-python/
                # when to use break vs continue

            # Disassemble each instruction in the section and print the result
            for x in md.disasm(code, address):
                print(f"0x{x.address:x}: {x.mnemonic} {x.op_str}")
