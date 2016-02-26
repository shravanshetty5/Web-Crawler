def get_next_target(page):   #Takes as input the extracted contents of the page and returns the 1st URL
    start_link = page.find('<a href=') # and its end point
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q): # takes as input two strings and combines them without elements repeating
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page, depth): # Takes as input the extracted contents of a page and depth
    links = [] # returns all the links(URLs) in the page and their depths
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append([url, depth + 1])
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed,max_depth): #Main Program - Takes as input seed link and the max depth it needs to crawl
    tocrawl = [[seed, 0]] #WILL CONTAIN links and thier depths
    depth = 0
    crawled = []
    index = []
    while tocrawl and depth <= max_depth: #keep crawling till all pages are crawled or max depth is reached
        page, depth = tocrawl[0]
        tocrawl = tocrawl[1:]
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl, get_all_links(content, depth))
            crawled.append(page)
        if tocrawl:
            depth = tocrawl[0][1] # assign depth of the next element in the to crawl list
        else:
            break
    return index

def get_page(url):#Program to get page content
	try:
	    import urllib
	    return urllib.urlopen(url).read()

	except:
	    return "error"

def add_to_index(index, keyword, url):#Program searches if keyword and url are
    for lineIndex in index: #in index, and if not, adds it to index
        if lineIndex[0] == keyword:
            if url not in lineIndex[1]:
                lineIndex[1].append(url)
            return
    index.append([keyword, [url]])

def lookup(index, keyword):#program looks up keyword in index and gives
    for lineIndex in index:#list of related URLs
        if lineIndex[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):#takes all the contents in the page
    words = content.split() #and creates Index
    for keyword in words:
        add_to_index(index, keyword, url)
