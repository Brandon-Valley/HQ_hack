# to ba able to import from parent dir
import sys
parent_dir_path = ''
parent_dir_path_list = sys.path[0].split('\\')[0:-1]
for dir in parent_dir_path_list:
    parent_dir_path += dir + '\\'
parent_dir_path = parent_dir_path[0:-1]
sys.path.append(parent_dir_path)

# from parent dir
import Solver 
import solver_utils


# pulls first page in google for the full question + 'wiki', then finds # of occurances of all options,
# only gives confident answer if only one of the options occurs

class Basic_Wiki_Match(Solver.Solver):
    def __init__(self):
        self.solver_output = Solver.Solver_Output('Basic_Wiki_Match') 
    
    # decide if this solver is appropriate based on the question and options
    def appropriate(self, qo_properties):
#         print('need to implement appropriate function!')
        return True;
        
        
    def solve(self, question, options, qo_properties, results_l):
        q_wiki_text = solver_utils.get_text_from_first_wiki_article(question)
        num_occ_l = solver_utils.build_num_occurrence_l(q_wiki_text, options)
        
        # most simple solver, only return a confident answer if only one option appeared in text
        if (num_occ_l.count(0) == 2):
            self.solver_output.option_1_pts = solver_utils.is_gt_zero(num_occ_l[0]) * 100
            self.solver_output.option_2_pts = solver_utils.is_gt_zero(num_occ_l[1]) * 100
            self.solver_output.option_3_pts = solver_utils.is_gt_zero(num_occ_l[2]) * 100
        else:
            self.solver_output.confidence = 0
        
        results_l.append(self.solver_output)
    
    
    
if __name__ == '__main__':
    bwm = Basic_Wiki_Match()
    print(bwm.solver_output.weight)
    
    bwm.appropriate(4)


