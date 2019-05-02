

def print_str_wo_error(str):
    output = ''
    
    for char in str:
        try:
            print(char, end = '')
        except:
            print('[' + format(ord(char), "x") + ']', end = '')
            
    print('')
    

def print_qo_d(qo_d):
    print('')
    print_str_wo_error('Question:  ' + qo_d['question'])
    print_str_wo_error('Option_1:  ' + qo_d['option_1'])
    print_str_wo_error('Option_2:  ' + qo_d['option_2'])
    print_str_wo_error('Option_3:  ' + qo_d['option_3'])