from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def checkResponse(response):
    return response.status_code == 200;

def getSoup(url, header = True):
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
        

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def getSoupWithWebDriver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return soup

def getSoupWithInfiniteScroll(url, buttonXPath): 
    driver = webdriver.Chrome()
    driver.get(url)
    startTime = time.time()
    def click_load_more():
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button = WebDriverWait(driver, 20).until(
                 EC.element_to_be_clickable((By.XPATH, buttonXPath))
            )
            button.click()
            time.sleep(0.3)
        except:
            print("No more content to load or button not found")
            return False
        return True

    # Click the "Load More" button repeatedly until no more content is loaded
    while True:
        if not click_load_more(): break
        timer = time.time() - startTime
        if timer > 60: 
            print("session timed out")
            break
    
    # Once all content is loaded, extract data with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # Finally, close the browser
    driver.quit()
    return soup


if __name__ == "__main__":
    #soup = getParsedHTMLWithInfiniteScroll("https://ai.meta.com/blog", """//*[@id="facebook"]/body/div/div/div[2]/div/div[8]/div/div[4]/button""")
    soup = getSoupWithWebDriver("https://openai.com/blog?page=4")
    printSoupToFile(soup)
    