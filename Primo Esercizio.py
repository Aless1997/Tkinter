import tkinter as tk

def on_button_click():
    etichetta.config(text="Hai cliccato il bottone!")

root = tk.Tk()
root.title("Esempio di finestra")
root.geometry("300x300")

etichetta = tk.Label(root, text="Etichetta!")
etichetta.pack(pady = 50)

bottone = tk.Button(root, text="Cliccami", command=on_button_click)
bottone.pack(pady = 10)

root.mainloop()
