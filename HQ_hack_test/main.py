import webbrowser
search_terms = ['cats', 'dogs']

# ... construct your list of search terms ...

for term in search_terms:
    url = "https://www.google.com.tr/search?q={}".format(term)
#     webbrowser.open_new_tab(url)
    chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
    chrome_browser.open_new_tab(url)