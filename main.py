import csv
import os
import shutil
import pandas as pd
from get_article_urls import *
from get_article_content import *

def print_list_to_csv(type, postList):
    fail = 0
    csvPath = "Temp/" + type + ".csv"
    with open(csvPath, 'a', newline='') as file:
        writer = csv.writer(file)
        header = ["affiliation", "postLink", "researchLink", "title", "text"]
        writer.writerow(header)
        for post in postList:
            article = post.Article
            if article.text == "": 
                fail += 1
                continue
            writer.writerow([type, article.url, post.researchUrl, article.title, article.text])
    return fail, len(postList)

if __name__ == "__main__":
    # createTempFolder()
    # scrapeAnthropicNews()
    # scrapeOpenAIBlog()
    # scrapeOpenAIResearch()
    # scrapeAnthropicBlog()
    # scrapeMicrosoftNews()
    # scrapeMetaBlog()
    # consolidateCSV("result.csv")
