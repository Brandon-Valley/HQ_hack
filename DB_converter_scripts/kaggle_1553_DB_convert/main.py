#more data at https://twitter.com/HQTriviaScribe


import logger

import json


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
    
def no_answers_empty(q_d):
    for answer_d in q_d['answers']:
        if answer_d['text'] == '':
            return False
    return True
    
    
    
#get rid of questions that dont have answers, or correct answers q_d = question_dict
def trim_input_data_l(input_data_l):    
    trimmed_input_data_l = []
    for q_d in input_data_l:
#         print(len(q_d['answers']))
        if len(q_d['answers']) == 3 and no_answers_empty(q_d):
            trimmed_input_data_l.append(q_d)
#             print(len(q_d['answers']))
#             input_data_l.remove(q_d)
    return trimmed_input_data_l
            
            
def get_answer(answer_letter, in_d):
    for answer_d in in_d['answers']:
        if answer_d['choice'] == answer_letter:
            return answer_d['text']
            
            
def get_correct_letter(in_d):
    for answer_d in in_d['answers']:
        if answer_d['correct'] == True:
            return answer_d['choice']
            
            
#   timestamp    quest #    question    a    b    c    correct

def build_log_dl(input_data_l):
    log_dl = []
    
    for in_d in input_data_l:
        log_d = {'timestamp': in_d['timestamp'],
                 'question #': in_d['question_num'],
                 'question': in_d['question'],
                 'A': get_answer('A', in_d),
                 'B': get_answer('B', in_d),
                 'C': get_answer('C', in_d),
                 'correct': get_correct_letter(in_d)}
        log_dl.append(log_d)
    return log_dl




output_csv_filename = 'kaggle_1553_DB.csv'
header_list = ['timestamp', 'question #', 'question', 'A', 'B', 'C', 'correct']

with open('kaggle_1553_DB.json', 'r') as f:
    input_data_l = json.load(f)



trimmed_input_data_l = trim_input_data_l(input_data_l)
log_dl = build_log_dl(trimmed_input_data_l)
logger.logList(log_dl, output_csv_filename, wantBackup = True, headerList = header_list, overwriteAction = 'overwrite')

print('done!')
# print(log_dl)


# for distro in input_data_l:
#     print(distro['answers'][0])



# loaded_json = json.loads(json_data)
# for x in loaded_json:
#     print("%s: %d" % (x, loaded_json[x]))
    
    
    
    
    
    
    