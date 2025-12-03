import pickle

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)

print("Data yang dibaca dari 'data.pkl':", data)
# Fungsi: Membaca dan mendeserialisasi objek dari file.
# Kondisi: Ketika Anda ingin memuat kembali objek yang disimpan sebelumnya.
