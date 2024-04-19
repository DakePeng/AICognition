from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urljoin
from bs4_handle_helper import * 

url = "https://ai.meta.com/blog"
buttonXPath = """/html/body/div/div/div[2]/div/div[8]/div/div[4]/button"""
driver = webdriver.Chrome()
driver.get(url)
def click_load_more():
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, buttonXPath))
        )
        load_more_button.click()
    except:
        print("No more content to load or button not found")
        return False
    return True
# Click the "Load More" button repeatedly until no more content is loaded
while True:
    if not click_load_more(): break

soup = BeautifulSoup(driver.page_source, "html.parser")
with open("Meta_Blog_Site.txt", "w") as file:
    print(soup, file = file)
    
postClasses = soup.find_all(class_ = "_amtj")
allLinks = []
for postClass in postClasses:
    postLinks = postClass.find_all('a')
    for link in postLinks:
        link = [urljoin(url, link.get('href')), None]
        allLinks.append(link)
        
with open("Meta_Blog_Links.txt", "w") as file:
    print(allLinks, file = file)