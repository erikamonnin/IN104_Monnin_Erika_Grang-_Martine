import tkinter as tk
from card_class import Card
from deck_class import Deck
import time



class Window(tk.Frame):
	
	def __init__(self, master=None):
 		self.var = tk.IntVar()
		c = tk.Checkbutton(
			master, text="Enable Tab",
			variable=self.var,
			command=self.cb)
		c.pack()

	def cb(self, event):
		print "variable is", self.var.get()



root = tk.Tk()
root.geometry("400x300")

app = Window(root)
app.mainloop()
