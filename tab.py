from bs4 import BeautifulSoup as bs
import requests
import re
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np


class Tab:
    def __init__(self, songname, URL):
        self.link = URL
        self.songname  =  songname
    def get_tabs(self):
        '''
        This function takes html content as input and pulls out tabs 

        Input: 
            self
        
        Returns:
            Tabs as a list where each element is a string of a guitar, every 6 elements is a block
        '''
    
        driver = Chrome()
        driver.get(self.link)

        #Get page Source
        page_source = driver.page_source
        driver.close()

        #Parse HTML with soup
        soup = bs(page_source, "html.parser")
        
        #Output tabs where each line is an element in a list
        nasty_tabs = [s  for span in soup.select('.fsG7q .y68er') for s in span.stripped_strings]
        return nasty_tabs
    
    def clean_tabs(self):
        '''
        Clean up tabs from get_tabs()

        Input: 
            Self

        Returns:
            cleaned_tabs  **list**:
                list of cleaned tabs
        '''
        cleaned_tabs = []

        #Clean up the list
        for line in self.get_tabs():
            if line[1] == '|':
                #print(line)
                cleaned_tabs.append(line)
        
        return cleaned_tabs
    
    def tab_to_arr(self): 
        '''
        Convert cleaned tab list to array grouped as six
        '''
        tab_arr = np.array(self.clean_tabs())
        tab_arr = tab_arr.reshape(-1,1)
        tab_arr = tab_arr.reshape(-1,6)
        return tab_arr
    
    def tabs_to_txt(self):
        '''
        This function uses the get_tabs() output and writes it to a txt file 
        formatted for later parsing, or just for fun
        '''
       
       
        clean_tabs = self.clean_tabs()
  
        
        with open('{}.txt'.format(self.songname), 'w') as f:
            for line in clean_tabs:
                f.write(line)
                f.write('\n')
        f.close()
        return 



    
if __name__ == "__main__":
    
    XO = Tab('XO','https://tabs.ultimate-guitar.com/tab/eden-the-eden-project/xo-tabs-1729693')
    isohel = Tab('Isohel', 'https://tabs.ultimate-guitar.com/tab/eden-the-eden-project/isohel-tabs-2954888')
    rock_roll = Tab('Rock and Roll', 'https://tabs.ultimate-guitar.com/tab/eden-the-eden-project/rock-and-roll-tabs-1869697')
    rock_roll.tabs_to_txt()
   