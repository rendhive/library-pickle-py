import pickle
import sys

data = {'key': 'value'}

with open('data_v3.pkl', 'wb') as file:
    pickle.dump(data, file, protocol=3)  # Menyimpan dengan protokol versi 3

print("Data disimpan dengan protokol versi 3.")
# Fungsi: Menyimpan data dengan memilih spesifik protokol untuk kompatibilitas.
# Kondisi: Ketika Anda perlu memastikan bahwa data dapat dibaca oleh versi Python yang lebih lama.
