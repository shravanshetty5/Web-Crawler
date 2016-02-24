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
    while tocrawl and depth <= max_depth: #keep crawling till all pages are crawled or max depth is reached
        page, depth = tocrawl[0]
        tocrawl = tocrawl[1:]
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page), depth))
            crawled.append(page)
        if tocrawl:
            depth = tocrawl[0][1] # assign depth of the next element in the to crawl list
        else:
            break
    return crawled
