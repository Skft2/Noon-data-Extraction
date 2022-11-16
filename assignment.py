from operator import ne
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")

product_url = []
def links():
    link = driver.find_elements(By.XPATH, value='//span[@class="sc-5e739f1b-0 gEERDr wrapper productContainer  "]/a["href"]')
    for i in link:
        print(i.get_attribute('href'))
        product_url.append(i.get_attribute('href'))

for i in range(1,65):
    url = f"https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page={i}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc"

    driver.get(url)
    time.sleep(1)
    links()

    

print(len(product_url))
driver.quit()