import Tkinter as tk

fenetre = tk.Tk()


listbox = tk.Listbox(fenetre)
listbox.pack()
for item in ["Recyclage", "Compost", "Verre", "Bouchon", "Cendrier", "Electronique", "Piles", "Ordures menageres"]:
	listbox.insert(tk.END, item)


bouton=tk.Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()


fenetre.mainloop()
