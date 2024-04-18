
from urllib.parse import urljoin
from bs4_handle_helper import * 

def scrapeOpenAIBlogLinks():
    base = 'https://openai.com/blog?page='
    pageNum = 7
    allLinks = []
    for page in range(1, pageNum + 1):
        url = base + str(page)
        soup = getParsedHTML(url)
        if soup == None: continue
        postLinks = soup.find_all('a', type = "blog-details")
        for link in postLinks:
            link = [urljoin(url, link.get('href')), None]
            allLinks.append(link)
    return allLinks

def scrapeOpenAIResearchLinks():
    base = 'https://openai.com/research?page='
    pageNum = 9
    allLinks = []
    for page in range(1,pageNum + 1):
        url = base + str(page)
        soup = getParsedHTML(url)
        if soup == None: continue
        postClasses = soup.find_all(class_ = "cols-container relative")
        for postClass in postClasses:
            posts = postClass.find_all(class_ = "ui-link group f-ui-1 inline-block relative ui-link--inherit relative")
            articleLink, postLink = None, None
            for item in posts:
                postLink = urljoin(url, item.get('href'))
            articles = postClass.find_all(class_ = "ui-link group f-ui-1 inline-block relative ui-link--inherit ml-auto shrink-0 relative self-start")
            for item in articles:
                articleLink = item.get('href')
            allLinks.append([postLink,articleLink])
    return allLinks

def scrapeAnthropicBlogLinks():
    base = 'https://claudeai.uk/ai-blog/page/'
    pageNum = 56
    allLinks = []
    for page in range(1, pageNum + 1):
        url = base + str(page)
        soup = getParsedHTML(url)
        if soup == None: continue
        postClass = soup.find_all(class_ = "rpwwt-widget")[0]
        postLinks = postClass.find_all('a')
        for link in postLinks:
            link = [urljoin(url, link.get('href')), None]
            allLinks.append(link)
    return allLinks

def scrapeAnthropicNewsLinks():
    base = 'https://www.anthropic.com/news'
    allLinks = []
    url = base
    soup = getParsedHTML(url)
    if soup == None: return allLinks
    postClass = soup.find_all(class_ = "contentFadeUp s:grid s:grid-12 PostList_post-grid-masonry__fWABy")[0]
    postLinks = postClass.find_all('a')
    for link in postLinks:
        link = [urljoin(url, link.get('href')), None]
        allLinks.append(link)
    return allLinks

def scrapeMicrosoftNewsLinks():
    base = 'https://news.microsoft.com/source/view-all/?_tags=ai&_paged='
    pageNum = 33
    allLinks = []
    for page in range(1, pageNum + 1):
        url = base + str(page)
        soup = getParsedHTML(url)
        if soup == None: continue
        postClasses = soup.find_all(class_ = "fwpl-item el-lhgurn")
        for postClass in postClasses:
            postLinks = postClass.find_all('a')
            for link in postLinks:
                link = [urljoin(url, link.get('href')), None]
                allLinks.append(link)
    return allLinks