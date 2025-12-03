import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

print("Objek 'Person' berhasil diserialisasi ke 'person.pkl'.")
# Fungsi: Menyimpan objek kustom (mis. kelas pengguna) ke dalam file.
# Kondisi: Ketika Anda memiliki objek kustom yang ingin disimpan untuk penggunaan di masa mendatang.
