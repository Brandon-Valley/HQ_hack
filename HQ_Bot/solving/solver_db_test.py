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





# solver ideas
# -  if question contains the word 'phrase' and has a quoted phrase, google 'qusetion + phrases.org.uk" and search occurances
#    - would only apply to 0.011% 



# interesting questions:
# 10 - the quote is by john but is also the name of a book by hemmingway, maybe quara search?
#      - maybe search for popular phrase, 2nd article or question:  https://www.phrases.org.uk/meanings/for-whom-the-bell-tolls.html






DB_CSV_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\HQ_hack\\HQ_qo_database.csv"
KEYWORDS_CSV_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\HQ_hack\\HQ_Bot\\keywords.csv"

DB_LINE_NUM = 10



db_dl = logger.readCSV(DB_CSV_PATH)

question = db_dl[DB_LINE_NUM - 2]['question']
options = [db_dl[DB_LINE_NUM - 2]['A'],
           db_dl[DB_LINE_NUM - 2]['B'],
           db_dl[DB_LINE_NUM - 2]['C']]

# print(db_dl[DB_LINE_NUM - 2])
keywords_d = utils.get_keywords_d_from_csv(KEYWORDS_CSV_PATH)

solver_output_l = solver_select.get_solver_output_l(question, options, keywords_d)


#show output of test
print('question:  ', question)
print('')
print('option_1:  ', options[0])
print('option_2:  ', options[1])
print('option_3:  ', options[2])
print('')


for solver_output in solver_output_l: #````````````````````````````````````````````````````````````````````
    solver_output.print_me()



















