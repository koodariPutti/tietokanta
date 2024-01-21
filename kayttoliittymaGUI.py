"""
@author Eetu Lindfors
Käyttöliittymä tietokannalle
"""
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tietokanta import lisaa_kurssi, hae_kurssit, poista_kurssi, luo_tietokanta

def lisaa_kurssi_gui(tree, nimi_entry, opintopisteet_entry, arvosana_entry, tila_entry, vuosi_entry):
    nimi = nimi_entry.get()
    opintopisteet = opintopisteet_entry.get()
    arvosana = arvosana_entry.get()
    tila = tila_entry.get()
    vuosi = vuosi_entry.get()

    if nimi and opintopisteet and arvosana and tila and vuosi:
        try:
            opintopisteet = int(opintopisteet)
            arvosana = int(arvosana)
            luo_tietokanta()
            lisaa_kurssi(nimi, opintopisteet, arvosana, tila, vuosi)
            messagebox.showinfo("Onnistui", "Kurssi lisätty onnistuneesti.")
            nayta_kurssit(tree)
        except ValueError:
            messagebox.showerror("Virhe", "Anna kelvolliset opintopisteet ja arvosana.")
    else:
        messagebox.showerror("Virhe", "Täytä kaikki tiedot.")


def poista_kurssi_gui(tree, id_entry):
    try:
        kurssi_id = int(id_entry.get())
        vahvista = messagebox.askyesno("Vahvista poisto", "Haluatko varmasti poistaa kurssin?")
        if vahvista:
            poista_kurssi(kurssi_id)
            messagebox.showinfo("Onnistui", "Kurssi poistettu onnistuneesti.")
            nayta_kurssit(tree)
    except ValueError:
        messagebox.showerror("Virhe", "Anna kelvollinen ID.")


def nayta_kurssit(tree):
    tree.delete(*tree.get_children())
    kurssit = hae_kurssit()
    for kurssi in kurssit:
        tree.insert('', 'end', values=kurssi)


def keskita_ikkuna(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    width = root.winfo_width()
    height = root.winfo_height()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"+{x}+{y}")


def main():
    root = tk.Tk()
    root.title("Kurssien Hallinta")

    root.bind("<Configure>", lambda e: keskita_ikkuna(root))

    frame = tk.Frame(root)
    frame.pack(padx=100, pady=100)

    font = ('Arial', 12)

    nimi_label = tk.Label(frame, text="Nimi:", font=font)
    nimi_label.grid(row=0, column=0, sticky="e")
    nimi_entry = tk.Entry(frame)
    nimi_entry.grid(row=0, column=1)

    opintopisteet_label = tk.Label(frame, text="Opintopisteet:", font=font)
    opintopisteet_label.grid(row=1, column=0, sticky="e")
    opintopisteet_entry = tk.Entry(frame)
    opintopisteet_entry.grid(row=1, column=1)

    arvosana_label = tk.Label(frame, text="Arvosana:", font=font)
    arvosana_label.grid(row=2, column=0, sticky="e")
    arvosana_entry = tk.Entry(frame)
    arvosana_entry.grid(row=2, column=1)

    tila_label = tk.Label(frame, text="Tila:", font=font)
    tila_label.grid(row=3, column=0, sticky="e")
    tila_entry = tk.Entry(frame)
    tila_entry.grid(row=3, column=1)

    vuosi_label = tk.Label(frame, text="Vuosi:", font=font)
    vuosi_label.grid(row=4, column=0, sticky="e")
    vuosi_entry = tk.Entry(frame)
    vuosi_entry.grid(row=4, column=1)

    lisaa_button = tk.Button(frame, text="Lisää kurssi",
                             command=lambda: lisaa_kurssi_gui(tree, nimi_entry, opintopisteet_entry,
                                                               arvosana_entry, tila_entry, vuosi_entry),
                             font=font)
    lisaa_button.grid(row=5, columnspan=2, pady=10)

    id_label = tk.Label(frame, text="ID poisto:", font=font)
    id_label.grid(row=6, column=0, sticky="e")
    id_entry = tk.Entry(frame)
    id_entry.grid(row=6, column=1)

    poista_button = tk.Button(frame, text="Poista kurssi",
                              command=lambda: poista_kurssi_gui(tree, id_entry),
                              font=font)
    poista_button.grid(row=7, columnspan=2, pady=10)

    columns = ('ID', 'Nimi', 'Opintopisteet', 'Arvosana', 'Tila', 'Vuosi')
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.grid(row=8, column=0, columnspan=2, pady=10)

    nayta_kurssit(tree)

    keskita_ikkuna(root)
    root.mainloop()

if __name__ == "__main__":
    main()