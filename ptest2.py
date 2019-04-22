import time
from urllib.parse import quote_plus
from selenium import webdriver


class Browser:

    def __init__(self, path, initiate=True, implicit_wait_time = 10, explicit_wait_time = 2):
        self.path = path
        self.implicit_wait_time = implicit_wait_time    # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        self.explicit_wait_time = explicit_wait_time    # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        if initiate:
            self.start()
        return

    def start(self):
        self.driver = webdriver.PhantomJS(self.path)
        self.driver.implicitly_wait(self.implicit_wait_time)
        return

    def end(self):
        self.driver.quit()
        return

    def go_to_url(self, url, wait_time = None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
        self.driver.get(url)
        print('[*] Fetching results from: {}'.format(url))
        time.sleep(wait_time)
        return

    def get_search_url(self, query, page_num=0, per_page=10, lang='en'):
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

    def search(self, query, page_num=0, per_page=10, lang='en', wait_time = None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
        url = self.get_search_url(query, page_num, per_page, lang)
        self.go_to_url(url, wait_time)
        results = self.scrape()
        return results




path = 'C:/Users/Brandon/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe' ## SET YOU PATH TO phantomjs
br = Browser(path)
results = br.search('origen of the number 1')
for r in results:
    print(r)

br.end()