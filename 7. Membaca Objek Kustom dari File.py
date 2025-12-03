import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

with open('person.pkl', 'rb') as file:
    person = pickle.load(file)

print(f"Nama: {person.name}, Usia: {person.age}")
# Fungsi: Membaca dan mendeserialisasi objek kustom dari file.
# Kondisi: Ketika Anda ingin memulihkan objek kustom yang tersimpan sebelumnya.
