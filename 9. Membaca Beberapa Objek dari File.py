import pickle

data = []

with open('multiple_data.pkl', 'rb') as file:
    while True:
        try:
            data.append(pickle.load(file))
        except EOFError:
            break

print("Data yang dibaca dari 'multiple_data.pkl':", data)
# Fungsi: Membaca beberapa objek dari file yang telah serialisasi.
# Kondisi: Ketika Anda ingin memulihkan semua objek dari satu file.
