import os
import subprocess


# KNOWN_ADB_DEVICE_IP_D['WIRED'] = '9889ba33444758574e'
# KNOWN_ADB_DEVICE_IP_D['WIRELESS'] = '192.168.0.9:5555'

KNOWN_ADB_DEVICE_IP_D = {'WIRED'    : '9889ba33444758574e',
                         'WIRELESS' :'192.168.0.9:5555'}



#if multiple devices:  adb -s 192.168.0.15  pull /sdcard/sc.png
def adb_screenshot(screenshot_filename, adb_device_ip):
    os.system("adb -s " + adb_device_ip + " shell screencap -p /sdcard/" + screenshot_filename)
    os.system("adb -s " + adb_device_ip + " pull /sdcard/" + screenshot_filename)# + ' >C:/Users/Brandon/Documents/Personal_Projects/HQ_hack/project_utils') 
#     image = cv2.imread(screenshot_filename)
#     image.show()


def init_adb(print_device_ip_name = True):
    adb_device_ip = None

    # get list of connected devices
    devices_output_str = subprocess.check_output('adb devices', shell=True)#os.system('adb devices')
    split_devices_output_str = str(devices_output_str).split('\\')
    
    devices_l = []  # ["b'List of devices attached", 'r', 'n9889ba33444758574e', 'tdevice', 'r', 'n192.168.0.9:5555', 'tdevice', 'r', 'n', 'r', "n'"]
    str_num = 2

    while(str_num < len(split_devices_output_str) - 3):
        device_ip_str = split_devices_output_str[str_num]
        devices_l.append(device_ip_str[1:]) #remove 'n' from in front of IPs
        str_num += 3    
    
    
        # set adb_device_ip
    if   len(devices_l) == 0:
        raise Exception('ERROR:  No ADB Devices Detected')
    elif   len(devices_l) == 1:
        adb_device_ip = devices_l[0]
    # if wired and wireless IP available, default to wired
    elif KNOWN_ADB_DEVICE_IP_D['WIRED'] in devices_l and KNOWN_ADB_DEVICE_IP_D['WIRELESS'] in devices_l :
        adb_device_ip = KNOWN_ADB_DEVICE_IP_D['WIRED']
    
    # check that adb_device_ip was set
    if adb_device_ip == None:
        raise Exception('ERROR:  adb_device_ip == None  -->  device IP not being chosen from devices_l: ', devices_l)

    
    #print device IP name
    if print_device_ip_name == True:
        ip_name = None
        for name, ip in KNOWN_ADB_DEVICE_IP_D.items():
            if ip == adb_device_ip:
                ip_name = name
                break
        if ip_name == None:
            print('connected to unkown ADB device IP: ', adb_device_ip)
        else:
            print('connected to ADB device IP: ', ip_name)


    return adb_device_ip






if __name__ == '__main__':
    import extract_text
    print ('running...')
    extract_text.test_alignment()
