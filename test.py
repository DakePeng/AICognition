import newspaper


if __name__ == "__main__":
    paper1 = newspaper.build('http://www.sina.com.cn/', language='zh')
    for category in paper1.category_urls():
        print(category)
    for article in paper1.articles:
        article.download()
        article.parse()
        print(article.text)