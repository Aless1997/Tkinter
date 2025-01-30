import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

# Creazione finestra principale
root = tb.Window(themename="cosmo")  # Usa un tema moderno
root.geometry("600x350")
root.title("Tkinter Designer")

# Layout a due colonne
left_frame = tk.Frame(root, bg="#1E88E5", width=250, height=350)
left_frame.pack(side="left", fill="both")

right_frame = tk.Frame(root, bg="white", width=350, height=350)
right_frame.pack(side="right", fill="both", expand=True)

# Testo nel pannello sinistro
welcome_label = tk.Label(
    left_frame,
    text="Welcome to Tkinter Designer\n\n"
         "Tkinter Designer uses the Figma API\n"
         "to analyze a design file and create\nthe respective code.",
    fg="white", bg="#1E88E5",
    font=("Arial", 12),
    justify="left"
)
welcome_label.place(x=20, y=50)

# Form nel pannello destro
tk.Label(right_frame, text="Enter the details.", font=("Arial", 14, "bold"), bg="white").place(x=20, y=20)

ttk.Entry(right_frame, width=40).place(x=20, y=60)
ttk.Entry(right_frame, width=40).place(x=20, y=100)
ttk.Entry(right_frame, width=40).place(x=20, y=140)

# Bottone moderno con ttkbootstrap
btn = tb.Button(right_frame, text="Generate", bootstyle="primary", width=20)
btn.place(x=20, y=180)

# Avvia il loop Tkinter
root.mainloop()
