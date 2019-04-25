import os


#if multiple devices:  adb -s 192.168.0.15  pull /sdcard/sc.png
def adb_screenshot(screenshot_filename):
    os.system("adb shell screencap -p /sdcard/" + screenshot_filename)
    os.system("adb pull /sdcard/" + screenshot_filename + ' >C:/Users/Brandon/Documents/Personal_Projects/HQ_hack/project_utils') 
#     image = cv2.imread(screenshot_filename)
#     image.show()


def init_adb():
#     os.system('adb devices')
    os.system("adb connect 192.168.0.9:5555")
    
    #     os.system("adb kill-server")
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
