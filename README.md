# tabs_to_music
 # Background 
 Guitar tabs are written with numbers representing where on the guitar strings to play certain notes. However, most other music is represented pictorally with notes drawn as circles on a series of horizontal lines. To make it easier to play guitar music on other instruments, this code will convert guitar tabs to traditional musical notation. 

 # Methodology
 This program uses web scraping to read the numbers from guitar tabs and translate them to Guido notation, an ASCII based musical notation that can be converted to traditional musical notation.
 
 # Use
 To use this program ensure that Google Chrome and the files sheet.py, tab.py, and spaghetti.py are be installed. Next, navigate to https://www.ultimate-guitar.com/ and find guitar tabs that you want to translate. Copy the link to the tabs and call the spaghetti() function in spaghetti.py. The call should be: spaghetti('songname', 'link'). The program will open two windows: the Ultimate Guitar webpage containing the tabs you want to translate and http://www.noteserver.org/noteserver.html that contains a tool to represent notes pictorally. The music will be saved as in image with the name: "songname_sheet_music.png". A separate text file containing the Guido notation will also be saved as "songname_guido.txt".

# Limitations
This program is currently only applicable to standard guitar tuning and is unable to differentiate different guitar techniques like slides and hammers. Furthermore, this program can not translate chords, so only tabs with no chords will be translated accurately. This code only works on the website Ultimate Guitar and is at the mercy to changes in the HTML of the website. Finally, due to how Note Server works, notes are written on a single row, so long guitar tabs will result in squished and illegible sheet music. However, this issue is mitigated with the translation of tabs to Guido Notation. The translation to Guido Notation is still extremely useful and different programs can be used to translate more legible sheet music. 

# RUNTIME
Please note that due to popups in Ultimate Guitar, the HTML can change and the code will timeout. Alternatively, the webscraping of Ultimate Guitar sometimes will simply take a long time when other times it won't. Be patient when running the code, and if it fails try a few more times and it should work. 

# Examples
Use these functions to try out the code!
Happy Birthday: spaghetti('HBD', 'https://tabs.ultimate-guitar.com/tab/misc-traditional/happy-birthday-tabs-42938')
Twinkle Twinkle Little Star: spaghetti('Twinkle','https://tabs.ultimate-guitar.com/tab/misc-children/twinkle-twinkle-little-star-tabs-605822')
 
