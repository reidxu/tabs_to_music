from tab import Tab
from sheet import Sheet

def spaghetti(songname, URL):
    #Initialize Tab object
    tab_obj = Tab(songname,URL)
    #Pull and wrap up the tabs
    wrapped  = tab_obj.wrap()
    sheet_obj = Sheet(songname, wrapped)
    final_convert = ''
    for single_tab in wrapped:
        dict_to_guido = sheet_obj.dict_to_guido(single_tab)
        final_convert = final_convert + dict_to_guido
    final_convert = final_convert + ']'
    final_convert = '[' + final_convert
    print(final_convert)
    sheet_obj.input_noteserver(final_convert)

if __name__ == "__main__":
    spaghetti('twinkle','https://tabs.ultimate-guitar.com/tab/misc-children/twinkle-twinkle-little-star-tabs-605822')
    #spaghetti('Happy Birthday', 'https://tabs.ultimate-guitar.com/tab/misc-traditional/happy-birthday-tabs-42938')