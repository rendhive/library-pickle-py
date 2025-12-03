import pickle

employees = [
    {'name': 'Tom', 'age': 28},
    {'name': 'Sara', 'age': 32}
]

# Serialisasi daftar karyawan
with open('employees.pkl', 'wb') as file:
    pickle.dump(employees, file)

with open('employees.pkl', 'rb') as file:
    loaded_employees = pickle.load(file)

print("Loaded Employees:", loaded_employees)
# Fungsi: Memproses dan menyimpan kumpulan data yang lebih kompleks menggunakan pickle.
# Kondisi: Ketika Anda berurusan dengan list atau kumpulan data terstruktur.
