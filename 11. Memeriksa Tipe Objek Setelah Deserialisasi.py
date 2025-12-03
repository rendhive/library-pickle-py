import pickle

data = {'key': 'value'}

# Serialisasi dan kemudian deserialisasi
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("Type of loaded_data:", type(loaded_data))
# Fungsi: Memverifikasi tipe objek setelah deserialisasi.
# Kondisi: Ketika Anda perlu memastikan bahwa objek yang dimuat adalah dari tipe yang diharapkan.
