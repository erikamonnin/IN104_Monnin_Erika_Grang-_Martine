import tkinter as tk
from card_class import Card
from deck_class import Deck
import time


# definition de la class window #

class Window(tk.Frame):

	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.master = master

	def label(self,sentence):
		expression = tk.Label(self,text=sentence)
		expression.pack()
			
	
	def fermer(self):
		quit()
	
	def management(self):
		root2 = tk.Tk()
		root2.geometry("400x300")
		return(Window(root2))
		
	def training(self):
		return
		
	#def open_new_window(self,Title,Sentence):
	#	root2=tk.Tk()
	#	root2.geometry("400x300")
	#	app2=Window(root2)
	#	app2.master.title(Title)
	#	app2.pack(fill=tk.BOTH, expand=1)
	#	app2.label(Sentence)
		
def open_window():
	win=tk.Toplevel(root)
	
def test():
	print("encore un test on s'en sort plus")
	return
		
#utilisation de la classe window #
	
root = tk.Tk()
root.geometry("400x300")
app=Window(root)
app.master.title("Flashcard system")
app.pack(fill=tk.BOTH, expand=1)
app.label("Welcome in our flashcard system!")

managementButton = tk.Button(root,text="Management system", command=open_window())
managementButton.place(x=100,y=100)

trainingButton = tk.Button(app,text="Training system",command=app.training)
trainingButton.place(x=100,y=150)

quitButton = tk.Button(app,text="Fermer", command=app.fermer)
quitButton.pack(side="bottom")

app.mainloop()

