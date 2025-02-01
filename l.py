import tkinter as tk
import os
lista = os.listdir()

def testo():
    testo = entry.get()
    risultato.config(text=f"Hai inserito: {testo}")

    if 'Dati.txt' not in lista:
        with open('Dati.txt', 'a') as file:
            file.write(testo + "\n")
    else:
        with open('Dati.txt', 'a') as file:
            file.write(testo + "\n")

def read():
    try:
        with open('Dati.txt', 'r') as file:
            lettura = file.read()
            risultato2.config(text=f"{lettura}")
    except FileNotFoundError:
        risultato2.config(text=f"Nessun file trovato!")

root = tk.Tk()
root.title("Programma personale")
root.geometry("350x450")

descr1 = tk.Label(text="Di seguito potrai inserire un testo da salvare su txt:")
descr1.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=2.5)

btn = tk.Button(root, text="Invia!", command=testo)
btn.pack(pady=2.5)

risultato = tk.Label(root, text="Nessun testo inserito!")
risultato.pack(pady=2.5)

btn2 = tk.Button(root, text="Leggi File", command=read)
btn2.pack(pady=2.5)

risultato2 = tk.Label(root, text="Nessuna Lettura")
risultato2.pack(pady=2.5)

tk.mainloop()
