import pickle

data_combined = []

with open('large_data.pkl', 'rb') as file:
    while True:
        try:
            data = pickle.load(file)
            data_combined.append(data)
        except EOFError:
            break

print("Data yang dipulihkan:", data_combined)
# Fungsi: Mengambil data secara berurutan dari file pickle yang besar.
# Kondisi: Ketika Anda ingin mengembalikan data dalam urutan yang sudah disimpan.
