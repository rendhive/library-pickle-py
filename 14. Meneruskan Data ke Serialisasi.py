import pickle

data = {'key': 'value'}

# Serializing data with additional context
context = {'context_info': 'example'}

with open('data_with_context.pkl', 'wb') as file:
    pickle.dump((data, context), file)

print("Data dengan konteks berhasil diserialisasi ke 'data_with_context.pkl'.")
# Fungsi: Menggabungkan beberapa data menjadi satu file sekaligus menggunakan tuple.
# Kondisi: Ketika Anda ingin menyimpan objek dengan konteks tambahan yang relevan.
