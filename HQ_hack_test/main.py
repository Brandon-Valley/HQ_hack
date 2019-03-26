# import webbrowser
# search_terms = ['cats', 'dogs']
# 
# # ... construct your list of search terms ...
# 
# for term in search_terms:
#     url = "https://www.google.com.tr/search?q={}".format(term)
# #     webbrowser.open_new_tab(url)
#     chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
#     chrome_browser.open_new_tab(url)


try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
   
# to search 
query = "which musical act was not signed to motown? + wiki"
   
for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
    print(j) 
     
    
    
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://en.wikipedia.org/wiki/List_of_Motown_artists'

# Connect to the URL
response = requests.get(url)
# for line in response.text:
#     print(line)

if "Baker Sanusis" in response.text:
    print("yay")
    
print(response.text.count('Baker Sanusi'))


# soup = BeautifulSoup(response.text, "html.parser")
# print (soup)