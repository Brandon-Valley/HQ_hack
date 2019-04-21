# to be able to import from parent dir
import sys
import autocorrect
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


# - make score of accociation between whole question and wiki article, compare to wiki of all options
#     - maybe make the uncommoness of words found in wikis effect score ie: steam boat gives more points than ocean
#          -maybe also use thesurus in search, maybe use antonyms when there are neg words in question


#  - user google natural language to go after multi step, it can recognize when there is a description of a person, so you can
#    find that person, then use his name to do more saerches

# interesting questions:
# 10 - the quote is by john but is also the name of a book by hemmingway, maybe quara search?
#      - maybe search for popular phrase, 2nd article or question:  https://www.phrases.org.uk/meanings/for-whom-the-bell-tolls.html




def print_solved_csv_stats(solved_db_csv_path):
    solved_db_dl = logger.readCSV(solved_db_csv_path)
    
    correct_answer_total = 0
    wrong_answer_total   = 0
    no_try_total         = 0
    solver_times         = []
    
    for line_d in solved_db_dl:
        solver_times.append(float(line_d['time']))
        
        if   line_d['right'] != '':
            correct_answer_total += 1
        elif line_d['wrong'] != '':
            wrong_answer_total += 1
        if line_d['tryed_to_solve'] != '':
            no_try_total += 1
            
    result_percent_l = solver_utils.num_occurrence_percent_l([correct_answer_total, wrong_answer_total, no_try_total])
    print('')
    print('correct: ', result_percent_l[0] * 100)
    print('wrong:   ', result_percent_l[1] * 100)
    print('no_try:  ', result_percent_l[2] * 100)
    print('')
    print('avg solver time: ', (sum(solver_times) / len(solver_times)) )









SOLVED_DB_HEADER_LIST = ['timestamp', 'question #', 'question', 'A', 'B', 'C', 'correct', 'wrong', 'tryed_to_solve', 'right', 'time' ]

DB_CSV_PATH = 'test_db.csv'#"C:\\Users\\Brandon\\Documents\\Personal_Projects\\HQ_hack\\HQ_qo_database.csv"
KEYWORDS_CSV_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\HQ_hack\\HQ_Bot\\keywords.csv"

SOLVED_DB_CSV_PATH = 'solved_db.csv'

start_time = time.time()

try:
    os.remove(SOLVED_DB_CSV_PATH)
except:
    print('making new solved db csv...')
    
    
print('opening browser...')
br = phantom_js_browser.Browser()
keywords_d = utils.get_keywords_d_from_csv(KEYWORDS_CSV_PATH)



db_dl = logger.readCSV(DB_CSV_PATH)
# print(db_dl)
print('num lines to solve: ', len(db_dl) - 2)


try:
    
    line_cnt = 0
    for line_d in db_dl:
        question       = line_d['question']
        options       = [line_d['A'],
                         line_d['B'],
                         line_d['C']]
        correct_answer = line_d['correct']
    
    
        solver_start_time = time.time()
        
        solved_output_d = solver_select.solve(question, options, keywords_d, br)
        
        solver_end_time = time.time()    
        solver_time = solver_end_time - solver_start_time
        
        
        tryed_to_solve = '' # empty box if it did try to solve
        if solved_output_d['answer'] == None:
            tryed_to_solve = 'NO_TRY'
            
        wrong = ''
        right = ''
        if solved_output_d['answer'] != None:
            if solved_output_d['answer'] == correct_answer:
                right = 'RIGHT'
            else:
                wrong = 'WRONG'
            
    
        line_d['right'] = right
        line_d['wrong'] = wrong
        line_d['tryed_to_solve'] = tryed_to_solve
        line_d['time'] = solver_time
        
        logger.logSingle(line_d, SOLVED_DB_CSV_PATH, wantBackup = False, headerList = SOLVED_DB_HEADER_LIST, overwriteAction = 'append')
        
        print('')
        print('solved line:  %s,   time = %s' %(line_cnt + 2, solver_time))#`````````````````````````````````````````````````````````````````````````
        line_cnt += 1
except:
    print('ERROR, %s is probably open' %(SOLVED_DB_CSV_PATH))
    
    

end_time = time.time()
print('total_time: solved %s lines in %s sec' %(line_cnt, end_time - start_time))


br.end()



print_solved_csv_stats(SOLVED_DB_CSV_PATH)


print('done!')

















