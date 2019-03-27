import logger

import json


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
    
    
#get rid of questions that dont have answers, q_d = question_dict
def trimmed_input_data_d(raw_input_data_d):    
    for q_d in raw_input_data_d:
        if len(q_d['answers']) == 0:
            raw_input_data_d.remove(q_d)
    return raw_input_data_d
            
    
# input_file_path = 'kaggle_1553_DB.json'
    
# raw_input = read_text_file(input_file_path)

with open('kaggle_1553_DB.json', 'r') as f:
    raw_input_data_d = json.load(f)

# for distro in distros_dict:
#     print(distro['answers'][0])


trimmed_input_data_d(raw_input_data_d)



for distro in raw_input_data_d:
    print(distro['answers'][0])



# loaded_json = json.loads(json_data)
# for x in loaded_json:
#     print("%s: %d" % (x, loaded_json[x]))
    
    
    
    
    
    
    