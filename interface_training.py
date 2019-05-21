
from card_class import Card
from deck_class import Deck
from review_list import to_be_reviewed

import tkinter as tk
import tkFont as tkfont
import time
import datetime
import random




class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        global attributs
        global my_deck
        my_deck=Deck()
        my_deck.load_the_deck('first_deck.pickle')
        today=datetime.datetime.now()
        global a_revoir
        a_revoir=to_be_reviewed(my_deck, today)
        random.shuffle(a_revoir)

        label = tk.Label(self, text="Start today session ? Only %s cards to review" %(len(a_revoir)), font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button_start = tk.Button(self, text="Start",
                            command=self.train)
        button_quit = tk.Button(self, text="Quit",
                            command=self.quit)
        attributs=[label, button_start, button_quit]
        button_start.pack()
        button_quit.pack()
        

    def train(self):
        while len(a_revoir)>0:
            card=a_revoir[0]
            self.clean(attributs)
            self.train_one_card(card)
            
            a_revoir.pop()

    def quit(self):
        exit()

    def train_one_card(card):
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

    def clean(attributs):
        for i in attributs:
            i.destroy()
        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        
        
        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()








#class Train(tk.Frame):
#
#def __init__(self, parent, controller):
#tk.Frame.__init__(self, parent)
#self.controller = controller
#self.answer=tk.StringVar()
#
#
#while len(a_revoir)>0:
#card=a_revoir[0]
#label = tk.Label(self, text="Quelle est la poubelle adaptee a ce dechet : %s ?" %(card.topside))
#label.pack(side="top", fill="x", pady=10)
#		
#recyclage_button = tk.Button(self, text="R- Recyclage", command=self.recyclage(card.backside))
#recyclage_button.pack()
#		
#compost_button = tk.Button(self, text="C- Compost", command=self.compost(card.backside))
#compost_button.pack()
#
#verre_button = tk.Button(self, text="V- Verre", command=self.verre(card.backside))
#verre_button.pack()
#
#bouchon_button = tk.Button(self, text="B- Bouchon", command=self.bouchon(card.backside))
#bouchon_button.pack()
#
#cendrier_button = tk.Button(self, text="M- Cendrier", command=self.cendrier(card.backside))
#cendrier_button.pack()
#
#electronic_button = tk.Button(self, text="E- Electronique", command=self.electronic(card.backside))
#electronic_button.pack()
#			
#piles_button = tk.Button(self, text="P- Piles", command=self.piles(card.backside))
#piles_button.pack()
#
#ordures_button = tk.Button(self, text="O- Ordures menageres", command=self.ordures(card.backside))
#ordures_button.pack()
#
#quit_button = tk.Button(self, text="Quit", command=self.quit)
#quit_button.pack()
#
#
#			
#a_revoir.pop()
			
#for item in ["Recyclage", "Compost", "Verre", "Bouchon", "Cendrier", "Electronique", "Piles", "Ordures menageres"]:
			
#def recyclage(self, backside):
#self.answer.set()
#if backside=='R':
#label = tk.Label(self, text="Yeah !! Brilliant ! You learn so fast !")
#label.pack()
#else :
#label = tk.Label(self, text="Owowo... That was not what was expected... %s was expected" %(backside))
#label.pack()

# To include images we need to use PIL (Python Image Library)
# from PIL import Image, ImageTk



"""Method to display an image."""
#	img = Image.open('flowers.jpg')
#	render = ImageTk.PhotoImage(img)
#	imag = tk.Label(self.master, image=render)
#	imag.image = render
#	imag.grid(row=3, column=0, columnspan=2)
