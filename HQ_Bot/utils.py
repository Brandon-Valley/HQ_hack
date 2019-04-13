
import colors



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
        