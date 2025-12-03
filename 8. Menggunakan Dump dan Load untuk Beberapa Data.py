import pickle

data1 = {'name': 'John'}
data2 = {'name': 'Jane'}

with open('multiple_data.pkl', 'wb') as file:
    pickle.dump(data1, file)
    pickle.dump(data2, file)

print("Beberapa data berhasil diserialisasi ke 'multiple_data.pkl'.")
# Fungsi: Menyimpan beberapa objek ke dalam file menggunakan dump.
# Kondisi: Ketika Anda ingin menyimpan lebih dari satu objek dalam satu file.
