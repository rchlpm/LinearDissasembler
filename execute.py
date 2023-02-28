import pefile as pefile

exe_file_path = '/Users/rachel/Desktop/Copmuter Arch/ModelSimSetup-20.1.1.720-windows.exe'

try:
    # parse exe file
    exe = pefile.PE(exe_file_path)
    try:
        # call the function we created earlier
        pefile(exe)
    except:
        print('something is wrong with this exe file')
except:
    print('pefile cannot parse this file')
