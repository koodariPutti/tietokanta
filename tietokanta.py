"""
@author Eetu Lindfors
20.1.2024
Tietokanta opinnoille
"""
import sqlite3

def luo_tietokanta():
    """
    Luo tietokannan ja taulun, jos niitä ei ole vielä olemassa.
    """
    # Avaa yhteys tietokantaan
    conn = sqlite3.connect('yliopiston_kurssit.db')
    cursor = conn.cursor()

    # Suorita SQL-komento taulun luomiseksi, jos se ei ole vielä olemassa.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kurssit (
        id INTEGER PRIMARY KEY,
        nimi TEXT NOT NULL,
        opintopisteet INTEGER NOT NULL,
        arvosana INTEGER,
        tila TEXT,
        vuosi TEXT
    )
    ''')

    # Tallenna muutokset ja sulje yhteys.
    conn.commit()
    conn.close()


def lisaa_kurssi(nimi, opintopisteet, arvosana, tila, vuosi):
    """
    Lisää uuden kurssin tietokantaan.
    :param nimi:
    :param opintopisteet:
    :param arvosana:
    :param tila:
    :param vuosi
    :return:
    """
    # Avaa yhteys tietokantaan.
    conn = sqlite3.connect('yliopiston_kurssit.db')
    cursor = conn.cursor()

    # Tarkista onko vastaava kurssi jo olemassa nimen perusteella.
    cursor.execute('SELECT * FROM kurssit WHERE nimi=?', (nimi,))
    olemassa_olevat_kurssit = cursor.fetchall()

    if not olemassa_olevat_kurssit:
        # Jos vastaavaa kurssia ei ole, lisää se tietokantaan.
        cursor.execute('''
                INSERT INTO kurssit (nimi, opintopisteet, arvosana, tila, vuosi)
                VALUES (?, ?, ?, ?, ?)
            ''', (nimi, opintopisteet, arvosana, tila, vuosi))

        # Tallenna muutokset ja sulje yhteys.
        conn.commit()
        conn.close()
        print(f"Kurssi '{nimi}' lisätty onnistuneesti.")
    else:
        print(f"Kurssi '{nimi}' on jo olemassa.")


def hae_kurssit():
    """
    Hae kaikki kurssit tietokannasta ja palauta ne listana.
    :return:
    """
    # Avaa yhteys tietokantaan
    conn = sqlite3.connect('yliopiston_kurssit.db')
    cursor = conn.cursor()

    # Suorita SQL-komento kaikkien kurssien hakemiseksi.
    cursor.execute('SELECT * FROM kurssit')

    # Haetaan kaikki kurssit ja tallennetaan ne muuttujaan (kurssit).
    kurssit = cursor.fetchall()

    # Sulje yhteys ja palauta kurssit lista.
    conn.close()
    return kurssit


def poista_kurssi(kurssi_id):
    """
    Poista kurssi tietokannasta annetun kurssi_id:n perusteella.
    :param kurssi_id
    :return: 
    """
    # Avaa yhteys
    conn = sqlite3.connect('yliopiston_kurssit.db')
    cursor = conn.cursor()

    # Suorita SQL-komento kurssin poistamiseksi ID:N perusteella
    cursor.execute('''
        DELETE FROM kurssit WHERE id=?
    ''', (kurssi_id,))

    conn.commit()
    conn.close()


def main():
    """
    Pääohjelma, jossa suoritetaan tietokannan ja taulun luonti,
    lisätään kursseja, haetaan kaikki kurssit ja tulostetaan ne.
    :return:
    """
    luo_tietokanta()

    #lisaa_kurssi('Ohjelmointi 1', 6, 3, 'Done', 'S2021')


    kaikki_kurssit = hae_kurssit()
    for kurssi in kaikki_kurssit:
        print(kurssi)


if __name__ == "__main__":
    main()



