import pickle

data = {'key': 'value', 'number': 42}

with open('data_v2.pkl', 'wb') as file:
    pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)

print("Data berhasil diserialisasi ke 'data_v2.pkl' dengan menggunakan protokol tertinggi.")
# Fungsi: Menggunakan protokol serialisasi yang berbeda untuk efisiensi.
# Kondisi: Ketika Anda ingin menggunakan versi terbaru dari protokol pickle untuk mengoptimalkan ukuran.
