import os
import subprocess


WIRED_PHONE_IP = 'n9889ba33444758574e'
WIRELESS_PHONE_IP = 'n192.168.0.9:5555'



#if multiple devices:  adb -s 192.168.0.15  pull /sdcard/sc.png
def adb_screenshot(screenshot_filename):
    os.system("adb -s 9889ba33444758574e shell screencap -p /sdcard/" + screenshot_filename)
    os.system("adb -s 9889ba33444758574e pull /sdcard/" + screenshot_filename)# + ' >C:/Users/Brandon/Documents/Personal_Projects/HQ_hack/project_utils') 
#     image = cv2.imread(screenshot_filename)
#     image.show()


def init_adb():
#     os.system("adb kill-server")

    # get list of connected devices
    devices_output_str = subprocess.check_output('adb devices', shell=True)#os.system('adb devices')
    split_devices_output_str = str(devices_output_str).split('\\')
    
    # ["b'List of devices attached", 'r', 'n9889ba33444758574e', 'tdevice', 'r', 'n192.168.0.9:5555', 'tdevice', 'r', 'n', 'r', "n'"]
    devices_l = []
    str_num = 2
    if True: #check if device list empty #finish this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        while(str_num < len(split_devices_output_str) - 3):
            devices_l.append(split_devices_output_str[str_num])
            str_num += 3    
    
    # if wired and wireless IP available, default to wired
    if WIRED_PHONE_IP in devices_l and WIRELESS_PHONE_IP in devices_l :
        os.system("adb connect " + WIRED_PHONE_IP)
    
    
    
    
    
#     print(split_devices_output_str)
    print(devices_l)
#     os.system("adb connect 192.168.0.9:5555")
    
    #     
#     
#     os.system('adb devices')
#     # for wireless adb
#     os.system("adb connect 192.168.0.9:5555")
    
    # for wired adb
#     os.system("adb disconnect 192.168.0.9:5555")
    
    
#     os.system("adb connect 9889ba33444758574e:5037")
    
#     os.system('adb devices')
#     os.system("adb disconnect 192.168.0.9:5555")
#     os.system("adb connect 9889ba33444758574e")

# init_adb()






if __name__ == '__main__':
    import extract_text
    print ('running...')
    extract_text.test_alignment()
