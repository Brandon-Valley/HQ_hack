
import Solver


# pulls first page in google for the full question + 'wiki', then finds # of occurances of all options,
# only gives confident answer if only one of the options occurs

class Basic_Wiki_Match(Solver.Solver):
    def __init__(self):
        self.solver_output = Solver.Solver_Output()
        
    
    # decide if this solver is appropriate based on the question and options
    def appropriate(self, qo_properties):
        print('need to implement appropriate function!')
        return False;
        
        
    def solve(self, question, options, qo_properties):
        print('need to implement solve function!')
        return self.solver_output
    
    
    
if __name__ == '__main__':
    bwm = Basic_Wiki_Match()
    
    bwm.appropriate(4)


