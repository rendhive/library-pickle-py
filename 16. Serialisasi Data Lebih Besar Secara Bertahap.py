import pickle

data_part1 = {'key1': 'value1'}
data_part2 = {'key2': 'value2'}

# Menyimpan dua bagian data secara terpisah
with open('large_data.pkl', 'wb') as file:
    pickle.dump(data_part1, file)
    pickle.dump(data_part2, file)

print("Bagian data berhasil disimpan ke 'large_data.pkl'.")
# Fungsi: Menyimpan data dalam bagian-bagian terpisah untuk kompresi yang lebih baik.
# Kondisi: Ketika Anda memiliki data yang besar dan ingin membaginya menjadi bagian yang lebih kecil.
