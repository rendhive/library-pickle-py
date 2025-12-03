import pickle

with open('list_data.pkl', 'rb') as file:
    data_list = pickle.load(file)

print("List yang dibaca dari 'list_data.pkl':", data_list)
# Fungsi: Membaca dan mendeserialisasi list objek dari file.
# Kondisi: Ketika Anda ingin memulihkan list objek yang tersimpan.
