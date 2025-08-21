<!--
 Copyright 2025 ariefsetyonugroho
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     https://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

# 📦 Face Attendance Solenoid Door Lock 
Pendeteksian wajah dengan output doorlock

## ✨ Features  


## ⚙️ Installation & 🚀 Usage 
- Clone Project
```
git clone https://github.com/JehianKamal/face-attendance-solenoid-door-lock.git
```
- Buka Project
```
cd face-attendance-solenoid-door-lock
```
- Install requirements
```
pip install -r requirements.txt
```
- Run Project </br>
Pertama: Jalan program yang ada di dalam folder `examples/` 
```
cd examples
```
Kedua: Jalankan program dibawah untuk mencapture gambar yang akan dilatih. Setelah kamera muncul dan wajah terdeteksi segera tekan tombol `c` sebanyak 5 kali diterminal sampai ada `[INFO] 5 IMAGE CAPTURE SUCCESSFULL`.
```
python take_pictures.py
```
Ketiga: Jalankan program dibawah untuk melakukan training data. Data training akan otomatis tesimpan dalam folder 
```
python train.py
```
Keempat: Sebelum menjalankan program. Buka program `test.py` dan ubah bagian dibawah dengan nama dari wajah/user
```
known_names = ['Arief Setyo Nugroho']
```
Kelima:: Jalankan program dibawah untuk melakukan testing 


## Notes
Saat mau melakukan capture ulang, hapus semua gambar yang ada pada folder `faces_data`. Jika ingin menambah data tanpa menghapus data gambar lama, ganti id yang ada di program `take_pictures.py`.
```
ids = 1  # ganti id jika lebih dari satu orang
```
Setelah itu, tambahkan nama dari gambar di `test.py`
```
known_names = ['Arief Setyo Nugroho', 'Nama_gambar_baru]
```

## ScreenShoot


https://github.com/user-attachments/assets/11a3faba-4f77-4eef-b693-bc2525d05002

