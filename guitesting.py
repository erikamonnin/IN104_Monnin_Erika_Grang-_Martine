import tkinter as tk
from card_class import Card
from deck_class import Deck
import time

my_deck=Deck()


        		

class Window(tk.Frame):
	
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.master = master
		self.init_window()
		
	#Creation of init_window
	def init_window(self):

	       	# changing the title of our master widget      
        	self.master.title("Flashcard system")
	
        	# allowing the widget to take the full space of the root window
        	self.pack(fill=tk.BOTH, expand=1)
        	
        	#creating a quitting button instance
        	quitButton = tk.Button(self,text="Fermer", command=self.user_exit)
        	quitButton.pack(side="bottom")
        	
        def user_exit(self):
        	quit()
        	
        	
       
def load_a_deck(fenetre):
       	var_texte = tk.StringVar()
       	ligne_texte = tk.Entry(fenetre, textvariable=var_texte)
       	ligne_texte.pack()
       	filename=raw_input('Nom du fichier\n') + '.pickle'
	my_deck.load_the_deck(filename)
	
def deck_management(fenetre):
     	newWindow=tk.Tk()
        newWindow.geometry("400x300")
        newWindow.title("Management system part 2")
             	

def management(fenetre):
	man=tk.Tk()
       	man.geometry("400x300")
       	man.title("Management system")
       	lab=tk.Label(man, text="Do you want to load a deck?")
       	lab.pack()
        	
       	yesButton = tk.Button(man, text="Yes", command=load_a_deck(man))
       	yesButton.place(x=100,y=100)
       	yesButton.pack()
       	noButton = tk.Button(man, text="No", command=deck_management(man))
       	noButton.place(x=100,y=150)
       	noButton.pack()
       	
       	quitButton = tk.Button(man,text="Fermer", command=man.destroy)
       	quitButton.pack(side="bottom")        	
       

def training(fenetre):
        trn=tk.Tk()
        trn.geometry("400x300")
        trn.title("Training system")
        
	
root = tk.Tk()
#size of the window
root.geometry("400x300")
        	
#introducing the game
first_expr = tk.Label(root, text="Welcome to our flashcard system! \n")
first_expr.pack()
        	
#choosing what to do
#managementButton = tk.Button(root, text="Management system", command=management(root))
#managementButton.place(x=100,y=100)
trainingButton = tk.Button(root, text="Training system", command=training(root))
trainingButton.place(x=100,y=150)
	

app = Window(root)
app.mainloop()
