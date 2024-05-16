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
    url = "https://openai.com/research/weak-to-strong-generalization"
    print(scrapeArticle(url).text)