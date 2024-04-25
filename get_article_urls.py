import os
import shutil
from bs4_handle_helper import * 
from get_article_urls_helper import scrapeLinks

def scrapeOpenAIBlogLinks():
    base = "https://openai.com/blog?page="
    totalPageNum = 7
    groupingClass = "lg:w-3-cols xs:w-6-cols mt-spacing-6 md:w-4-cols"
    return scrapeLinks(base, totalPageNum, groupingClass)

def scrapeOpenAIResearchLinks():
    base = "https://openai.com/research?page="
    totalPageNum = 9
    groupingClass = "cols-container relative"
    postLinkClass = "ui-link group f-ui-1 inline-block relative ui-link--inherit relative"
    researchLinkClass = "ui-link group f-ui-1 inline-block relative ui-link--inherit ml-auto shrink-0 relative self-start"
    return scrapeLinks(base, totalPageNum, groupingClass, postLinkClass, researchLinkClass= researchLinkClass, hasReseachLink= True)

def scrapeAnthropicBlogLinks():
    base = "https://claudeai.uk/ai-blog/page/"
    totalPageNum = 57
    groupingClass = "entry-title"
    return scrapeLinks(base, totalPageNum, groupingClass, useHeader = False)

def scrapeAnthropicNewsLinks():
    base = "https://www.anthropic.com/news"
    totalPageNum = 0
    groupingClass = "contentFadeUp s:grid s:grid-12 PostList_post-grid-masonry__fWABy"
    return scrapeLinks(base, totalPageNum, groupingClass)

def scrapeMicrosoftNewsLinks():
    base = 'https://news.microsoft.com/source/view-all/?_tags=ai&_paged='
    totalPageNum = 33
    groupingClass = "fwpl-item el-lhgurn"
    return scrapeLinks(base, totalPageNum, groupingClass)
    
def scrapeMetaBlogLinks():
    base = 'https://ai.meta.com/blog'
    buttonXPath = "/html/body/div/div/div[2]/div/div[8]/div/div[4]/button"
    totalPageNum = 0
    groupingClass = "_amtj"
    postLinkClass = "_amsv"
    return scrapeLinks(base, totalPageNum, groupingClass, postLinkClass, infiniteScroll= True, infiniteScrollButtonXPath= buttonXPath)

def scrapeGoogleAIBlogLinks():
    base = "https://blog.google/technology/ai/"
    buttonXPath = "/html/body/main/article/section[2]/uni-article-feed/div/button"
    totalPageNum = 0
    groupingClass = "article-list__feed load-more-content"
    postLinkClass = "feed-article__overlay"
    return scrapeLinks(base, totalPageNum, groupingClass, postLinkClass, infiniteScroll= True, infiniteScrollButtonXPath= buttonXPath)

def scrapeGoogleGeminiLinks():
    base = "https://blog.google/products/gemini/"
    buttonXPath = "/html/body/main/article/section[2]/uni-article-feed/div/button"
    totalPageNum = 0
    groupingClass = "article-list__feed load-more-content"
    postLinkClass = "feed-article__overlay"
    return scrapeLinks(base, totalPageNum, groupingClass, postLinkClass, infiniteScroll= True, infiniteScrollButtonXPath= buttonXPath)

def scrapeGoogleResearchLinks():
    base = "https://research.google/blog/?search=AI&page="
    totalPageNum = 25
    groupingClass = "glue-grid blog-posts-grid__cards"
    postLinkClass = "glue-card not-glue"
    return scrapeLinks(base, totalPageNum, groupingClass, postLinkClass)

def scrapeTheVergeLinks():
    base = "https://www.theverge.com/ai-artificial-intelligence/archives/"
    totalPageNum = 15
    groupingClass = "mx-auto w-full"
    postLinkClass = "after:absolute after:inset-0 group-hover:shadow-underline-blurple dark:group-hover:shadow-underline-franklin"
    return scrapeLinks(base, totalPageNum, groupingClass, postLinkClass)

def createLinksFolder():
    folder_path = os.path.join(os.getcwd(), "Links")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

def printLinksToFile(allLinks, type):
    csvPath = "Links/" + type + ".txt"
    with open(csvPath, 'w') as file:
        for pair in allLinks:
            line = str(pair[0]) + " " + str (pair[1])
            print(line, file = file)
        
if __name__ == "__main__":
    # createLinksFolder()
    # printLinksToFile(scrapeOpenAIBlogLinks(),type = "OpenAI_Blog")
    # printLinksToFile(scrapeOpenAIResearchLinks(),type = "OpenAI_Research")
    # printLinksToFile(scrapeAnthropicBlogLinks(),type = "Anthropic_Blog")
    # printLinksToFile(scrapeAnthropicNewsLinks(),type = "Anthropic_News")
    # printLinksToFile(scrapeMicrosoftNewsLinks(),type = "Micrisoft_News")
    # printLinksToFile(scrapeMetaBlogLinks(),type = "Meta_Blog")
    # printLinksToFile(scrapeGoogleAIBlogs(),type = "Google_Blog")
    # printLinksToFile(scrapeGoogleGemini(),type = "Google_Gemini")
    # printLinksToFile(scrapeGoogleResearchLinks(),type = "Google_Research")
    printLinksToFile(scrapeTheVergeLinks(),type = "The_Verge_AI")