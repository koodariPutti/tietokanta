import tkinter as tk
import sqlite3
from tkinter import messagebox
from tietokanta import lisaa_kurssi, hae_kurssit, poista_kurssi, luo_tietokanta

def lisaa_kurssi_gui(nimi_entry=None, opintopisteet_entry=None,
                     arvosana_entry=None, tila_entry=None, vuosi_entry=None
                     ):
    nimi = nimi_entry.get()
    opintopisteet = opintopisteet_entry.get()
    arvosana = arvosana_entry.get()
    tila = tila_entry.get()
    vuosi = vuosi_entry.get()

    if nimi and opintopisteet and arvosana and tila and vuosi:
        conn = sqlite3.connect('yliopiston_kurssit.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO kurssit (nimi, opintopisteet, arvosana, tila, vuosi)
            VALUES (?, ?, ?, ?, ?)
        ''', (nimi, opintopisteet, arvosana, tila, vuosi))

        conn.commit()
        conn.close()

        messagebox.showinfo("Onnistui", "Kurssi lisätty onnistuneesti.")
    else:
        messagebox.showerror("Virhe", "Täytä kaikki tiedot.")

def main():
    ###########################################################################
    """                 KÄYTTÖLIITTYMÄÄ TÄSTÄ ETEENPÄIN                     """
    ###########################################################################
    root = tk.Tk()
    root.title("Kurssien Hallinta")

    frame = tk.Frame(root)
    frame.pack(padx=300, pady=300)

    nimi_label = tk.Label(frame, text="Nimi:")
    nimi_label.grid(row=0, column=0, sticky="e")
    nimi_entry = tk.Entry(frame)
    nimi_entry.grid(row=0, column=1)

    opintopisteet_label = tk.Label(frame, text="Opintopisteet:")
    opintopisteet_label.grid(row=1, column=0, sticky="e")
    opintopisteet_entry = tk.Entry(frame)
    opintopisteet_entry.grid(row=1, column=1)

    arvosana_label = tk.Label(frame, text="Arvosana:")
    arvosana_label.grid(row=2, column=0, sticky="e")
    arvosana_entry = tk.Entry(frame)
    arvosana_entry.grid(row=2, column=1)

    tila_label = tk.Label(frame, text="Tila:")
    tila_label.grid(row=3, column=0, sticky="e")
    tila_entry = tk.Entry(frame)
    tila_entry.grid(row=3, column=1)

    vuosi_label = tk.Label(frame, text="Vuosi:")
    vuosi_label.grid(row=4, column=0, sticky="e")
    vuosi_entry = tk.Entry(frame)
    vuosi_entry.grid(row=4, column=1)

    lisaa_button = tk.Button(frame, text="Lisää kurssi",
                             command=lisaa_kurssi_gui)
    lisaa_button.grid(row=5, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()