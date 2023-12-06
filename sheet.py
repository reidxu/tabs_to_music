'''
This code will take guido notation and input it into 
noteserver.org to get the converted sheet music
'''

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Sheet:
    def __init__(self, songname):
        self.songname = songname
       
    def input_noteserver(self, guido):
        '''
        Takes in a string and opens noteserver.org to type in the string
        '''
        driver = Chrome()
        driver.get('http://www.noteserver.org/noteserver.html')
        inputter = driver.find_element(By.ID, "gmnSandbox")
        inputter.send_keys(guido)
        inputter.send_keys(Keys.ENTER)

        with open('{}_sheet_music.png'.format(self.songname), 'wb') as f:
            f.write(driver.find_element(By.ID, 'canvasContainer').screenshot_as_png)

        return

if __name__  == "__main__":
    guido = '[a b c]'
    isohel = Sheet('isohel')
    isohel.input_noteserver(guido)
