# for python3
# from tkinter import *
# from tkinter import ttk

from Tkinter import *
import ttk

import speech_recognition as sr

PUZZLE_SIZE = 3
PUZZLE_ROWS = ["ABC","DEF","GHI"]
PUZZLE_COLUMNS = [""]*PUZZLE_SIZE
print PUZZLE_ROWS
print PUZZLE_COLUMNS
PUZZLE_ITEM_CONTAINER = [["*"]*PUZZLE_SIZE for i in range(0,PUZZLE_SIZE)]

# for i in xrange(0, PUZZLE_SIZE):
#     for j in xrange(0,PUZZLE_SIZE):
#         PUZZLE_COLUMNS[j][i]=PUZZLE_ROWS[i][j]
print PUZZLE_ROWS
print PUZZLE_COLUMNS


class Puzzle:

    def __init__(self, master):    
    
        '''header'''
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        ttk.Label(self.header_frame, text = "You Said : ").pack(side = LEFT,padx=5)
        voice_text_field = Entry(self.header_frame, width = 15)
        voice_text_field.pack(side=LEFT)


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
        result_text_field = Entry(self.footer_frame, width = 10)
        result_text_field.pack(side=LEFT)

        '''search'''
        SEARCH_STRING = get_spoken_word() 
        
        '''search_rows'''
        for i in xrange(0,PUZZLE_SIZE):
            start_index = PUZZLE_ROWS[i].find(SEARCH_STRING)
            if(start_index>-1):
                for j in xrange(0,len(SEARCH_STRING)):
                    PUZZLE_ITEM_CONTAINER[i][j].config(background="Yellow")
                break

        '''search_columns'''
            #TODO


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