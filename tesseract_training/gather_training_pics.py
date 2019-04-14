# to ba able to import from parent dir
import sys
parent_dir_path = ''
parent_dir_path_list = sys.path[0].split('\\')[0:-1]
for dir in parent_dir_path_list:
    parent_dir_path += dir + '\\'  
# parent_dir_path = parent_dir_path[0:-1]
sys.path.append(parent_dir_path[0:-1])


from os import listdir
from os.path import isfile, join






from project_utils import extract_text # from parent dir




QUESTION_TRAINING_PICS_PATH = 'training_pics\\questions'
OPTIONS_TRAINING_PICS_PATH  = 'training_pics\\options'


def filenames_in_dir(dir_path):
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]


def get_current_img_nums():
    cur_question_img_num = 0
    cur_option_img_num   = 0
    
    question_img_filenames = filenames_in_dir(QUESTION_TRAINING_PICS_PATH)
    option_img_filenames   = filenames_in_dir(OPTIONS_TRAINING_PICS_PATH) 
    try:
        cur_question_img_num = int ( question_img_filenames[0].split('.')[0].split('_')[-1] )
    except:
        pass
    try:
        cur_question_img_num   = int ( option_img_filenames  [0].split('.')[0].split('_')[-1] )
    except:
        pass
    
    return cur_question_img_num, cur_option_img_num
    
def main():
#     onlyfiles = [f for f in listdir(QUESTION_TRAINING_PICS_PATH) if isfile(join(QUESTION_TRAINING_PICS_PATH, f))]
#     print(onlyfiles)
    
    print(filenames_in_dir(OPTIONS_TRAINING_PICS_PATH))
    
    cur_question_img_num, cur_options_img_num = get_current_img_nums()
    
#     print(cur_options_img_num)
#     print(cur_img_num_d)
    qo_dict = { 'question': '', 
                'option_1': '',
                'option_2': '',
                'option_3': ''  }
   
    while(True):
    
        user_input = input('q to quit, anything else to continue:  ')
       
        if user_input == 'q':
            break
        
        # [language name].[font name].exp[number].[file extension]
        qo_img_path_list = [QUESTION_TRAINING_PICS_PATH + '\\eng.HQ_Question_Font.exp' + str(cur_question_img_num + 1) + '.png',
                            OPTIONS_TRAINING_PICS_PATH  + '\\eng.HQ_Options_Font.exp'  + str(cur_options_img_num + 1)  + '.png',
                            OPTIONS_TRAINING_PICS_PATH  + '\\eng.HQ_Options_Font.exp'  + str(cur_options_img_num + 2)  + '.png',
                            OPTIONS_TRAINING_PICS_PATH  + '\\eng.HQ_Options_Font.exp'  + str(cur_options_img_num + 3)  + '.png',]
        cur_question_img_num += 1
        cur_options_img_num  += 3

        
        print('running...')    
        extract_text.run_grab_screen_and_extract_text_threads(qo_dict, qo_img_path_list)
        
    #     print(qo_dict)
    
    
    
    
    
if __name__ == "__main__":
    main()
    print('done!')
    
