
from card_class import Card
from deck_class import Deck
from review_list import to_be_reviewed

import tkinter as tk
import tkFont as tkfont
from tkinter.messagebox import *

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
        for F in (StartPage, PageTwo, Train):
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
        self.config(bg='#D2F081') 

        global my_deck
        my_deck=Deck()
        my_deck.load_the_deck('first_deck.pickle')
        today=datetime.datetime.now()
        global a_revoir
        a_revoir=to_be_reviewed(my_deck, today)
        random.shuffle(a_revoir)

        label = tk.Label(self, text="Start today session ? Only %s cards to review" %(len(a_revoir)), font=controller.title_font, bg='#D2F081')
        label.pack(side="top", fill="x", pady=10)

        button_start = tk.Button(self, text="Start",
                            command= lambda: controller.show_frame("Train"))
        button_quit = tk.Button(self, text="Quit",
                            command= self.quit, bg='#8ABC00')
        
        button_start.pack()
        button_quit.pack()
        






class Train(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='#D2F081') 
        global succes
        global echecs
        global L
        global attributs
        succes = 0
        echecs = 0
        L = 0
        attributs = []
        self.train()


    def train(self):

        global attributs
        global succes, echecs, L
        self.clean(attributs)
        attributs = []
	
	if len(a_revoir)!=0:
        	card = a_revoir[0]
                L +=1
     
        	label = tk.Label(self, text="What is the bin adapted for this waste : %s ?" %(card.topside), font=self.controller.title_font, bg='#D2F081')
        	label.pack()

       		button_recy = tk.Button(self, text="Recyclage", command = lambda : self.answer('R', card))
       		button_comp = tk.Button(self, text="Compost", command = lambda : self.answer('C', card))
        	button_verre = tk.Button(self, text="Verre", command = lambda : self.answer('V', card))
        	button_bou = tk.Button(self, text="Bouchon", command = lambda : self.answer('B', card))
        	button_cen = tk.Button(self, text="Cendrier", command = lambda : self.answer('M', card))
        	button_elec = tk.Button(self, text="Electronique", command = lambda : self.answer('E', card))
        	button_piles = tk.Button(self, text="Piles", command = lambda : self.answer('P', card))
        	button_relais = tk.Button(self, text="Relais", command = lambda : self.answer('T', card))
        	button_amp = tk.Button(self, text="Ampoules", command = lambda : self.answer('A', card))
        	button_ordmen = tk.Button(self, text="Ordures menageres", command = lambda : self.answer('O', card))	
        	button_quit = tk.Button(self, text="Quit", command=self.quit, bg='#8ABC00')


        	attributs = [label, button_recy, button_quit, button_comp, button_verre, button_bou, button_cen, button_elec, button_piles, button_relais, button_amp, button_ordmen]

        	button_recy.pack()
        	button_comp.pack()
        	button_verre.pack()
        	button_bou.pack()
        	button_cen.pack()
        	button_elec.pack()
        	button_piles.pack()
        	button_relais.pack()
        	button_amp.pack()
        	button_ordmen.pack()
        	button_quit.pack()


    

    def answer(self, ans, card):
        global succes, echecs, L

        if ans==card.backside:
            succes = succes +1
	    ps = int((float(succes)/L)*100)
	    pe = int((float(echecs)/L)*100)
            showinfo("Info", "Brilliant ! You learn so fast ! \n %s %% of good answers and only %s %% of wrong ones" %(ps, pe))
            card.position +=1
        else :
            echecs = echecs +1
	    ps = int((float(succes)/L)*100)
	    pe = int((float(echecs)/L)*100)
            showinfo("Info", "Owowow... %s was expected \n %s %% of good answers and only %s %% of wrong ones" %(card.backside, ps, pe))
            card.position = 0

        card.date=datetime.datetime.now()
        card.review=False
        a_revoir.pop(0)
        if len(a_revoir)!=0:
            self.train()
        else : 
            my_deck.save_the_deck('first_deck.pickle') 
            self.controller.show_frame("PageTwo")




    def clean(self, attributs):
        for i in attributs :
            i.destroy()
        





    def quit(self):
        my_deck.save_the_deck('first_deck.pickle')
        showinfo("Info", "Don't forget to come back to finish the session !")
        exit()



        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Today session is over ! Congratulations !!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()





