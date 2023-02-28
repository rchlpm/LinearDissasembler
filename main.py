from capstone import *
from capstone.x86 import *


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main_code(sections, base):
    addresses = []
    # Use a breakpoint in the code line below to debug your script.
    for section in sections:
        addresses.append(section.VirtualAddress)

        # if the address of section corresponds to the first instruction then
        # this section should be the main code section
    if base in addresses:
        return sections[addresses.index(base)]
        # otherwise, sort addresses and look for the interval to which the base of code
        # belongs
    else:
        addresses.append(base)
        addresses.sort()
        if addresses.index(base) != 0:
            return sections[addresses.index(base) - 1]
        else:
            # this means we failed to locate it
            return None
    # Press ⌘F8 to toggle the breakpoint.



