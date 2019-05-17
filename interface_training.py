
from card_class import Card
from deck_class import Deck
from review_list import to_be_reviewed

import tkinter as tk
import tkFont as tkfont
import time
import datetime
import random


my_deck=Deck()
my_deck.load_the_deck('first_deck.pickle')
today=datetime.datetime.now()
a_revoir=to_be_reviewed(my_deck, today)
random.shuffle(a_revoir)
L=len(a_revoir)


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
        for F in (StartPage, Train):
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




# To include images we need to use PIL (Python Image Library)
# from PIL import Image, ImageTk

class StartPage(tk.Frame):
	"""Class for the Master widget."""
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
        	self.controller = controller

		# set the title for the window
		#self.title('Training interface')

		# we create a menu
		#self.menu = tk.Menu(self.master)
		#self.config(menu=self.menu)

		#file = tk.Menu(self.menu)

		# we add an element inside the menu (to quit the programm)
		#file.add_command(label="Quitter", command=self.quit)
		# but we also need to add the element to the menu
		#self.menu.add_cascade(label="File", menu=file)

		
		# we add a label
		label = tk.Label(self, text="Start today session ? Only %s cards to review" %L)
		label.grid(row=0, column=0, sticky=tk.W)

		# we create a button
		# we set command=self.quit
		# When the button is pressed, quit module is ran
		quit_button = tk.Button(self, text="Quit", command=self.quit)
		# and we add the button to the layout
		quit_button.grid(row=1, column=0)


		start_button = tk.Button(self, text="Start", command=lambda: controller.show_frame("Train"))
		start_button.grid(row=1, column=1)

	def quit(self):
		exit()






class Train(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		#self.answer=tk.StringVar()


		while L>0:
			card=a_revoir[0]
			label = tk.Label(self, text="Quelle est la poubelle adaptee a ce dechet : %s ?" %(card.topside))
			label.grid(row=0, column=0, sticky=tk.W)
		
			recyclage_button = tk.Button(self, text="Recyclage", command=self.recyclage(card.backside))
			recyclage_button.grid(row=2, column=0)
		
			compost_button = tk.Button(self, text="Compost", command=self.compost(card.backside))
			compost_button.grid(row=3, column=0)

			verre_button = tk.Button(self, text="Verre", command=self.verre(card.backside))
			verre_button.grid(row=4, column=0)

			bouchon_button = tk.Button(self, text="Bouchon", command=self.bouchon(card.backside))
			bouchon_button.grid(row=5, column=0)

			cendrier_button = tk.Button(self, text="Cendrier", command=self.cendrier(card.backside))
			cendrier_button.grid(row=6, column=0)

		#for item in ["Recyclage", "Compost", "Verre", "Bouchon", "Cendrier", "Electronique", "Piles", "Ordures menageres"]:
			
		

	def load_deck(self):
		var_texte = tk.StringVar()
		ligne_texte = tk.Entry(fenetre, textvariable=var_texte)
		ligne_texte.pack()
		name=var_text.get()
		my_deck.load_the_deck(name.pickle)

	def recyclage(self, backside):
		#self.answer.set()
		if backside=='R':
			label = tk.Label(self, text="Yeah !! Brilliant ! You learn so fast !")
			label.grid(row=1, column=0, sticky=tk.W)

		else :
			label = tk.Label(self, text="Owowo... That was not what was expected... %s was expected" %(backside))
			label.grid(row=1, column=0, sticky=tk.W)


	def compost(self, backside):
		#self.answer.set()
		if backside=='C':
			label = tk.Label(self, text="Yeah !! Brilliant ! You learn so fast !")
			label.grid(row=1, column=0, sticky=tk.W)

		else :
			label = tk.Label(self, text="Owowo... That was not what was expected... %s was expected" %(backside))
			label.grid(row=1, column=0, sticky=tk.W)



	def verre(self, backside):
		#self.answer.set()
		if backside=='V':
			label = tk.Label(self, text="Yeah !! Brilliant ! You learn so fast !")
			label.grid(row=1, column=0, sticky=tk.W)

		else :
			label = tk.Label(self, text="Owowo... That was not what was expected... %s was expected" %(backside))
			label.grid(row=1, column=0, sticky=tk.W)



	def bouchon(self, backside):
		#self.answer.set()
		if backside=='B':
			label = tk.Label(self, text="Yeah !! Brilliant ! You learn so fast !")
			label.grid(row=1, column=0, sticky=tk.W)

		else :
			label = tk.Label(self, text="Owowo... That was not what was expected... %s was expected" %(backside))
			label.grid(row=1, column=0, sticky=tk.W)



	def cendrier(self, backside):
		#self.answer.set()
		if backside=='M':
			label = tk.Label(self, text="Yeah !! Brilliant ! You learn so fast !")
			label.grid(row=1, column=0, sticky=tk.W)

		else :
			label = tk.Label(self, text="Owowo... That was not what was expected... %s was expected" %(backside))
			label.grid(row=1, column=0, sticky=tk.W)



	def quit(self):
		exit()








app = SampleApp()
app.mainloop()








"""Method to display an image."""
#	img = Image.open('flowers.jpg')
#	render = ImageTk.PhotoImage(img)
#	imag = tk.Label(self.master, image=render)
#	imag.image = render
#	imag.grid(row=3, column=0, columnspan=2)
