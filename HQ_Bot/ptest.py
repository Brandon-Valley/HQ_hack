import time
from urllib.parse import quote_plus
from selenium import webdriver
import threading

PATH = 'C:/Users/Brandon/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe' ## SET YOU PATH TO phantomjs

class Browser:

    def __init__(self, path = PATH, initiate=True, implicit_wait_time = 0, explicit_wait_time = 0):#implicit_wait_time = 10, explicit_wait_time = 2):
        print('starting phantom js browser...')
        self.sem = threading.Semaphore()
        
        
        self.id_d = {}
        
        self.path = PATH
        self.implicit_wait_time = implicit_wait_time    # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        self.explicit_wait_time = explicit_wait_time    # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        if initiate:
            self.start()
        return

    def start(self):
        print('in start')
        self.driver = webdriver.PhantomJS(PATH)
#         self.driver.implicitly_wait(self.implicit_wait_time)
        print('about done starting browser???')
        return

    def end(self):
        self.driver.quit()
        return

    def go_to_url(self, url, wait_time = None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
        self.driver.get(url)
#         print('[*] Fetching results from: {}'.format(url))
        time.sleep(wait_time)
        return

    def get_search_url(self, query, page_num=0, per_page=1, lang='en'):
        query = quote_plus(query)
        url = 'https://www.google.hr/search?q={}&num={}&start={}&nl={}'.format(query, per_page, page_num*per_page, lang)
        return url

    def scrape(self):
        #xpath migth change in future
        links = self.driver.find_elements_by_xpath("//h3[@class='r']/a[@href]") # searches for all links insede h3 tags with class "r"
        results = []
        for link in links:
            d = {'url': link.get_attribute('href'),
                 'title': link.text}
            results.append(d)
        return results

    def search(self, query, id, page_num=0, per_page=1, lang='en', wait_time = None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
            
        self.id_d[id] = {'url': self.get_search_url(query, page_num, per_page, lang) } #  url = self.get_search_url(query, page_num, per_page, lang)


            
        self.sem.acquire()
        self.go_to_url(self.id_d[id]['url'], wait_time)
        results = self.scrape()
        self.sem.release()
        
        return results






def get_search_result(query, result_l_index, results_l, br):
    
    results = br.search(query, result_l_index )
    results_l[result_l_index] = results
    print('         just finished thread: ', result_l_index)
    return
# #     print('trying: ', result_l_index)
# #     solved = False
# #     while True:
#     try:
#         results = br.search(query )
#         results_l[result_l_index] = results
#     #     THREADS_DONE += 1
#     #     print('threads done: ', THREADS_DONE)
#         print('         just finished thread: ', result_l_index)
#         return
#     except:
#         print('sleeping: ', result_l_index)
#         time.sleep(3)
#         get_search_result(query, result_l_index, results_l, br)
#         
#         
# #             print('sleeping on thread: ', result_l_index)
# #             time.sleep(5)

# def add_and_start_thread(x, br, thread_list, results_l):
#     t = Thread(target=get_search_result, args=('origin of the number ' + str(x), x, results_l, br))
#     thread_list.append(t)
#     t.start()


from threading import Thread


NUM_THREADS_ = 10
def main():

    path = 'C:/Users/Brandon/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe' ## SET YOU PATH TO phantomjs
    br = Browser()
    print('here')
    i = 0
    start = time.time()
    
    thread_list = []
    results_l = []
#     for x in range(NUM_THREADS_):
#         results_l.append(None)
#         thread_list.append(Thread(target=get_search_result, args=('origin of the number ' + str(x), x, results_l, br)))
#         
#         
#     start_time = time.time()
#         
#     threads_started = 0
#     for thread in thread_list:
#         if (threads_started > 0 and threads_started % 40 == 0):
#             print('sleeping on starting threads, threads_started = ', threads_started)
#             time.sleep(10)
#         thread.start()
#         threads_started += 1
#        
#     for thread in thread_list:
#         thread.join()



    start_time = time.time()
    
    
    
    
    for x in range(NUM_THREADS_):
        results_l.append(None)
        thread_list.append(Thread(target=get_search_result, args=('origin of the number ' + str(x), x, results_l, br)))
    
    for thread in thread_list:
        thread.start()
     
    for thread in thread_list:
        thread.join()
    
    
    
    
#     THREADS_AT_A_TIME = 30
#     finished_threads = 0;
#     while(finished_threads < NUM_THREADS_):
#         cur_thread_list = []
#         
#         for x in range(THREADS_AT_A_TIME):
#             result_l_index = x + finished_threads
#             t = Thread(target=get_search_result, args=('origin of the number ' + str(result_l_index), result_l_index, results_l, br))
#             cur_thread_list.append(t)
#             
#         for thread in cur_thread_list:
#             thread.start()
#         
#         for thread in cur_thread_list:
#             thread.join()
    
    
#     
# 
#     for x in range(NUM_THREADS_):
#         if x > 0:
#             if x % 40 == 0:
#                 print('just made and started another 40 threads, joining all running threads before continueing, x: ', x)
#                 for thread in thread_list:
#                     thread.join()
# #                 time.sleep(10)
#         
#         
#         results_l.append(None)
# #         thread_list.append(Thread(target=get_search_result, args=('origin of the number ' + str(x), x, results_l, br)))
#         add_and_start_thread(x, br, thread_list, results_l)
#         
#         
    
        
#     threads_started = 0
#     for thread in thread_list:
#         if (threads_started > 0 and threads_started % 40 == 0):
#             print('sleeping on starting threads, threads_started = ', threads_started)
#             time.sleep(10)
#         thread.start()
#         threads_started += 1
       
#     for thread in thread_list:
#         thread.join()
    
    
    success_total = 0    
    for result_num, result in enumerate(results_l):
        if result != None:
            success_total += 1
            
        print('%s:  %s' %(result_num, result))
        
    
    print('success_total: ', success_total)
    
    total_time = time.time() - start_time
    print('total_time = ', total_time)
    print('avg time per search: ', total_time / NUM_THREADS_)




# 
#     results = br.search('What was the first theatrical feature film to be completely computer-animated? ' )
#     for r in results:
#         print(r)
#     print('%s    %s' %(i, time.time() - start))
#     i += 1
#             
#     end = time.time()
#     print('total_time: ', end - start)
#     
#     br.end()
    
    
    
    
if __name__ == "__main__":
    main()