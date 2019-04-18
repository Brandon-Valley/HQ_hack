

class Solver_Output():
    def __init__(self):
        # total out of 100
        self.option_1_pts = 0
        self.option_2_pts = 0
        self.option_3_pts = 0

        # 0 - 100, how confident the solver is that it is correct
        self.confidence = 100
        
        # weight of the overall answer from this solver, 0 - 100
        self.weight = 100;



class Solver():
    def __init__(self):
        self.solver_output = Solver_Output()
        
    
    # decide if this solver is appropriate based on the question and options
    def appropriate(self, qo_properties):
        print('need to implement appropriate function!')
        return False;
        
        
    def solve(self, question, options, qo_properties):
        print('need to implement solve function!')
        return self.solver_output
    
    
    
    
    
    