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


def get_current_img_num_d():
    cur_img_num_d = {'question': 0,
                     'options'  :0}
    
    question_img_filenames = filenames_in_dir(QUESTION_TRAINING_PICS_PATH)
    option_img_filenames   = filenames_in_dir(OPTIONS_TRAINING_PICS_PATH) 
    
    
    try:
        cur_img_num_d['question'] = int ( question_img_filenames[0].split('.')[0].split('_')[-1] )
    except:
        pass
    try:
        cur_img_num_d['option']   = int ( option_img_filenames  [0].split('.')[0].split('_')[-1] )
    except:
        pass
    
    return cur_img_num_d
    
def main():
#     onlyfiles = [f for f in listdir(QUESTION_TRAINING_PICS_PATH) if isfile(join(QUESTION_TRAINING_PICS_PATH, f))]
#     print(onlyfiles)
    
    print(filenames_in_dir(OPTIONS_TRAINING_PICS_PATH))
    
    cur_img_num_d = get_current_img_num_d()
    print(cur_img_num_d)
    
    
    qo_dict = { 'question': '', 
                'option_1': '',
                'option_2': '',
                'option_3': ''  }
           
    run_grab_screen_and_extract_text_threads(qo_dict)
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
    
