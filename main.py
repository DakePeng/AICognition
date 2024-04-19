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

def scrapeOpenAIBlog():
    type = "OpenAI_Blog"
    print("Scraping OpenAI Blog Posts")
    links = scrapeOpenAIBlogLinks()
    postList = scrapeArticleList(links)
    fail, all = print_list_to_csv(type, postList)
    print("Successfully scraped " + str (all - fail) + " out of " + str(all) + " posts ")

def scrapeOpenAIResearch():
    type = "OpenAI_Research"
    print("Scraping OpenAI Research Posts")
    links = scrapeOpenAIResearchLinks()
    postList = scrapeArticleList(links)
    fail, all = print_list_to_csv(type , postList)
    print("Successfully scraped " + str (all - fail) + " out of " + str(all) + " posts ")

def scrapeAnthropicBlog():
    type = "Anthropic_Blog"
    print("Scraping Anthropic Blog Posts")
    links = scrapeAnthropicBlogLinks()
    postList = scrapeArticleList(links)
    fail, all = print_list_to_csv(type, postList)
    print("Successfully scraped " + str (all - fail) + " out of " + str(all) + " posts ")

def scrapeAnthropicNews():
    type = "Anthropic_News"
    print("Scraping Anthropic News Posts")
    links = scrapeAnthropicNewsLinks()
    postList = scrapeArticleList(links)
    fail, all = print_list_to_csv(type, postList)
    print("Successfully scraped " + str (all - fail) + " out of " + str(all) + " posts ")
    
def scrapeMicrosoftNews():
    type = "Microsoft_News"
    print("Scraping Microsoft News Posts")
    links = scrapeMicrosoftNewsLinks()
    postList = scrapeArticleList(links)
    fail, all = print_list_to_csv(type, postList)
    print("Successfully scraped " + str (all - fail) + " out of " + str(all) + " posts ")

def scrapeMetaBlog():
    type = "Meta_Blog"
    print("Scraping Meta Blog Posts")
    links = scrapeMetaBlogLinks()
    print("links obtained")
    postList = scrapeArticleList(links)
    fail, all = print_list_to_csv(type, postList)
    print("Successfully scraped " + str (all - fail) + " out of " + str(all) + " posts ")

 
def consolidateCSV(outputFileName, delete = False):
    folder_path = "Temp/"
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    merged_data = pd.DataFrame()
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        merged_data = merged_data._append(df, ignore_index=True)
        if delete: os.remove(file_path)
    output_file_path = outputFileName
    merged_data.to_csv(output_file_path, index=False)
    
def createTempFolder():
    folder_path = os.path.join(os.getcwd(), "Temp")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

if __name__ == "__main__":
    # createTempFolder()
    # scrapeAnthropicNews()
    # scrapeOpenAIBlog()
    # scrapeOpenAIResearch()
    # scrapeAnthropicBlog()
    # scrapeMicrosoftNews()
    # scrapeMetaBlog()

