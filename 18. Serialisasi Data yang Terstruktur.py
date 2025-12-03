import pickle

# Struktur data dengan objek dan list
complex_data = {
    'employees': [
        {'name': 'Tom', 'age': 28},
        {'name': 'Sara', 'age': 32}
    ],
    'department': 'Sales'
}

with open('complex_data.pkl', 'wb') as file:
    pickle.dump(complex_data, file)

print("Data kompleks berhasil diserialisasi ke 'complex_data.pkl'.")
# Fungsi: Menyimpan struktur data kompleks ke file menggunakan pickle.
# Kondisi: Ketika Anda bekerja dengan data terstruktur yang memiliki banyak level.
