from card_class import Card
from deck_class import Deck
from review_list import to_be_reviewed

import tkinter as tk
import tkFont as tkfont
from tkinter.messagebox import *
import time
import datetime
import random

my_deck=Deck()

### CREATION OF THE SAMPLE APP CLASS ###
# it enables us to change for one window to another and to come back to the first window #

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        #loop with all the windows we want to ba able to access# 
        for F in (StartPage, StartSession, Train):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        



class StartPage(tk.Frame):
	
    def __init__(self, parent, controller):
    	tk.Frame.__init__(self,parent)
    	self.controller = controller
    	self.config(bg='#D2F081')
    	label = tk.Label(self, text="Load a deck", font=controller.title_font, bg='#D2F081')
    	label.pack(side="top", fill="x", pady=10)
    	button = tk.Button(self, text="Start session", command=lambda: controller.show_frame("StartSession"), bg='#8ABC00')
    	button.pack()
		
    	deckname = tk.StringVar()
    	label1 = tk.Label(self, text= "Name of the deck", bg='#D2F081')
	entry1 = tk.Entry(self, textvariable=deckname)
	label1.pack()
	entry1.pack()
	button2 = tk.Button(self, text = "Load", command = lambda : self.load_deck(deckname.get(), my_deck), bg='#B2ED11')
	button2.pack()
	
    def load_deck(self,deckname, deck):
    	filename=deckname + '.pickle'
	deck.load_the_deck(filename)
	showinfo("Info!", "your deck has been correctly loaded, it contains " + str(len(deck.cards)) + " cards")
	
	
	
	
	
	
	
class StartSession(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='#D2F081') #adding color
        label = tk.Label(self, text="Do you want to start the session? Your deck contains " + str(len(my_deck.cards)) + " cards", font=controller.title_font, bg='#D2F081') 
        label.pack(side="top", fill="x", pady=10)
	
	#creating the buttons to access the other windows
        button1 = tk.Button(self, text="Start", command = lambda : controller.show_frame("Train"),bg='#B2ED11')
        button2 = tk.Button(self, text="Quit", command = self.quit,bg='#8ABC00')
        button1.pack()
        button2.pack()
        
    def quit(self):
    	exit()
    	
    	
    	
    	
    	
class Train(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='#D2F081')
        label = tk.Label(self, text="Training", font=controller.title_font,bg='#D2F081')
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Quit", command=self.quit,bg='#8ABC00')
	button.pack()
	
	
    def quit(self):
    	exit()





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

    	
