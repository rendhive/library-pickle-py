import pickle

def custom_function(x):
    return x * x

# Serialisasi fungsi kustom
with open('custom_function.pkl', 'wb') as file:
    pickle.dump(custom_function, file)

with open('custom_function.pkl', 'rb') as file:
    loaded_function = pickle.load(file)

print("Hasil dari fungsi kustom:", loaded_function(5))
# Fungsi: Menyimpan dan memulihkan fungsi kustom.
# Kondisi: Ketika Anda membutuhkan kemampuan untuk menggunakan fungsi kembali tanpa mendefinisikannya setiap kali.
