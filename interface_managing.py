import tkinter as tk
import tkFont as tkfont


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
		label = tk.Label(self, text="What do you want to do ?", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)

		button1 = tk.Button(self, text="Add a card", command=lambda: controller.show_frame("AddCard"))
		button2 = tk.Button(self, text="Edit a card", command=lambda: controller.show_frame("EditCard"))
		button3 = tk.Button(self, text="Delete a card", command=lambda: controller.show_frame("DeleteCard"))
		button4 = tk.Button(self, text="Print a card", command=lambda: controller.show_frame("PrintCard"))
		button5 = tk.Button(self, text="Quit", command=self.quit)
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


class EditCard(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Edit a card", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
		button.pack()

class DeleteCard(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Delete a card", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
		button.pack()

class PrintCard(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Print a card", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
		button.pack()


if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()

