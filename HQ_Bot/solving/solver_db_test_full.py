# to be able to import from parent dir
import sys
parent_dir_path = ''
parent_dir_path_list = sys.path[0].split('\\')[0:-1]
for dir in parent_dir_path_list:
    parent_dir_path += dir + '\\'
parent_dir_path = parent_dir_path[0:-1]
sys.path.append(parent_dir_path)

# from parent dir
import logger 
import utils

import solver_select
import solver_utils
import phantom_js_browser

import time
import os





# solver ideas
# -  if question contains the word 'phrase' and has a quoted phrase, google 'qusetion + phrases.org.uk" and search occurances
#    - would only apply to 0.011% 



# interesting questions:
# 10 - the quote is by john but is also the name of a book by hemmingway, maybe quara search?
#      - maybe search for popular phrase, 2nd article or question:  https://www.phrases.org.uk/meanings/for-whom-the-bell-tolls.html




SOLVED_DB_HEADER_LIST = ['timestamp', 'question #', 'question', 'A', 'B', 'C', 'correct', 'wrong', 'tryed_to_solve', 'right', 'time' ]

DB_CSV_PATH = 'test_db.csv'#"C:\\Users\\Brandon\\Documents\\Personal_Projects\\HQ_hack\\HQ_qo_database.csv"
KEYWORDS_CSV_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\HQ_hack\\HQ_Bot\\keywords.csv"

SOLVED_DB_CSV_PATH = 'solved_db.csv'

start_time = time.time()

try:
    os.remove(SOLVED_DB_CSV_PATH)
except:
    print('making new solved db csv...')

br = phantom_js_browser.Browser()
keywords_d = utils.get_keywords_d_from_csv(KEYWORDS_CSV_PATH)



db_dl = logger.readCSV(DB_CSV_PATH)
# print(db_dl)
print('num lines to solve: ', len(db_dl) - 2)

correct_answer_total = 0
wrong_answer_total   = 0
no_try_total         = 0
solver_times         = []

line_cnt = 0
for line_d in db_dl:
    question       = line_d['question']
    options       = [line_d['A'],
                     line_d['B'],
                     line_d['C']]
    correct_answer = line_d['correct']


    if line_cnt != 0 and line_cnt % 180 == 0:
        print ('sleeping...')
        time.sleep(30)

    solver_start_time = time.time()
    
    solved_output_d = solver_select.solve(question, options, keywords_d, br)
    
    solver_end_time = time.time()    
    solver_time = solver_end_time - solver_start_time
    solver_times.append(solver_time)
    
    
    tryed_to_solve = '' # empty box if it did try to solve
    if solved_output_d['answer'] == None:
        tryed_to_solve = 'NO_TRY'
        no_try_total += 1
        
    wrong = ''
    right = ''
    if solved_output_d['answer'] != None:
        if solved_output_d['answer'] == correct_answer:
            right = 'RIGHT'
            correct_answer_total += 1
        else:
            wrong = 'WRONG'
            wrong_answer_total += 1
        

    line_d['right'] = right
    line_d['wrong'] = wrong
    line_d['tryed_to_solve'] = tryed_to_solve
    line_d['time'] = solver_time
    
    logger.logSingle(line_d, SOLVED_DB_CSV_PATH, wantBackup = False, headerList = SOLVED_DB_HEADER_LIST, overwriteAction = 'append')
    
    print('solved line:  %s,   time = %s' %(line_cnt + 2, solver_time))#`````````````````````````````````````````````````````````````````````````
    line_cnt += 1
    
    
# urllib.error.HTTPError: HTTP Error 503: Service Unavailable
    
    
# for dict in db_dl:
#     print('tryed_to_solve: ', dict['tryed_to_solve'])
    
# logger.logList(db_dl, SOLVED_DB_CSV_PATH, wantBackup = False, headerList = SOLVED_DB_HEADER_LIST, overwriteAction = 'overwrite')
    

result_percent_l = solver_utils.num_occurrence_percent_l([correct_answer_total, wrong_answer_total, no_try_total])
print('correct: ', result_percent_l[0] * 100)
print('wrong:   ', result_percent_l[1] * 100)
print('no_try:  ', result_percent_l[2] * 100)

end_time = time.time()
print('total_time: ', end_time - start_time)

print('avg solver time: ', sum(solver_times) / len(solver_times))

br.end()
print('done!')


# solver_output_l = solver_select.get_solver_output_l(question, options, keywords_d)


#show output of test
# print('question:  ', question)
# print('')
# print('option_1:  ', options[0])
# print('option_2:  ', options[1])
# print('option_3:  ', options[2])
# print('')
# 
# 
# for solver_output in solver_output_l: #````````````````````````````````````````````````````````````````````
#     solver_output.print_me()



















