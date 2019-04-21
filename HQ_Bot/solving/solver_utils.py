import webbrowser
from googlesearch import search

    
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import time

        
        
        
def get_first_wiki_article_url(query, br):
#     got_result = False
    while True:
    
        result = br.search(query + 'wiki')
#         print('in solver utils', result)#1`````````````````````````````````````````````````````````````````````````````````````
        
        if result == []:
            print('sleeping...')
            time.sleep(5)
        else:
            return result[0]['url']


#     try: 
#         from googlesearch import search 
#     except ImportError:  
#         print("No module named 'google' found") 
       
    # to search 
#     query = "which musical act was not signed to motown? + wiki"
       
    for j in search(query + ' wiki', tld="co.in", num=1, stop=1, pause=0): 
        return j
    
    
    

def get_text_from_url(url):
    # Connect to the URL
    response = requests.get(url)
    return response.text


# def get_text_from_first_wiki_article(query):
#     url = get_first_wiki_article_url(query)
#     return get_text_from_url(url)


def build_num_occurrence_l(text, terms_l):
    num_occurrences_l = []
    
    for term in terms_l:
        num_occurrences_l.append(text.count(term))
    
    return num_occurrences_l


def num_occurrence_percent_l(num_occurrence_l):
    num_occ_percent_l = [0,0,0]
    
    # if given all 0's, return all 0's
    if num_occurrence_l == [0,0,0]:
        return num_occ_percent_l
    
    total_occ = sum(num_occurrence_l)
    
    num_occ_percent_l[0] = num_occurrence_l[0] / total_occ
    num_occ_percent_l[1] = num_occurrence_l[1] / total_occ
    num_occ_percent_l[2] = num_occurrence_l[2] / total_occ
    
    return num_occ_percent_l





# is greater than zero
def is_gt_zero(num):
    if num > 0:
        return True
    return False




# def build_occurrence_stat_dict_list(text, terms_l):
#     occ_stat_dl = []
#     
#     for term in terms_l:
#         occ_stat_d = {'option' : term,
#                       'count'  : text.count(term)}
#         occ_stat_dl.append(occ_stat_d)
# 
# #         occ_stat_d[term] = text.count(term)
#         
#     return occ_stat_dl
    
    
    


    


# def show_relation_stats(question, options_l):
#     print('getting relation stats...')
#     
#     start = time.time()#```````````````````````````````````````````````````````````````
#     
#     q_wiki_url = get_first_wiki_article_url(question)#```````````````````````````````````````````````````````````
#     
#     end = time.time()
#     print('get_first_wiki_article_url(question): ', end - start)#`````````````````````````````````````````````````
#     
#     q_wiki_title = get_wiki_title(q_wiki_url)
#     q_wiki_text = get_text_from_url(q_wiki_url)
#     occ_stat_dl = build_occurrence_stat_dict_list(q_wiki_text, options_l)
# #     print(occ_stat_d)
#     print_occurrence_stat_dict_list(occ_stat_dl, q_wiki_title)
#     
    
    
#     
#     
#     
#     
# A = ''
# 
# 
# from threading import Thread
# 
# def func1(q):
#     url = get_first_wiki_article_url(q)
#     print (url)
#     dd = get_text_from_url(url)
# #     print (dd)
# #     print('done1')
# #     return a
# #     A = a
# 
# def func2():
#     get_first_wiki_article_url('how long do dogs get')
#     print('done2')
# 
# # if __name__ == '__main__':
# #     Thread(target = func1).start()
# #     Thread(target = func2).start()
#     
#     
#     
#     
#     
# if __name__ == '__main__':
#         
#     start = time.time()#```````````````````````````````````````````````````````````````
#     
#     # q_wiki_url = get_first_wiki_article_url('how long do cats get')#```````````````````````````````````````````````````````````
#     
#     # Thread(target = func1).start()
#     # Thread(target = func2).start()
#     # 
#     # 
#     # while (Thread(target = func1).is_alive() == False):
#     #     print ('waiting')
#         
#         
#     # t1 = Thread(target=func1, args=(['how many letters in alphabet']))
#     # t2 = Thread(target=func1, args=(['history of the letter a']))
#     # t3 = Thread(target=func1, args=(['history of the letter b']))
#     # t4 = Thread(target=func1, args=(['history of the letter c']))
#     # t5 = Thread(target=func1, args=(['history of the letter d']))
#     # t6 = Thread(target=func1, args=(['history of the letter e']))
#     # 
#     # t1.start()
#     # t2.start()
#     # t3.start()
#     # t4.start()
#     # t5.start()
#     # t6.start()
#     # 
#     # t1.join()
#     # t2.join()
#     # t3.join()
#     # t4.join()
#     # t5.join()
#     # t6.join()
#     # # t2.join()    
#         
#         
#     num_threads = 5    
#     thread_list = []
#     
#     for thread_num in range(num_threads):
#         question = 'history of the number ' + str(thread_num)
#         new_thread = Thread(target=func1, args=([question]))
#         thread_list.append(new_thread)
#         
#     for thread in thread_list:
#         thread.start()
#     
#     
#     for thread in thread_list:
#         thread.join()
#         
#         
#         
#     
#     end = time.time()
#     print('get_first_wiki_article_url(question): ', end - start)#`````````````````````````````````````````````````
#     print(A)
#         
#         
#         
#         
#         