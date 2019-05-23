import tkinter as tk
import tkFont as tkfont
from tkinter.messagebox import * 
from card_class import Card
from deck_class import Deck
import time

my_deck=Deck()





### CREATION OF THE SAMPLE APP CLASS ###
# it enables us to change for one window to another and to come back to the first window #

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
        
        #loop with all the windows we want to ba able to access# 
        for F in (StartPage, AddCard, EditCard, DeleteCard, PrintCard, LoadDeck, SaveDeck):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoadDeck")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
        
        
        
        
        
### CREATION OF THE FIRST WINDOW CLASS ###
# it will contain all the access to the ohter windows #

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='#D2F081') #adding color
        label = tk.Label(self, text="What do you want to do?", font=controller.title_font, bg='#D2F081') #asking question
        label.pack(side="top", fill="x", pady=10)
	
	#creating the buttons to access the other windows
        button1 = tk.Button(self, text="Add a card", command = lambda : controller.show_frame("AddCard"),bg='#B2ED11')
        button2 = tk.Button(self, text="Edit a card", command = lambda : controller.show_frame("EditCard"),bg='#B2ED11')
        button3 = tk.Button(self, text="Delete a card", command = lambda : controller.show_frame("DeleteCard"),bg='#B2ED11')
        button4 = tk.Button(self, text="Print a card", command = lambda : controller.show_frame("PrintCard"),bg='#B2ED11')
        button5 = tk.Button(self, text="Load a deck", command = lambda : controller.show_frame("LoadDeck"),bg='#B2ED11')
        button6 = tk.Button(self, text="Save a deck", command = lambda : controller.show_frame("SaveDeck"),bg='#B2ED11')
        button7 = tk.Button(self, text="Quit", command = self.quit,bg='#8ABC00')
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()
        
    def quit(self):
    	exit()
    	
    	
    	
    	


### CREATION OF THE OTHER WINDOWS: ###
###				   ###
### ADD CARD WINDOW		   ###
### EDIT CARD WINDOW		   ###
### DELETE CARD WINDOW		   ###
### PRINT CARD WINDOW		   ###
### LOAD DECK WINDOW		   ###
### SAVE DECK WINDOW		   ###


class AddCard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='#D2F081')
        label = tk.Label(self, text="Add a card", font=controller.title_font,bg='#D2F081')
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"),bg='#8ABC00')
	button.pack()
	
	identifier = tk.StringVar()
	topside = tk.StringVar()
	backside = tk.StringVar()
	
	label1 = tk.Label(self, text= "Identifier", bg='#D2F081')
	entry1 = tk.Entry(self, textvariable=identifier)
	label2 = tk.Label(self, text="Topside", bg='#D2F081')
	entry2 = tk.Entry(self, textvariable=topside)
	label3 = tk.Label(self, text="Backside", bg='#D2F081')
	entry3 = tk.Entry(self, textvariable=backside)
	
	label1.pack()
	entry1.pack()
	label2.pack()
	entry2.pack()
	label3.pack()
	entry3.pack()
	
	button2 = tk.Button(self, text = "Add", command = lambda : self.add_card(identifier.get(),topside.get(),backside.get()), bg='#B2ED11')
	button2.pack()
	
    def add_card(self,identifier,topside,backside):
    	existence=False
    	
    	for c in my_deck.cards:
		if c.identifier==identifier:
			showinfo("Info!","This card already exists!")
			existence=True
			
	if existence==False:
		if identifier== '' or topside == '' or backside == '':
			showinfo("Info!","All arguments need to be completed")
    		else:
    			my_deck.add_card_to_deck(identifier,"Waste",topside,backside)
			showinfo("Info!","Your card has been correctly added, now you have " + str(len(my_deck.cards)) + " cards in the deck")
			
			
			
			
			
	
class EditCard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='#D2F081')
        label = tk.Label(self, text="Edit a card", font=controller.title_font, bg='#D2F081')
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"),bg='#8ABC00')
        button.pack()
        
        identifier = tk.StringVar()
	edited_attribute = tk.StringVar()
	change = tk.StringVar()
	
	label1 = tk.Label(self, text= "Identifier", bg='#D2F081')
	entry1 = tk.Entry(self, textvariable=identifier)
	label2 = tk.Label(self, text="Edited attribute (to choose between: identifier - subject - topside - backside)", bg='#D2F081')
	entry2 = tk.Entry(self, textvariable=edited_attribute)
	label3 = tk.Label(self, text="Change", bg='#D2F081')
	entry3 = tk.Entry(self, textvariable=change)
	
	label1.pack()
	entry1.pack()
	label2.pack()
	entry2.pack()
	label3.pack()
	entry3.pack()
	
	button2 = tk.Button(self, text = "Edit", command = lambda : self.editing_card(identifier.get(),edited_attribute.get(),change.get()), bg='#B2ED11')
	button2.pack()
	
    def editing_card(self,identifier,attribute,change):
    	existence=False
    	
    	if my_deck.cards==[]:
    		existence=True
    		showinfo("Info","Empty deck: you should add cards first!")
    	else:    	
		for c in my_deck.cards:
			if c.identifier==identifier:
				existence=False
			else:
				existence=True
			
			
	if existence==False:	
		if identifier== '' or attribute == '' or change == '':
			showinfo("Info!","All arguments need to be completed")	
		elif attribute=='identifier' or attribute=='topside' or attribute=='backside' or attribute=='subject' or attribute=='review' or attribute=='position':
			my_deck.edit_card(identifier,attribute,change)
			showinfo("Info!","The card has been succesfully edited!")
		else: 
			showinfo("Info!","This attribute does not exist!")
	else:
		showinfo("Info!","This card does not exist!")
	
	
	
	
	
	
	
	
	
	
	
class DeleteCard(tk.Frame):
	
    def __init__(self, parent, controller):
    	tk.Frame.__init__(self,parent)
    	self.controller = controller
    	self.config(bg='#D2F081')
    	label = tk.Label(self, text="Delete a card", font=controller.title_font, bg='#D2F081')
    	label.pack(side="top", fill="x", pady=10)
    	button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"),bg='#8ABC00')
    	button.pack()
    	
    	identifier = tk.StringVar()
    	label1 = tk.Label(self, text= "Identifier", bg='#D2F081')
	entry1 = tk.Entry(self, textvariable=identifier)
	label1.pack()
	entry1.pack()
	button2 = tk.Button(self, text = "Delete", command = lambda : self.deleting_card(identifier.get()), bg='#B2ED11')
	button2.pack()
	
    def deleting_card(self,identifier):
    	existence=False
    	
    	if my_deck.cards==[]:
    		existence=True
    		showinfo("Info","Empty deck: you should add cards first!")
    	else:    	
		for c in my_deck.cards:
			if c.identifier==identifier:
				existence=False
			else:
				existence=True
			
	if existence == False:
    		my_deck.delete_card_from_deck(identifier)
    		showinfo("Info!","The card has been deleted, you now have " + str(len(my_deck.cards)) + " cards")
    	else:
    		showinfo("Info!","This card does not exist or you haven't choose a card")
	
	
	
	
	
	
	
	
	
	
	
	
class PrintCard(tk.Frame):
	
    def __init__(self, parent, controller):
    	tk.Frame.__init__(self,parent)
    	self.controller = controller
    	self.config(bg='#D2F081')
    	label = tk.Label(self, text="Print a card", font=controller.title_font, bg='#D2F081')
    	label.pack(side="top", fill="x", pady=10)
    	button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"),bg='#8ABC00')
    	button.pack()
    	
    	identifier = tk.StringVar()
    	label1 = tk.Label(self, text= "Identifier", bg='#D2F081')
	entry1 = tk.Entry(self, textvariable=identifier)
	label1.pack()
	entry1.pack()
	button2 = tk.Button(self, text = "Print", command = lambda : self.print_card(identifier.get()), bg='#B2ED11')
	button2.pack()
	
    def print_card(self,identifier):
    	existence=False
    	my_card=Card("id_card","Waste","topside","backside")
    	
      	if my_deck.cards==[]:
    		showinfo("Info","Empty deck: you should add cards first!")
    	else:	
    		for c in my_deck.cards:
			if c.identifier==identifier:
				existence=False
				my_card.identifier=c.identifier
				my_card.subject=c.subject
				my_card.topside=c.topside
				my_card.backside=c.backside
				break
			else:
				existence=True
				
	if existence==False:
		showinfo("Here is your card","id: " + identifier + "\ntopside: " + my_card.topside + "\nbackside: " + my_card.backside)
	else:
		showinfo("Info!","This card does not exist or you haven't choose a card")
		
		
		
		
		
		
		
		
				
class LoadDeck(tk.Frame):
	
    def __init__(self, parent, controller):
    	tk.Frame.__init__(self,parent)
    	self.controller = controller
    	self.config(bg='#D2F081')
    	label = tk.Label(self, text="Load a deck", font=controller.title_font, bg='#D2F081')
    	label.pack(side="top", fill="x", pady=10)
    	button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"), bg='#8ABC00')
    	button.pack()
		
    	deckname = tk.StringVar()
    	label1 = tk.Label(self, text= "Name of the deck", bg='#D2F081')
	entry1 = tk.Entry(self, textvariable=deckname)
	label1.pack()
	entry1.pack()
	button2 = tk.Button(self, text = "Load", command = lambda : self.load_deck(deckname.get()), bg='#B2ED11')
	button2.pack()
	
    def load_deck(self,deckname):
    	filename=deckname + '.pickle'
	my_deck.load_the_deck(filename)
	showinfo("Info!", "your deck has been correctly loaded, it contains " + str(len(my_deck.cards)) + " cards")
	
	
	
	
	
	
	
	
	
	
class SaveDeck(tk.Frame):
	
    def __init__(self, parent, controller):
    	tk.Frame.__init__(self,parent)
    	self.controller = controller
    	self.config(bg='#D2F081')
    	label = tk.Label(self, text="Save a deck", font=controller.title_font, bg='#D2F081')
    	label.pack(side="top", fill="x", pady=10)
    	button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"), bg='#8ABC00')
    	button.pack()
		
    	deckname = tk.StringVar()
    	label1 = tk.Label(self, text= "Name of the deck",bg='#D2F081')
	entry1 = tk.Entry(self, textvariable=deckname)
	label1.pack()
	entry1.pack()
	button2 = tk.Button(self, text = "Save", command = lambda : self.save_deck(deckname.get()), bg='#B2ED11')
	button2.pack()
	
    def save_deck(self,deckname):
    	if deckname == '':
    		showinfo("Info!","You need to choose a deck!")
    	else:
    		filename=deckname + '.pickle'
		my_deck.save_the_deck(filename)
		showinfo("Info!","your deck has been correctly saved")
	

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

