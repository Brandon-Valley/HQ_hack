

def contains_neg_keyword(question, keywords_d):
    for keyword in keywords_d['negative']:
        if question.contains(keyword):
            return True
    return False


def build_qo_properties(question, options, keywords_d):
    qo_prop_d = {'contains_neg_keyword' : contains_neg_keyword(question, keywords_d),
                 'quoted_phrases'       : []}
    


def solve(question, options, keywords):
    qo_properties = build_qo_properties(question, options, keywords_d)
    pass