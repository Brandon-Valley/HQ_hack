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


import time #just for testing

#                           |
#                           V
#                           y1
#                    --> x1   x2 -->
#                           y2
#                           |
#                           V
#(31,228,455,710)     
#                     x1  y1  x2  y2
yo = 80
# xo = 30
QUESTION_SC_COORDS = (40,240,420,460)
OPTION_1_SC_COORDS = (70,470,380,530)
OPTION_2_SC_COORDS = (70,470+yo,380,530+yo)
OPTION_3_SC_COORDS = (70,470+(yo*2),380,530+(yo*2))

QUESTION_IMG_PATH = 'question_temp.png'
OPTION_1_IMG_PATH = 'option_1_temp.png'
OPTION_2_IMG_PATH = 'option_2_temp.png'
OPTION_3_IMG_PATH = 'option_3_temp.png'

QO_IMG_PATH_LIST = [QUESTION_IMG_PATH,
                    OPTION_1_IMG_PATH,
                    OPTION_2_IMG_PATH,
                    OPTION_3_IMG_PATH]

BACKGROUND_IMG_DIMS = (500, 1200)
BACKGROUND_IMG_COLOR = (5, 5, 5, 5)#(000, 153, 000, 5)

ADB_SCREENSHOT_FILENAME = 'screencap.png'




# def crop_question_and_options_from_adb_screenshot(adb_screenshot_filename):
#     
#     img = Image.open(adb_screenshot_filename)
#     cropped_img = img.crop((80,550,900,800))
#     cropped_img.show()




    
    
def crop_img(original_img, cropped_img_path, crop_coords):
#         img = Image.open(adb_screenshot_filename)
    cropped_img = original_img.crop(crop_coords)
#     cropped_img.show()
    cropped_img.save(cropped_img_path)
    

def adb_screenshot(screenshot_filename):
    os.system("adb shell screencap -p /sdcard/" + screenshot_filename)
    os.system("adb pull /sdcard/" + screenshot_filename)
#     image = cv2.imread(screenshot_filename)
#     image.show()


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
    
    
    
def run_extract_text_threads(original_img, qo_dict, img_path_list = QO_IMG_PATH_LIST):
    crop_img_and_extract_text(original_img, QUESTION_SC_COORDS, img_path_list[0], 'question' , qo_dict)
    crop_img_and_extract_text(original_img, OPTION_1_SC_COORDS, img_path_list[1], 'option_1' , qo_dict)
    crop_img_and_extract_text(original_img, OPTION_2_SC_COORDS, img_path_list[2], 'option_2' , qo_dict)
    crop_img_and_extract_text(original_img, OPTION_3_SC_COORDS, img_path_list[3], 'option_3' , qo_dict)


def crop_img_and_extract_text(original_img, crop_coords, cropped_img_path, qo_dict_key, qo_dict):
    crop_img(original_img, cropped_img_path, crop_coords)
    qo_dict[qo_dict_key] = extract_text_from_image(cropped_img_path)
    
    

def run_crop_img_and_extract_text_threads(original_img, qo_dict, img_path_list = QO_IMG_PATH_LIST):
    crop_img_and_extract_text(original_img, QUESTION_SC_COORDS, img_path_list[0], 'question' , qo_dict)
    crop_img_and_extract_text(original_img, OPTION_1_SC_COORDS, img_path_list[1], 'option_1' , qo_dict)
    crop_img_and_extract_text(original_img, OPTION_2_SC_COORDS, img_path_list[2], 'option_2' , qo_dict)
    crop_img_and_extract_text(original_img, OPTION_3_SC_COORDS, img_path_list[3], 'option_3' , qo_dict)
    
    
#     
#     thread_list = []
#        
#     thread_list.append(Thread(target=crop_img_and_extract_text, args=(original_img, QUESTION_SC_COORDS, img_path_list[0], 'question' , qo_dict)))
# #     thread_list.append(Thread(target=crop_img_and_extract_text, args=(original_img, OPTION_1_SC_COORDS, img_path_list[1], 'option_1' , qo_dict)))
# #     thread_list.append(Thread(target=crop_img_and_extract_text, args=(original_img, OPTION_2_SC_COORDS, img_path_list[2], 'option_2' , qo_dict)))
# #     thread_list.append(Thread(target=crop_img_and_extract_text, args=(original_img, OPTION_3_SC_COORDS, img_path_list[3], 'option_3' , qo_dict)))  
# #         
#     for thread in thread_list:
#         thread.start()
#        
#     for thread in thread_list:
#         thread.join()




def grab_screen(screenshot_cords, save_path):
    im = Imagegrab.grab(bbox=screenshot_cords) #im = Imagegrab.grab(bbox=(31,228,485,640))
    im.save(save_path)
#

def extract_text_from_image(img_path, lang = 'eng'):    
    image = cv2.imread(img_path)
#     cv2.imshow("Original", image)
    
    # Apply an "average" blur to the image
    
#     blurred = cv2.blur(image, (3,3))
# # #     cv2.imshow("Blurred_image", blurred)
#     img = Image.fromarray(blurred)

    text = pytesseract.image_to_string(image, lang)
    
    return text


#probably faster to give this func its own thread
def grab_screen_and_extract_text(screenshot_coords, img_path, qo_dict_key, qo_dict):
    grab_screen(screenshot_coords, img_path)
    qo_dict[qo_dict_key] = extract_text_from_image(img_path) 
    


def run_grab_screen_and_extract_text_threads(qo_dict, img_path_list = QO_IMG_PATH_LIST):
    thread_list = []
       
    thread_list.append(Thread(target=grab_screen_and_extract_text, args=(QUESTION_SC_COORDS, img_path_list[0], 'question' , qo_dict)))
    thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_1_SC_COORDS, img_path_list[1], 'option_1' , qo_dict)))
    thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_2_SC_COORDS, img_path_list[2], 'option_2' , qo_dict)))
    thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_3_SC_COORDS, img_path_list[3], 'option_3' , qo_dict)))  
        
    for thread in thread_list:
        thread.start()
       
    for thread in thread_list:
        thread.join()



def delete_temp_files():
    for img_path in QO_IMG_PATH_LIST:
        try:
            os.remove(img_path)
        except:
            pass


def read_questions_and_options_from_screen():    
    qo_dict = { 'question': '', 
                'option_1': '',
                'option_2': '',
                'option_3': ''  }
           
    run_grab_screen_and_extract_text_threads(qo_dict)

    delete_temp_files()
#      
    return qo_dict



#runs a dummy version of read_questions_and_options_from_screen() and shows an image
#showing what it grabbed for the question and options, based on this, you can tell if you 
#need to move the phone window
def test_alignment():
    qo_dict = { 'question': '', 
                'option_1': '',
                'option_2': '',
                'option_3': ''  }
    
    
#     adb_screenshot(ADB_SCREENSHOT_FILENAME)#put back in !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    original_screenshot = Image.open(ADB_SCREENSHOT_FILENAME)
#     run_crop_img_and_extract_text_threads(original_screenshot, qo_dict)
    crop_question_and_option_imgs(original_screenshot)
    run_extract_text_and_add_to_qo_dict_threads(qo_dict)
        
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
    
    # run threads to extract text from images
#     thread_list = []
#        
#     thread_list.append(Thread(target=extract_text_from_image, args=(QUESTION_IMG_PATH, 'question', qo_dict)))
#     thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_1_SC_COORDS, OPTION_1_IMG_PATH, 'options' , qo_dict)))
#     thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_2_SC_COORDS, OPTION_2_IMG_PATH, 'options' , qo_dict)))
#     thread_list.append(Thread(target=grab_screen_and_extract_text, args=(OPTION_3_SC_COORDS, OPTION_3_IMG_PATH, 'options' , qo_dict)))  
#         
#     for thread in thread_list:
#         thread.start()
#        
#     for thread in thread_list:
#         thread.join()
    
    
    
    delete_temp_files()
    
    
    return qo_dict
    




if __name__ == '__main__':
    print ('running...')
    
    test_alignment()
    
    
    adb_screenshot(ADB_SCREENSHOT_FILENAME)
    crop_question_and_options_from_adb_screenshot(ADB_SCREENSHOT_FILENAME)
    
    st = time.time()
        
    qo_d = read_questions_and_options_from_screen()
#     qo_dict = test_alignment()
#     print(qo_d)


    testing_utils.print_str_wo_error(qo_d['question'])

#     print(qo_d['question'])
    print(qo_d['option_1'])
    print(qo_d['option_2'])
    print(qo_d['option_3'])
#     for char in qo_d['question']:
#         print(char)

    
    et = time.time()
    print('total time: ', et - st)
    print('done')
    
