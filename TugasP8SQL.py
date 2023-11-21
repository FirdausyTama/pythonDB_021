import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

uiApp = tk.Tk()
uiApp.configure(background='lavender')
uiApp.geometry("700x750")
uiApp.resizable(False, False)
uiApp.title("Aplikasi Prediksi Jurusan Pilihan")

# make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10, fill="x", expand=True)

# make label
inputLabel = ttk.Label(inputFrame, text="Input Nilai Mata Pelajaran")
inputLabel.pack(padx=160, pady=10, fill="x", expand=True)

# 1. membuat input nilai indo
labelInputTgl = ttk.Label(inputFrame, text="Masukan Nama Siswa")
labelInputTgl.pack(padx=10, pady=5, fill="x", expand=True)

entryInputTgl = ttk.Entry(inputFrame)
entryInputTgl.pack(padx=10, pady=5, fill="x", expand=True)

# 2. membuat input nilai fisika
labelInputFsk = ttk.Label(inputFrame, text="Masukan Nilai Fisika")
labelInputFsk.pack(padx=10, pady=5, fill="x", expand=True)

entryInputFsk = ttk.Entry(inputFrame)
entryInputFsk.pack(padx=10, pady=5, fill="x", expand=True)

# 3. membuat input nilai Bahasa inggris
labelInputIng = ttk.Label(inputFrame, text="Masukan Nilai Bahasa Inggris")
labelInputIng.pack(padx=10, pady=5, fill="x", expand=True)

entryInputIng = ttk.Entry(inputFrame)
entryInputIng.pack(padx=10, pady=5, fill="x", expand=True)

# 4. membuat input nilai biologi
labelInputJrg = ttk.Label(inputFrame, text="Masukan Nilai Biologi")
labelInputJrg.pack(padx=10, pady=5, fill="x", expand=True)

entryInputJrg = ttk.Entry(inputFrame)
entryInputJrg.pack(padx=10, pady=5, fill="x", expand=True)

# 5 Membuat variabel prediksi fakultas
labelInputFk = ttk.Label(inputFrame, text="Prediksi Fakultas")
labelInputFk.pack(padx=10, pady=5, fill="x", expand=True)

# membuat Button
def klikbutton():
    nama_siswa = entryInputTgl.get()
    fisika = float(entryInputFsk.get())
    inggris = float(entryInputIng.get())
    biologi = float(entryInputJrg.get())

    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        prediksi_fakultas = "Teknik"
    elif inggris > biologi and inggris > fisika:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Tidak dapat diprediksi"

    messagebox.showinfo("Hasil Prediksi", f"\nHasil Prediksi Fakultas {prediksi_fakultas}!")
    simpan_data_ke_sqlite(nama_siswa, biologi, fisika, inggris, prediksi_fakultas)

def simpan_data_ke_sqlite(nama_siswa, entryInputJrg, entryInputFsk, entryInputIng, prodi_terpilih):
    # Membuka atau membuat database SQLite
    conn = sqlite3.connect("prodidb.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nama_siswa TEXT, 
                    nilai_biologi REAL,
                    nilai_fisika REAL,
                    nilai_inggris REAL,
                    prodi_terpilih TEXT)''')

    # Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO hasil_prediksi (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prodi_terpilih) VALUES (?, ?, ?, ?, ?)",
                   (nama_siswa, entryInputJrg, entryInputFsk, entryInputIng, prodi_terpilih))

    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

buttonSubmit = ttk.Button(inputFrame, text="Submit Nilai", command=klikbutton)
buttonSubmit.pack(padx=10, pady=10, fill="x", expand=True)

uiApp.mainloop()
