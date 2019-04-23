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
        	
        	# creating a menu
        	menu = tk.Menu(self.master)
        	self.master.config(menu=menu)

		close = tk.Menu(menu)
		close.add_command(label="Fermer",command=self.user_exit)
        	menu.add_cascade(label="Fermer", menu=close)
        		        	
		fil = tk.Menu(menu)
        	fil.add_command(label="Ouvrir")
        	fil.add_command(label="Enregistrer")
        	menu.add_cascade(label="File", menu=fil)
        	
        	edit = tk.Menu(menu)
        	edit.add_command(label="Undo")
        	edit.add_command(label="Show Img", command=self.showImg)
        	edit.add_command(label="Show Text", command=self.showTxt)
        	menu.add_cascade(label="Edit", menu=edit)
	
        	
        def user_exit(self):
        	quit()
        
        def showImg(self):
        	load = PIL.Image.open("chat.png")
        	render = PIL.ImageTk.PhotoImage(load)
        	
        	img = tk.Label(self, image=render)
        	img.image = render
        	img.place(x=0, y=0)
        def showTxt(self):
        	text = tk.Label(self, text="Martine la bote!")
        	text.pack()
	

		
root = tk.Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()

