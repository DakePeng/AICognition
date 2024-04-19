from bs4_handle_helper import *
from newspaper import Article
from AICognitionPost import AICognitionPost 

def scrapeArticle(url):
    article = Article(url)
    article.download()
    article.parse()
    return article

def scrapeArticleList(allLinks):
    result = []
    for [url, researchLink] in allLinks:
        print(len(result))
        try: 
            article = scrapeArticle(url)
        except:
            article = emptyArticle()
        result.append(AICognitionPost(article, researchLink))
    return result

def emptyArticle():
    return Article("")

if __name__ == "__main__":
    url = "https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/"
    print(scrapeArticle(url).text)
    #print(emptyArticle().text)