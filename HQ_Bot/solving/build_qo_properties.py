def get_quoted_phrases(question):
    if question.count('"') < 2:
        return []
    
    quoted_phrases = []
    split_q = question.split('"')
    
    for q_piece_num, q_piece in enumerate(split_q):
        if q_piece_num % 2 != 0: # if odd, b/c lists are 0 indexed
            quoted_phrases.append(q_piece)
    return quoted_phrases



def contains_neg_keyword(question, keywords_d):
    for keyword in keywords_d['negative']:
        if keyword in question:
            return True
    return False


def build_qo_properties(question, options, keywords_d):
    qo_prop_d = {'contains_neg_keyword' : contains_neg_keyword(question, keywords_d),
                 'quoted_phrases'       : get_quoted_phrases(question)}
    
    return qo_prop_d
    