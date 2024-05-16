import requests
from urllib.parse import quote
import os
import shutil
import time
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

def downloadHTMLForLinkFile():
    return

def downloadHTML(url, path):
    fileName = quote(url, safe='')
    
    # Make a GET request to the URL
    response = requests.get(url, headers = headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the content to a local file
        with open(path + fileName + ".html", "wb") as f:
            f.write(response.content)
    else:
        print("Failed to download HTML file at" + url + ". Status code:", response.status_code)
        


def createHTMLFolder():
    folder_path = os.path.join(os.getcwd(), "HTML")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

if __name__ == "__main__":
    # createHTMLFolder()
    exampleURls = [
    "https://openai.com/research/gpt-4",
    "https://openai.com/research/weak-to-strong-generalization",
    "https://openai.com/research/efficient-training-of-language-models-to-fill-in-the-middle",
    "https://openai.com/research/formal-math",
    "https://openai.com/research/solving-math-word-problems",
    "https://openai.com/research/openai-five",
    "https://openai.com/research/learning-a-hierarchy",
    "https://openai.com/research/more-on-dota-2",
    "https://openai.com/research/improving-mathematical-reasoning-with-process-supervision",
    "https://openai.com/research/critiques"]
    
    
    downloadHTML("https://openai.com/research/more-on-dota-2", "./HTML/")
    