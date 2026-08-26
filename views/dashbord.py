import tkinter as tk

app = tk.Tk()
app.title("Gestion des salles")




label_salle = tk.Label(app, text = "Salle B-107")
label_salle.pack()


button = tk.Button(app,text = "fermer", command=app.quit)


button.pack()





app.mainloop()