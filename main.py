# import json
# import random

# def shuffle_correct_answer(data):
#     for key, value in data.items():
#         if "pilihan" in value:
#             options = list(value["pilihan"].items())
#             random.shuffle(options)  # Mengacak urutan jawaban
            
#             # Menyusun ulang pilihan dalam dictionary baru
#             shuffled_options = {chr(97 + i): {"jawaban": opt[1]["jawaban"], "status": opt[1]["status"], "penjelasan": opt[1]["penjelasan"]} for i, opt in enumerate(options)}
#             value["pilihan"] = shuffled_options
#     return data

# # Membaca data dari file JSON
# with open("data.json", "r", encoding="utf-8") as file:
#     data_json = json.load(file)

# # Mengacak posisi jawaban benar
# shuffled_data = shuffle_correct_answer(data_json)

# # Menyimpan hasil kembali ke file JSON
# with open("data.json", "w", encoding="utf-8") as file:
#     json.dump(shuffled_data, file, indent=4, ensure_ascii=False)

# print("Proses pengacakan selesai. Data telah diperbarui di data.json")

import re

def reorder_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Menggunakan regex untuk menangkap angka urut dari 1 sampai 42 beserta teksnya
    segments = re.findall(r'(\b(?:[1-9]|[1-3][0-9]|4[0-2])\.)\s*([^\d]+)', text)
    
    # Mengurutkan berdasarkan nomor urut yang ditemukan
    sorted_segments = sorted(segments, key=lambda x: int(x[0][:-1]))
    
    # Menggabungkan kembali teks dengan enter di antara nomor urut
    formatted_text = '\n'.join(f'{num} {txt.strip()}' for num, txt in sorted_segments)
    
    return formatted_text

# Contoh penggunaan
filename = 'data.txt'
result = reorder_text(filename)
print(result)
