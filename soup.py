from bs4 import BeautifulSoup as bs
import requests
import re
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tab:
    def __init__(self, URL):
        self.link = URL
        
    def pull_html(self):
        '''
        This function will pull all of the html data from a linked page

        Para,s:
            Self
        Returns:
            HTML content
        '''
        page = requests.get(self.link)
        return page.content
    
    def get_tabs(self):
        '''
        This function takes html content as input and pulls out tabs 

        Input: 
            self
        
        Returns:
            Tabs as .txt file (maybe)
        '''
    
        driver = Chrome()
        driver.get(self.link)

        #wait for page to load
        #wait = WebDriverWait(driver, 10)
        #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tK8GG Ph1Np")))

        #Get page Source
        page_source = driver.page_source
        driver.close()

        #Parse HTML with soup
        soup = bs(page_source, "html.parser")
        #tabs = soup.find(class_ = "fsG7q").find(class_ = 'y68er')
        tabs = [s  for span in soup.select('.fsG7q .y68er') for s in span.stripped_strings]

        
        
        
        return tabs
    
if __name__ == "__main__":
    
    XO = Tab('https://tabs.ultimate-guitar.com/tab/eden-the-eden-project/xo-tabs-1729693')
    
    print(XO.get_tabs())