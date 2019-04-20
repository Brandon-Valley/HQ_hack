from threading import Thread
import operator

import build_qo_properties
import solver_utils

from solvers import Basic_Wiki_Match


def init_solver_l():
    solver_l = []
    
    solver_l.append(Basic_Wiki_Match.Basic_Wiki_Match())
  
    return solver_l


def run_all_appropriate_solvers_in_thier_own_thread(question, options, qo_properties, results_l, appropriate_solver_l, br):
    thread_list = []
    
    for solver in appropriate_solver_l:
        thread_list.append(Thread(target=solver.solve, args=(question, options, qo_properties, results_l, br)))

    for thread in thread_list:
        thread.start()
       
    for thread in thread_list:
        thread.join()


def get_solver_output_l(question, options, keywords_d, br):
    qo_properties = build_qo_properties.build_qo_properties(question, options, keywords_d)
    solver_l = init_solver_l()
    
    # make list of solvers that are appropriate to use for this question based on the qo_properties
    appropriate_solver_l = []
    for solver in solver_l:
        if solver.appropriate(qo_properties):
            appropriate_solver_l.append(solver)
            
    results_l = [] # list of all solver outputs
    run_all_appropriate_solvers_in_thier_own_thread(question, options, qo_properties, results_l, appropriate_solver_l, br)
#     
#     for solver_output in results_l: #````````````````````````````````````````````````````````````````````
#         solver_output.print_me()
        
    return results_l



ANSWER_INDEX_LIST = ['A', 'B', 'C']

def get_answer(options_percent_totals_l):
    if options_percent_totals_l == [0,0,0]:
        return None
    
    max_index, max_value = max(enumerate(options_percent_totals_l), key=operator.itemgetter(1))
    return ANSWER_INDEX_LIST[max_index]
    



def calc_total_solved_output_d(solver_output_l):    
    options_totals_l = [0,0,0]
    
    for solver_output in solver_output_l:
        options_totals_l[0] = solver_output.option_1_pts * ( solver_output.confidence / 100 )
        options_totals_l[1] = solver_output.option_2_pts * ( solver_output.confidence / 100 )
        options_totals_l[2] = solver_output.option_3_pts * ( solver_output.confidence / 100 )
        
    options_percent_totals_l = solver_utils.num_occurrence_percent_l(options_totals_l)
    
    solved_output_d = {'option_1_pts': options_percent_totals_l[0] * 100,
                       'option_2_pts': options_percent_totals_l[1] * 100,
                       'option_3_pts': options_percent_totals_l[2] * 100,
                       'answer'      : get_answer(options_percent_totals_l)}

    return solved_output_d
    




def solve(question, options, keywords_d, br):
    solver_output_l = get_solver_output_l(question, options, keywords_d, br)
    solved_output_d = calc_total_solved_output_d(solver_output_l)
    return solved_output_d
    



def main():
    question = 'Who is credited with coining the phrase: "For whom the bell tolls"?'
    options = ['John Donne', 'Maryland', 'Ernest Hemingway']    
    solved_output_d = solve(question, options, {'negative': ['not']})
    print(solved_output_d)



if __name__ == "__main__":
    main()

