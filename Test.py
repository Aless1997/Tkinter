import tkinter as tk
import os

lista = os.listdir()

def xy():
    testo = x.get()
    risultato.config(text=f"Hai inserito il testo: {testo}")

    if "Prova.txt" not in lista:
        with open('Prova.txt', 'a') as file:
            file.write(testo+'\n')
    else:
        with open('Prova.txt', 'a') as file:
            file.write(testo+'\n')

def read():
    try:
        with open('Prova.txt', 'r') as file:
            cnt = file.read()
        lettura.config(text=cnt)
    except FileNotFoundError:
        lettura.config(text="Nessun File Trovato")


root = tk.Tk()
root.title("Programma personale")
root.geometry("300x300")

etichetta = tk.Label(root, text="Esercizio per visualizzare il testo:")
etichetta.pack(pady=10)

x = tk.Entry(root)
x.pack(pady=5)

btn = tk.Button(root, text="Cliccami", command=xy)
btn.pack(pady=2.5)

risultato = tk.Label(root, text="Non hai inserito nulla")
risultato.pack(pady=2.5)

btn2 = tk.Button(root, text='Leggi File', command=read)
btn2.pack(pady=5)

lettura = tk.Label(root, text="Nessuna Lettura Richiesta")
lettura.pack(pady=5)

tk.mainloop()