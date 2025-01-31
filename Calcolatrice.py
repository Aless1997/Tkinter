import tkinter as tk

def somma():
    valore1 = entry.get()
    valore2 = entry2.get()

    ris = int(valore1) + int(valore2)
    risultato.config(text=f"{ris}")
def diff():
    valore1 = entry.get()
    valore2 = entry2.get()

    ris = int(valore1) - int(valore2)
    risultato.config(text=f"{ris}")

root = tk.Tk()
root.title("Calcolatrice")
root.geometry("350x400")

entry = tk.Entry(root, width=5)
entry.pack(pady=10)

sum = tk.Button(root, text="+", command=somma)
sum.pack(pady=5)

dif = tk.Button(root,text="-", command=diff)
dif.pack(pady=5)

entry2 = tk.Entry(root, width=5)
entry2.pack(pady=10)

risultato = tk.Label(root, text="")
risultato.pack(pady=10)

root.mainloop()