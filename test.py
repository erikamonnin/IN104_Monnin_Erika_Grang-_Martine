import tkinter as tk
import tkFont as tkfont
from tkinter.messagebox import * 
from card_class import Card
from deck_class import Deck
import time

my_deck=Deck()

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
        for F in (StartPage, AddCard, EditCard, DeleteCard, PrintCard):
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
        label = tk.Label(self, text="What do you want to do?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Add a card", command = lambda : controller.show_frame("AddCard"))
        button2 = tk.Button(self, text="Edit a card", command = lambda : controller.show_frame("EditCard"))
        button3 = tk.Button(self, text="Delete a card", command = lambda : controller.show_frame("DeleteCard"))
        button4 = tk.Button(self, text="Print a card", command = lambda : controller.show_frame("PrintCard"))
        button5 = tk.Button(self, text="Quit", command = self.quit)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        
    def quit(self):
    	exit()


class AddCard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add a card", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
	button.pack()
	
	identifier = tk.StringVar()
	topside = tk.StringVar()
	backside = tk.StringVar()
	
	label1 = tk.Label(self, text= "Identifier")
	entry1 = tk.Entry(self, textvariable=identifier)
	label2 = tk.Label(self, text="Topside")
	entry2 = tk.Entry(self, textvariable=topside)
	label3 = tk.Label(self, text="Backside")
	entry3 = tk.Entry(self, textvariable=backside)
	
	label1.pack()
	entry1.pack()
	label2.pack()
	entry2.pack()
	label3.pack()
	entry3.pack()
	
	button2 = tk.Button(self, text = "Add", command = lambda : self.add_card(identifier.get(),topside.get(),backside.get()))
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
			showinfo("Info!","You have" + str(len(my_deck.cards)) + " cards")
	
class EditCard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Edit a card", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        identifier = tk.StringVar()
	edited_attribute = tk.StringVar()
	change = tk.StringVar()
	
	label1 = tk.Label(self, text= "Identifier")
	entry1 = tk.Entry(self, textvariable=identifier)
	label2 = tk.Label(self, text="Edited attribute (to choose between: identifier - subject - topside - backside - review - position)")
	entry2 = tk.Entry(self, textvariable=edited_attribute)
	label3 = tk.Label(self, text="Change")
	entry3 = tk.Entry(self, textvariable=change)
	
	label1.pack()
	entry1.pack()
	label2.pack()
	entry2.pack()
	label3.pack()
	entry3.pack()
	
	button2 = tk.Button(self, text = "Edit", command = lambda : self.editing_card(identifier.get(),edited_attribute.get(),change.get()))
	button2.pack()
	
    def editing_card(self,identifier,attribute,change):
    	existence=False
    	
    	if my_deck.cards==[]:
    		existence=True
    		showinfo("Info","Empty deck: you should add cards first!")
    	
	for c in my_deck.cards:
		if c.identifier==identifier:
			existence=False
		else:
			showinfo("Info!","This card does not exist!")
			existence=True
			
	if existence==False:	
		if identifier== '' or attribute == '' or change == '':
			showinfo("Info!","All arguments need to be completed")	
		elif attribute=='identifier' or attribute=='topside' or attribute=='backside' or attribute=='subject' or attribute=='review' or attribute=='position':
			my_deck.edit_card(identifier,attribute,change)
			showinfo("Info!","The card has been succesfully edited!")
		else: 
			showinfo("Info!","This attribute does not exist!")
	
	
	
	
class DeleteCard(tk.Frame):
	
    def __init__(self, parent, controller):
    	tk.Frame.__init__(self,parent)
    	self.controller = controller
    	label = tk.Label(self, text="Delete a card", font=controller.title_font)
    	label.pack(side="top", fill="x", pady=10)
    	button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
    	button.pack()
    	
    	identifier = tk.StringVar()
    	label1 = tk.Label(self, text= "Identifier")
	entry1 = tk.Entry(self, textvariable=identifier)
	label1.pack()
	entry1.pack()
	button2 = tk.Button(self, text = "Delete", command = lambda : self.deleting_card(identifier.get()))
	button2.pack()
	
    def deleting_card(self,identifier):
    	existence=False
    	
    	if my_deck.cards==[]:
    		existence=True
    		showinfo("Info","Empty deck: you should add cards first!")
    	
	for c in my_deck.cards:
		if c.identifier==identifier:
			existence=False
		else:
			showinfo("Info!","This card does not exist or you haven't choose a card")
			existence=True
			
	if existence == False:
    		my_deck.delete_card_from_deck(identifier)
    		showinfo("Info!","The card has been deleted, you now have" + str(len(my_deck.cards)) + " cards")
	
	
	
	
	
class PrintCard(tk.Frame):
	
    def __init__(self, parent, controller):
    	tk.Frame.__init__(self,parent)
    	self.controller = controller
    	label = tk.Label(self, text="Print a card", font=controller.title_font)
    	label.pack(side="top", fill="x", pady=10)
    	button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
    	button.pack()
    	

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

