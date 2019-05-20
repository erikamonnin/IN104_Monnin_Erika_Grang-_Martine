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




#utilisation de la classe window #
	
root = tk.Tk()
root.geometry("400x300")
app=Window(root)
app.master.title("Flashcard system")

app.label("Welcome")

app.mainloop()

