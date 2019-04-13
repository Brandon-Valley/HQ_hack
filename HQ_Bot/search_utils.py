import webbrowser
from googlesearch import search

import colors

import time

def chrome_search(search_terms):   
    for term in search_terms:
        url = "https://www.google.com.tr/search?q={}".format(term)
    #     webbrowser.open_new_tab(url)
        chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        chrome_browser.open_new_tab(url)
        
        
        
def get_first_wiki_article_url(query):
#     try: 
#         from googlesearch import search 
#     except ImportError:  
#         print("No module named 'google' found") 
       
    # to search 
#     query = "which musical act was not signed to motown? + wiki"
       
    for j in search(query + ' wiki', tld="co.in", num=1, stop=1, pause=0): 
        return j
    
    
    
    
    
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def get_text_from_url(url):

#     # Set the URL you want to webscrape from
#     url = 'https://en.wikipedia.org/wiki/List_of_Motown_artists'
    
    # Connect to the URL
    response = requests.get(url)
    return response.text






def build_occurrence_stat_dict_list(text, terms_l):
    occ_stat_dl = []
    
    for term in terms_l:
        occ_stat_d = {'option' : term,
                      'count'  : text.count(term)}
        occ_stat_dl.append(occ_stat_d)

#         occ_stat_d[term] = text.count(term)
        
    return occ_stat_dl
    
    
    
def print_occurrence_stat_dict_list(occ_stat_dl, q_wiki_title):
    print(colors.BRIGHT_CYAN + '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('')
    print('      ' + 'wiki:    ' + q_wiki_title)
    print('')
    for occ_stat_d in occ_stat_dl:
        print('      %s : %s' %(occ_stat_d['option'], occ_stat_d['count']))

#     
#     for option,count in occ_stat_d.items():
#         print('    %s : %s' %(option,count))
    print('')    
    
    
def get_wiki_title(q_wiki_url):
    split_url = q_wiki_url.split('/')
    return split_url[-1]
    


def show_relation_stats(question, options_l):
    print('getting relation stats...')
    
    start = time.time()#```````````````````````````````````````````````````````````````
    
    q_wiki_url = get_first_wiki_article_url(question)#```````````````````````````````````````````````````````````
    
    end = time.time()
    print('get_first_wiki_article_url(question): ', end - start)#`````````````````````````````````````````````````
    
    q_wiki_title = get_wiki_title(q_wiki_url)
    q_wiki_text = get_text_from_url(q_wiki_url)
    occ_stat_dl = build_occurrence_stat_dict_list(q_wiki_text, options_l)
#     print(occ_stat_d)
    print_occurrence_stat_dict_list(occ_stat_dl, q_wiki_title)
    
    
    
    
    
    
    
A = ''


from threading import Thread

def func1(q):
    url = get_first_wiki_article_url(q)
    print (url)
    dd = get_text_from_url(url)
#     print (dd)
#     print('done1')
#     return a
#     A = a

def func2():
    get_first_wiki_article_url('how long do dogs get')
    print('done2')

# if __name__ == '__main__':
#     Thread(target = func1).start()
#     Thread(target = func2).start()
    
    
    
    
    
if __name__ == '__main__':
        
    start = time.time()#```````````````````````````````````````````````````````````````
    
    # q_wiki_url = get_first_wiki_article_url('how long do cats get')#```````````````````````````````````````````````````````````
    
    # Thread(target = func1).start()
    # Thread(target = func2).start()
    # 
    # 
    # while (Thread(target = func1).is_alive() == False):
    #     print ('waiting')
        
        
    # t1 = Thread(target=func1, args=(['how many letters in alphabet']))
    # t2 = Thread(target=func1, args=(['history of the letter a']))
    # t3 = Thread(target=func1, args=(['history of the letter b']))
    # t4 = Thread(target=func1, args=(['history of the letter c']))
    # t5 = Thread(target=func1, args=(['history of the letter d']))
    # t6 = Thread(target=func1, args=(['history of the letter e']))
    # 
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    # 
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()
    # # t2.join()    
        
        
    num_threads = 5    
    thread_list = []
    
    for thread_num in range(num_threads):
        question = 'history of the number ' + str(thread_num)
        new_thread = Thread(target=func1, args=([question]))
        thread_list.append(new_thread)
        
    for thread in thread_list:
        thread.start()
    
    
    for thread in thread_list:
        thread.join()
        
        
        
    
    end = time.time()
    print('get_first_wiki_article_url(question): ', end - start)#`````````````````````````````````````````````````
    print(A)
        
        
        
        
        