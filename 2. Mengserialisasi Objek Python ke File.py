import pickle

data = {'key': 'value', 'number': 42}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

print("Data berhasil diserialisasi dan disimpan ke 'data.pkl'.")
# Fungsi: Menyimpan objek Python ke dalam file menggunakan serialisasi.
# Kondisi: Ketika Anda ingin menyimpan objek Python ke disk untuk diproses kemudian.
