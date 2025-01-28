import tkinter as tk

def show_text():
    text = entry.get()
    result_label.config(text=f"Il testo inserito è: {text}")

root = tk.Tk()
root.title("Esercizio")
root.geometry("300x300")

etichetta = tk.Label(root, text="Inserisci il tuo testo")
etichetta.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

bottone = tk.Button(root, text='Ciao', command=show_text)
bottone.pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
