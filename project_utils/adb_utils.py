import os
import subprocess


KNOWN_ADB_DEVICE_IP_D = {'WIRED'    : '9889ba33444758574e',
                         'WIRELESS' :'192.168.0.9:5555'}

NON_IP_STR_L = ["b'List of devices attached", 'r','tdevice', 'n', 'n"', "n'", 
                "nadb server version (40) doesn't match this client (36); killing...",
                'n* daemon not running. starting it now on port 5037 *', 'n* daemon started successfully *']




def get_adb_device_l():
    device_l = []
    devices_output_str = subprocess.check_output('adb devices', shell=True)#os.system('adb devices')
    split_devices_output_str = str(devices_output_str).split('\\')
    
    for st in split_devices_output_str:
        if st not in NON_IP_STR_L:
#             device_l.append(st)
            device_l.append(st[1:]) #remove 'n' from in front of IPs
    return device_l
    
    



def init_adb(print_device_ip_name = True):
    adb_device_ip = None

    # get list of connected devices
#     # if you already ran adb somewhere else without killing, kill it then try again
#     while(True):
#         devices_output_str = subprocess.check_output('adb devices', shell=True)#os.system('adb devices')
#         if devices_output_str != "adb server version (36) doesn't match this client (40); killing...":
#             print('breaking because this is a good result from adb devices:  ', devices_output_str)#````````````````````````````````
#             break
#         print("trying again after:  adb server version (36) doesn't match this client (40); killing...")
#             
        
#     devices_output_str = subprocess.check_output('adb devices', shell=True)#os.system('adb devices')
#         
#     split_devices_output_str = str(devices_output_str).split('\\')
#     
#     #['b"List of devices attached', 'r', 'r', 'n* daemon started successfully *', 'r', 'n9889ba33444758574e', 'tdevice', 'r', 'n', 'r', 'n"']
#     if (split_devices_output_str[2] == "nadb server version (40) doesn't match this client (36); killing..."):
#         split_devices_output_str.pop(2)
#         split_devices_output_str.pop(3)
#         split_devices_output_str.pop(4)
# #         split_devices_output_str.pop(5)
# #         split_devices_output_str.pop(6)
#     print('split_devices_output_str:  ', split_devices_output_str)
    
    devices_l = get_adb_device_l()  # ["b'List of devices attached", 'r', 'n9889ba33444758574e', 'tdevice', 'r', 'n192.168.0.9:5555', 'tdevice', 'r', 'n', 'r', "n'"]
#     str_num = 2
# 
#     while(str_num < len(split_devices_output_str) - 3):
#         device_ip_str = split_devices_output_str[str_num]
#         devices_l.append(device_ip_str[1:]) #remove 'n' from in front of IPs
#         str_num += 3    
    
    
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





#if multiple devices:  adb -s 192.168.0.15  pull /sdcard/sc.png
def adb_screenshot(screenshot_filename, adb_device_ip):
    subprocess.check_output("adb -s " + adb_device_ip + " shell screencap -p /sdcard/" + screenshot_filename)
    subprocess.check_output("adb -s " + adb_device_ip + " pull /sdcard/" + screenshot_filename)# + ' >C:/Users/Brandon/Documents/Personal_Projects/HQ_hack/project_utils') 
#     image = cv2.imread(screenshot_filename)
#     image.show()




if __name__ == '__main__':
    import extract_text
    print ('running...')
    extract_text.test_alignment()
