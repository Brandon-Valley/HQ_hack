
import colors
import logger



def avg_time(times):
    #print average time
    total_time = 0
    for time in times:
        total_time += time
    return total_time / len(times)




def print_question_and_options(question, options):
    try:
        print('    options: ', options)
    except:
        print (colors.BRIGHT_RED + "Terminal Print Fail")
        
    try:
        print('    question: ', question)
    except:
        print (colors.BRIGHT_RED + "Terminal Print Fail")
        
        
        
# returns a dictionary like: {'negative' : ['not', 'neither'], ...    
def get_keywords_d_from_csv(csv_path):
    keywords_d = {}
    
    data_dl = logger.readCSV(csv_path)
#     print(data_dl)
    
    # initialize headers
    for keyword_type, keyword in data_dl[0].items():
        keywords_d[keyword_type] = []
                 
       
    for data_d in data_dl:
        for keyword_type, keyword in data_d.items():
            if keyword != '':
                keywords_d[keyword_type].append(keyword)
    
    return keywords_d
        









# import answer_bot
# if __name__ == "__main__":
#     answer_bot.main()

