import tkinter as tk
from PIL import *
class Window(tk.Frame):
	
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.master = master
		self.init_window()
		
	#Creation of init_window
	def init_window(self):

	       	# changing the title of our master widget      
        	self.master.title("Management system")
	
        	# allowing the widget to take the full space of the root window
        	self.pack(fill=tk.BOTH, expand=1)
        	
        	#creating a quitting button instance
        	quitButton = tk.Button(self,text="Fermer", command=self.user_exit)
        	quitButton.pack(side="bottom")
        	
        	#introducing the game
        	first_expr = tk.Label(self, text="Welcome to our flashcard system! \n")
        	first_expr.pack()
        	
        	#creating the answers buttons
        	managementButton = tk.Button(self, text="Management system", command=self.management)
        	managementButton.place(x=100,y=100)
        	trainingButton = tk.Button(self, text="Training system", command=self.training)
        	trainingButton.place(x=100,y=150)
        	
        	#creating a radiobutton
        	
        	#var_choix = tk.StringVar()
		#choix_rouge = tk.Radiobutton(self, text="Rouge", variable=var_choix, value="rouge")
		#choix_vert = tk.Radiobutton(self, text="Vert", variable=var_choix, value="vert")
		#choix_bleu = tk.Radiobutton(self, text="Bleu", variable=var_choix, value="bleu")
		#choix_rouge.pack()
		#choix_vert.pack()
		#choix_bleu.pack()

        	
        	# creating a menu
        	#menu = tk.Menu(self.master)
        	#self.master.config(menu=menu)

		#close = tk.Menu(menu)
		#close.add_command(label="Fermer",command=self.user_exit)
        	#menu.add_cascade(label="Fermer", menu=close)
        		        	
		#fil = tk.Menu(menu)
        	#fil.add_command(label="Ouvrir")
        	#fil.add_command(label="Enregistrer")
        	#menu.add_cascade(label="File", menu=fil)
        	
        	#edit = tk.Menu(menu)
        	#edit.add_command(label="Undo")
        	#edit.add_command(label="Show Img", command=self.showImg)
        	#edit.add_command(label="Show Text", command=self.showTxt)
        	#menu.add_cascade(label="Edit", menu=edit)
	
        	
        def user_exit(self):
        	quit()
        	
        def load_a_deck(self):
        	filename=raw_input('Nom du fichier\n') + '.pickle'
		my_deck.load_the_deck(filename)
        	
        def no_load_a_deck(self):
        	return
        
	

		
root = tk.Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()

