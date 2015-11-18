# for python3
# from tkinter import *
# from tkinter import ttk

from Tkinter import *
import ttk

import speech_recognition as sr

PUZZLE_SIZE = 5
PUZZLE_ROWS = ["DUCKP","OOLPA","GREEN","FGCMT","EDKLF"]
PUZZLE_COLUMNS = [[] for i in range(0,PUZZLE_SIZE)]
PUZZLE_ITEM_CONTAINER = [["*"]*PUZZLE_SIZE for i in range(0,PUZZLE_SIZE)]

for i in xrange(0, PUZZLE_SIZE):
    temp=""
    for j in xrange(0,PUZZLE_SIZE):
        temp+=PUZZLE_ROWS[j][i]
    PUZZLE_COLUMNS[i] = temp

class Puzzle:
    
    def __init__(self, master):    
    
        SEARCH_STRING = "ERROR"

        '''header'''
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        ttk.Label(self.header_frame, text = "You Said : ").pack(side = LEFT,padx=5)
        self.voice_text_field = Entry(self.header_frame, width = 15)
        self.voice_text_field.pack(side=LEFT)

        self.speak_button = ttk.Button(self.header_frame,text="SPEAK" ,command = lambda : self.speak_button_clicked(SEARCH_STRING))
        self.speak_button.pack(side=LEFT)


        '''board'''
        self.board_frame = ttk.Frame(master)
        self.board_frame.pack()

        for i in xrange(0, PUZZLE_SIZE):
            for j in xrange(0, PUZZLE_SIZE):    
                PUZZLE_ITEM_CONTAINER[i][j] = ttk.Label(self.board_frame, text = PUZZLE_ROWS[i][j])
                PUZZLE_ITEM_CONTAINER[i][j].grid(row=i,column=j,padx=15,pady=15)

                
        '''footer'''
        self.footer_frame = ttk.Frame(master)
        self.footer_frame.pack()

        ttk.Label(self.footer_frame, text = "Result : ").pack(side = LEFT,padx=5)
        self.result_text_field = Entry(self.footer_frame, width = 10)
        self.result_text_field.pack(side=LEFT)


    def speak_button_clicked(self,SEARCH_STRING):
        SEARCH_STRING = get_spoken_word().upper()
        self.voice_text_field.delete(0,END)
        self.voice_text_field.insert(0,SEARCH_STRING)

        '''search_rows'''
        self.row_search(SEARCH_STRING)

        '''search_columns'''
        self.column_search(SEARCH_STRING)
        

    def row_search(self,SEARCH_STRING):
        for i in xrange(0,PUZZLE_SIZE):
            start_index = PUZZLE_ROWS[i].find(SEARCH_STRING)
            if(start_index>-1):
                for j in xrange(0,len(SEARCH_STRING)):
                    PUZZLE_ITEM_CONTAINER[i][start_index+j].config(background="Yellow")
                break
    
    def column_search(self,SEARCH_STRING):
        for i in xrange(0,PUZZLE_SIZE):
            start_index = PUZZLE_COLUMNS[i].find(SEARCH_STRING)
            if(start_index>-1):
                for j in xrange(0,len(SEARCH_STRING)):
                    PUZZLE_ITEM_CONTAINER[start_index+j][i].config(background="Yellow")
                break


def get_spoken_word():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    text = ""

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said " + r.recognize_google(audio))
        text = r.recognize_google(audio)

    except sr.UnknownValueError:
        print("Could not understand audio")
        text = "Could not understand"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return text

def main():            
    
    root = Tk()
    puzzle = Puzzle(root)
    root.mainloop()
    
if __name__ == "__main__": main()