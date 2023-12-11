'''
This code will take guido notation and input it into 
noteserver.org to get the converted sheet music
'''

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tab import Tab

class Sheet:
    def __init__(self, songname, tab):
        self.songname = songname
        self.tab = tab
        
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
    
    def wrap(self):
        '''
        This code will wrap up every 6 elements of the tab list into its own sublist 
        
        Input:   
        tab **list**
            List of full tab straight from UG
        '''
        sublist = 6

        # Use list comprehension to create sublists
        wrapped = [self.tab[i:i+sublist] for i in range(0, len(self.tab), sublist)]
        return wrapped
    
    def find_pos(self, start, step):
        '''
        This function finds the next position based off the starting point
        and the amount of half steps up. Returns the guido note string.
        '''
        scale = {1:'c', 2:'c#', 3:'d', 4:'d#', 5:'e', 6:'f', 7:'f#', 8:'g', 9:'g#', 10:'a', 11:'a#', 12:'b'}
        length_scale  = 12
        position = (step-(length_scale-start)) % length_scale 
        note  =  scale[position]
        octave_loops = step // length_scale #count how many loops were taken
        return note, octave_loops

    def translate_single(self):
        '''
        This function will translate a single tab of 6 strings
        single_tab format: [e, B, G, D, A, E]

        Returns: 
            notes  **dict**
                Dictionary of {position of note : letter  of note} format
        '''
        
        scale = {1:'c', 2:'c#', 3:'d', 4:'d#', 5:'e', 6:'f', 7:'f#', 8:'g', 9:'g#', 10:'a', 11:'a#', 12:'b'}
        scale_rev = {'c':1, 'c#':2, 'd':3, 'd#':4, 'e':5, 'f':6, 'f#':7, 'g':8, 'g#':9, 'a':10, 'a#':11, 'b':12}
        notes = {}
        single_tab = self.tab
        for num_string in range(6):
            string = single_tab[num_string]
            note_string = string[0] #this is the start
        
            if note_string == 'E':
                start_octave = 4
            if note_string in ['B', 'G', 'D']:
                start_octave  = 3
            if note_string in ['e', 'A']:
                start_octave = 2

            list_string = []
            for i in string:
                list_string.append(i)
            
            list_string.pop(0)
            
            list_string.pop(0)


            #list_string is now ['-', '-', '5', '-' ....] 
            
            count = 0
            for i in range(len(list_string)):
            
                if list_string[i].isnumeric() == False:
                    count+= 1 #Check how many non notes come before each note for a specific string. This allows for timing
                elif list_string[i].isnumeric() == True:
                    #If the space in the tab is a note, convert it to the musical letter
                    note_num = int(list_string[i])
                    start = scale_rev[note_string.lower()]
                    note, octave_loops = self.find_pos(start, note_num)
                    notes[count] = note + str(octave_loops + start_octave)
                    
        return notes
    def dict_to_guido(self):
        '''
        This function takes the output of translate_single and puts it in guido notation
        '''
        note_dict =  self.translate_single()
        positions = sorted(note_dict.keys())

        mega_string  = ''
        for i in positions:
            mega_string += '{} '.format(note_dict[i])
        mega_string =  '[' + mega_string
        mega_string  = mega_string + ']'
        return mega_string
        
            

                

    
if __name__  == "__main__":
    guido = '[a b c]'
    isohel_tab = Tab('Isohel', 'https://tabs.ultimate-guitar.com/tab/eden-the-eden-project/isohel-tabs-2954888')
    XO = Tab('XO','https://tabs.ultimate-guitar.com/tab/eden-the-eden-project/xo-tabs-1729693')
    twinkle = Tab('twinkle', 'https://tabs.ultimate-guitar.com/tab/misc-children/twinkle-twinkle-little-star-tabs-605822')
    #tabs  = XO.clean_tabs()
    #XO_sheet  = Sheet('XO', tabs)
    #wrapped = XO_sheet.wrap()
    
    tab_single = ['e|------6-----------5---------------6----------5-------------------------------|', 
        'B|-----------6-----------5--------------6----------5-5h6p5---------------------|', 
        'G|--------------------------------------------------------5--------------------|', 
        'D|--2/5---------1/3-------------2/5--------1/3---------------------------------|', 
        'A|---------5-----------3--------------5----------3-----------------------------|', 
        'E|-----------------------------------------------------------------------------|']
    
    test = Sheet('test_sheet', tab_single)
    print(test.dict_to_guido())

    #test_sheet = Sheet('Test', tabs)
    #test_guido = '[a b c d e {c,e,g}]'
    #test_sheet.input_noteserver(test_guido)
    
