from bs4_handle_helper import *
from urllib.parse import urljoin

def scrapeLinks(base, totalPageNum, groupingClass, postLinkClass = None, hasReseachLink = False, researchLinkClass = None, useHeader = True, infiniteScroll = False, infiniteScrollButtonXPath = None, useDriver = False):
    allLinks = []
    if totalPageNum == 0:
        url = base
        if infiniteScroll:
            soup = getSoupWithInfiniteScroll(url, infiniteScrollButtonXPath)
        else:
            if useDriver == True:
                soup = getSoupWithWebDriver(url)
            else:
                soup = getSoup(url, useHeader)
        pageLinks = getPostLinksFromSoup(soup, url, groupingClass, postLinkClass, hasReseachLink, researchLinkClass)
        allLinks = pageLinks
    else:
        for page in range(1, totalPageNum + 1):
            url = base + str(page)
            if useDriver == True:
                soup = getSoupWithWebDriver(url)
            else:
                soup = getSoup(url, useHeader)
            if soup == None: continue
            pageLinks = getPostLinksFromSoup(soup, url, groupingClass, postLinkClass, hasReseachLink, researchLinkClass)
            allLinks = allLinks + pageLinks
    return allLinks

def getPostLinksFromSoup(soup, url, groupingClass, postLinkClass = None, hasReseachLink = False, researchLinkClass = None):
    pageLinks = []
    groups = soup.find_all(class_ = groupingClass)
    postLink, researchLink = None, None
    if hasReseachLink:
        for group in groups:
            if postLinkClass == None:
                postAnchor = group.find("a")
            else:
                postAnchor = group.find("a", class_ = postLinkClass)
            if postAnchor:
                postLink = urljoin(url, postAnchor.get('href'))
            if researchLinkClass:
                try:
                    researchAnchor = group.find("a", class_ = researchLinkClass)
                    researchLink = urljoin(url, researchAnchor.get('href'))
                except:
                    researchLink = None
            pageLinks.append([postLink, researchLink])
    else:
        for group in groups:
            if postLinkClass == None:
                postAnchors = group.find_all("a")
            else:
                postAnchors = group.find_all("a", class_ = postLinkClass)
            for postAnchor in postAnchors:
                postLink = urljoin(url, postAnchor.get('href'))
                pageLinks.append([postLink, None])

    return pageLinks
