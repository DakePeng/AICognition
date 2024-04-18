from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def checkResponse(response):
    return response.status_code == 200;

def getParsedHTML(url, header = True):
    response = requests.get(url, headers = headers)
    response.encoding = response.apparent_encoding
    # Check if the request was successful (status code 200)
    if not checkResponse(response):
        print("Failed to retrieve webpage " + url)
        return None
    # Parse the HTML content of the page using BeautifulSoup
    return BeautifulSoup(response.text, 'html.parser')

def printSoupToFile(soup):
    with open("out.txt", "w") as file:
        print(soup.prettify(), file = file)
        
if __name__ == "__main__":
    soup = getParsedHTML("https://blog.google/technology/ai/")
    printSoupToFile(soup)