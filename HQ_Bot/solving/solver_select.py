from threading import Thread

import build_qo_properties

from solvers import Basic_Wiki_Match


def init_solver_l():
    solver_l = []
    
    solver_l.append(Basic_Wiki_Match.Basic_Wiki_Match())
  
    return solver_l


def run_all_appropriate_solvers_in_thier_own_thread(question, options, qo_properties, results_l, appropriate_solver_l):
    thread_list = []
    
    for solver in appropriate_solver_l:
        thread_list.append(Thread(target=solver.solve, args=(question, options, qo_properties, results_l)))

    for thread in thread_list:
        thread.start()
       
    for thread in thread_list:
        thread.join()



def solve(question, options, keywords_d):
    qo_properties = build_qo_properties.build_qo_properties(question, options, keywords_d)
    solver_l = init_solver_l()
    
    # make list of solvers that are appropriate to use for this question based on the qo_properties
    appropriate_solver_l = []
    for solver in solver_l:
        if solver.appropriate(qo_properties):
            appropriate_solver_l.append(solver)
            
    results_l = [] # list of all solver outputs
    run_all_appropriate_solvers_in_thier_own_thread(question, options, qo_properties, results_l, appropriate_solver_l)
    
    for solver_output in results_l: #````````````````````````````````````````````````````````````````````
        solver_output.print_me()
    
    
    
#     print(qo_properties)#```````````````````````````````````````````````````````````````````````````
    pass



def main():

    options = ['Minneapolis', 'Maryland', 'Miami']    
    solve('what is a "baseball"  and a "cat"', options, {'negative': ['not']})



if __name__ == "__main__":
    main()

