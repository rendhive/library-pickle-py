import pickle

# Menggunakan file yang tidak ada
try:
    with open('non_existing_file.pkl', 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File tidak ditemukan.")
# Fungsi: Menangani error saat memuat objek dari file.
# Kondisi: Saat Anda ingin memastikan aplikasi Anda tidak crash dengan file yang hilang atau rusak.
