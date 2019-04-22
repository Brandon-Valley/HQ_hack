# import subprocess
# subprocess.call(['ls','-l']) #all that is technically needed...
# subprocess.check_output(['adb', 'shell', 'screencap', '-p', '/sdcard/screencap.png'])


import os
 
 
os.system("adb shell screencap -p /sdcard/screencap.png")
os.system("adb pull /sdcard/screencap.png")