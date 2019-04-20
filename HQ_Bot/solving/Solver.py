

class Solver_Output():
    def __init__(self, solver_name):
        self.name = solver_name
        
        # total out of 100
        self.option_1_pts = 0
        self.option_2_pts = 0
        self.option_3_pts = 0

        # 0 - 100, how confident the solver is that it is correct
        self.confidence = 100
        
        # weight of the overall answer from this solver, 0 - 100
        self.weight = 100;
    
    def print_me(self):
        indent = '    '
        print('name:  ', self.name)
        print(indent + 'option_1_pts:  ' + str (self.option_1_pts))
        print(indent + 'option_2_pts:  ' + str (self.option_2_pts))
        print(indent + 'option_3_pts:  ' + str (self.option_3_pts))
        print(indent + 'confidence:    ' + str (self.confidence))
        print(indent + 'weight:        ' + str (self.weight))



class Solver():
    def __init__(self):
        self.solver_output = Solver_Output('DEFAULT_SOLVER_NAME')        
    
    # decide if this solver is appropriate based on the question and options
    def appropriate(self, qo_properties):
        print('need to implement appropriate function!')
        return False;
        
        
    def solve(self, question, options, qo_properties, results_l):
        print('need to implement solve function!')

        results_l.append(self.solver_output)
    
    
    
    
    
    