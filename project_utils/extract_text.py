#for some reason OCR works a lot better when you get a different screenshot for the question and each option


import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from PIL import Image
import pytesseract
import argparse
import cv2
import pyscreenshot as Imagegrab
from threading import Thread


from project_utils import testing_utils
from project_utils import adb_utils

# sys.path.insert(0, 'adb')
# import adb_utils


import time #just for testing

#                           |
#                           V
#                           y1
#                    --> x1   x2 -->
#                           y2
#                           |
#                           V
#     
#                     x1  y1  x2  y2
yo = 80
# xo = 30
q_x_start = 90
q_y_start = 500
q_width   = 900
q_hight   = 300

o_x_start   = 160
o_1_y_start = 985
o_width     = 820
o_hight     = 65

o_y_offset  = 190

QUESTION_SC_COORDS = (q_x_start,    q_y_start,                       q_x_start + q_width,    q_y_start   + q_hight)
OPTION_1_SC_COORDS = (o_x_start,    o_1_y_start,                     o_x_start + o_width,    o_1_y_start + o_hight)
OPTION_2_SC_COORDS = (o_x_start,    o_1_y_start +  o_y_offset,       o_x_start + o_width,    o_1_y_start + o_hight +  o_y_offset)
OPTION_3_SC_COORDS = (o_x_start,    o_1_y_start + (o_y_offset * 2),  o_x_start + o_width,    o_1_y_start + o_hight + (o_y_offset * 2))


# yo = 80
# # xo = 30
# QUESTION_SC_COORDS = (40,240,420,460)#(80,550,900,800)
# OPTION_1_SC_COORDS = (70,470,380,530)
# OPTION_2_SC_COORDS = (70,470+yo,380,530+yo)
# OPTION_3_SC_COORDS = (70,470+(yo*2),380,530+(yo*2))


QUESTION_IMG_PATH = 'question_temp.png'
OPTION_1_IMG_PATH = 'option_1_temp.png'
OPTION_2_IMG_PATH = 'option_2_temp.png'
OPTION_3_IMG_PATH = 'option_3_temp.png'

QO_IMG_PATH_LIST = [QUESTION_IMG_PATH,
                    OPTION_1_IMG_PATH,
                    OPTION_2_IMG_PATH,
                    OPTION_3_IMG_PATH]

BACKGROUND_IMG_DIMS = (1000, 1500)
BACKGROUND_IMG_COLOR = (5, 5, 5, 5)#(000, 153, 000, 5)

ADB_SCREENSHOT_FILENAME = 'screencap.png'

    
    
def crop_img(original_img, cropped_img_path, crop_coords):
#         img = Image.open(adb_screenshot_filename)
    cropped_img = original_img.crop(crop_coords)
#     cropped_img.show()
    cropped_img.save(cropped_img_path)
    



def crop_question_and_option_imgs(original_img, img_path_list = QO_IMG_PATH_LIST):
    crop_img(original_img,  img_path_list[0], QUESTION_SC_COORDS)
    crop_img(original_img,  img_path_list[1], OPTION_1_SC_COORDS)
    crop_img(original_img,  img_path_list[2], OPTION_2_SC_COORDS)
    crop_img(original_img,  img_path_list[3], OPTION_3_SC_COORDS)
    
    
def extract_text_and_add_to_qo_dict(cropped_img_path, qo_dict_key, qo_dict):
    qo_dict[qo_dict_key] = extract_text_from_image(cropped_img_path)
    
    
def run_extract_text_and_add_to_qo_dict_threads(qo_dict, img_path_list = QO_IMG_PATH_LIST):
    thread_list = []
       
    thread_list.append(Thread(target=extract_text_and_add_to_qo_dict, args=(img_path_list[0], 'question' , qo_dict)))
    thread_list.append(Thread(target=extract_text_and_add_to_qo_dict, args=(img_path_list[1], 'option_1' , qo_dict)))
    thread_list.append(Thread(target=extract_text_and_add_to_qo_dict, args=(img_path_list[2], 'option_2' , qo_dict)))
    thread_list.append(Thread(target=extract_text_and_add_to_qo_dict, args=(img_path_list[3], 'option_3' , qo_dict)))  
        
    for thread in thread_list:
        thread.start()
       
    for thread in thread_list:
        thread.join()
    

BAD_READ_SYM_CHARS_REPLACE_D = {'\n': ' ',
                                '|' : 'I'}

BAD_READ_HEX_CHARS_REPLACE_D = {'fb01': 'fi'}

def replace_bad_read_chars(text):
    for bad_chars, replacement_chars in BAD_READ_SYM_CHARS_REPLACE_D.items():
        if bad_chars in text:
            text = text.replace(bad_chars, replacement_chars)
            
    for char in text:
        hex_char = format(ord(char), "x")
#         print(hex_char)
#         print(hex(ord(char)), type(hex(ord(char))), hex(ord(char)) == '0xfb01', hex(ord(char)) in BAD_READ_HEX_CHARS_REPLACE_D.values())#``````````````````````````````````````````````````
        if format(ord(char), "x") in BAD_READ_HEX_CHARS_REPLACE_D.keys():
#             print('found bad hex char!!!!!!!!!!!!')#`````````````````````````````````````````````````````
            text = text.replace(char, BAD_READ_HEX_CHARS_REPLACE_D[hex_char])
            
    return text
    
    

def extract_text_from_image(img_path, lang = 'eng'):    
    image = cv2.imread(img_path)
#     cv2.imshow("Original", image)
    
    # Apply an "average" blur to the image
    
#     blurred = cv2.blur(image, (3,3))
# # #     cv2.imshow("Blurred_image", blurred)
#     img = Image.fromarray(blurred)

    text = pytesseract.image_to_string(image, lang)
    
    
    
    return replace_bad_read_chars(text)

# 
# #probably faster to give this func its own thread
# def grab_screen_and_extract_text(screenshot_coords, img_path, qo_dict_key, qo_dict):
#     grab_screen(screenshot_coords, img_path)
#     qo_dict[qo_dict_key] = extract_text_from_image(img_path) 
#     
# 
# 
# def run_grab_screen_and_extract_text_threads(qo_dict, img_path_list = QO_IMG_PATH_LIST):
#     thread_list = []
#        
#     thread_list.append(Thread(target=grab_screen_and_extract_text, args=(QUESTION_SC_COORDS, img_path_list[0], 'question' , qo_dict)))
#     thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_1_SC_COORDS, img_path_list[1], 'option_1' , qo_dict)))
#     thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_2_SC_COORDS, img_path_list[2], 'option_2' , qo_dict)))
#     thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_3_SC_COORDS, img_path_list[3], 'option_3' , qo_dict)))  
#         
#     for thread in thread_list:
#         thread.start()
#        
#     for thread in thread_list:
#         thread.join()



def delete_temp_files():
    for img_path in QO_IMG_PATH_LIST:
        try:
            os.remove(img_path)
        except:
            pass


def read_questions_and_options_from_screen(adb_device_ip):    
    qo_dict = { 'question': '', 
                'option_1': '',
                'option_2': '',
                'option_3': ''  }
           
#     run_grab_screen_and_extract_text_threads(qo_dict)


    adb_utils.adb_screenshot(ADB_SCREENSHOT_FILENAME, adb_device_ip)
    original_screenshot = Image.open(ADB_SCREENSHOT_FILENAME)
    crop_question_and_option_imgs(original_screenshot)
    run_extract_text_and_add_to_qo_dict_threads(qo_dict)


    delete_temp_files()
    
    print('in extract_text, qo_d: ', qo_dict)
#      
    return qo_dict






#runs a dummy version of read_questions_and_options_from_screen() and shows an image
#showing what it grabbed for the question and options, based on this, you can tell if you 
#need to move the phone window
def test_alignment():
    adb_device_ip = adb_utils.init_adb()
    print('adb done setting up')
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
    
    
    qo_dict = { 'question': '', 
                'option_1': '',
                'option_2': '',
                'option_3': ''  }
    
    start_time = time.time()    
    
    adb_utils.adb_screenshot(ADB_SCREENSHOT_FILENAME, adb_device_ip)
    print('screenshot time: ', time.time() - start_time)
     
     
    original_screenshot = Image.open(ADB_SCREENSHOT_FILENAME)
#     run_crop_img_and_extract_text_threads(original_screenshot, qo_dict)
    crop_question_and_option_imgs(original_screenshot)
    run_extract_text_and_add_to_qo_dict_threads(qo_dict)
     
    print('time to extract text: ', time.time() - start_time)
     
#     os.system("adb kill-server")
         
#     run_grab_screen_and_extract_text_threads(qo_dict)
     
     
    question_img = Image.open(QUESTION_IMG_PATH, 'r')
    option_1_img = Image.open(OPTION_1_IMG_PATH, 'r')
    option_2_img = Image.open(OPTION_2_IMG_PATH, 'r')
    option_3_img = Image.open(OPTION_3_IMG_PATH, 'r')
     
    img_w, img_h = question_img.size
    background = Image.new('RGBA', BACKGROUND_IMG_DIMS, BACKGROUND_IMG_COLOR)
    bg_w, bg_h = background.size
     
    question_img_offset = ((bg_w - img_w) // 2, ( bg_h - img_h) // 4)
    option_1_img_offset = ((bg_w - img_w) // 2, ((bg_h - img_h) // 4) * 2)
    option_2_img_offset = ((bg_w - img_w) // 2, ((bg_h - img_h) // 4) * 3)
    option_3_img_offset = ((bg_w - img_w) // 2, ((bg_h - img_h) // 4) * 4)
     
    background.paste(question_img, question_img_offset)
    background.paste(option_1_img, option_1_img_offset)
    background.paste(option_2_img, option_2_img_offset)
    background.paste(option_3_img, option_3_img_offset)
#     background.save('out.png')
    background.show()
     
     
    
    testing_utils.print_qo_d(qo_dict)
     
    delete_temp_files()
    return qo_dict
    

# https://superuser.com/questions/1395888/enable-adb-debugging-on-android-phone-with-broken-disabled-screen
# https://stackoverflow.com/questions/43050370/adb-server-version-36-doesnt-match-this-client-39-not-using-genymotion
#error: could not install *smartsocket* listener: cannot bind to 127.0.0.1:5037: Only one usage of each socket address (protocol/network address/port) is normally permitted. (10048)
if __name__ == '__main__':
    print ('running...')
    
    test_alignment()
    
#     
#     adb_screenshot(ADB_SCREENSHOT_FILENAME)
#     crop_question_and_options_from_adb_screenshot(ADB_SCREENSHOT_FILENAME)
#     
#     st = time.time()
#         
#     qo_d = read_questions_and_options_from_screen()
# #     qo_dict = test_alignment()
# #     print(qo_d)
# 
# 
#     testing_utils.print_str_wo_error(qo_d['question'])
# 
# #     print(qo_d['question'])
#     print(qo_d['option_1'])
#     print(qo_d['option_2'])
#     print(qo_d['option_3'])
# #     for char in qo_d['question']:
# #         print(char)
# 
#     
#     et = time.time()
#     print('total time: ', et - st)
#     print('done')
#     
