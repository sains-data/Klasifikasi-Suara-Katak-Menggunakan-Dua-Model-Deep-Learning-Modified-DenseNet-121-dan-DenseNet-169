# Klasifikasi-Suara-Katak-Menggunakan-Dua-Model-Deep-Learning-Modified-DenseNet-121-dan-DenseNet-169

**Kelompok 25:**
1. Kharisma Gumilang (121450142)
2. Afwa Fuadi Nugraha (121450019)
3. Isyamaetreya Savitri (121450137)
4. Yunita Amelia Puspitasari (121450118)
5. Jasmine Georgina Sekartaji (121450159)
6. Nadia Fitri Yani (121450101)

## Latar Belakang
Katak merupakan amfibi dengan keanekaragaman spesies yang tinggi dan berperan penting dalam ekosistem sebagai pengendali serangga serta bioindikator kesehatan lingkungan. Namun, populasinya kini menghadapi ancaman serius akibat kerusakan habitat, polusi, dan perubahan iklim. Suara unik yang dihasilkan setiap spesies dapat dimanfaatkan sebagai alat pemantauan ekosistem secara efektif. Melalui fitur Mel-frequency Cepstral Coefficients (MFCC) dan model DenseNet, pengenalan suara dapat dilakukan dengan akurasi tinggi, bahkan dalam kondisi lingkungan yang kompleks.

## Tujuan Penelitian
1. Mengklasifikasikan suara katak dari berbagai spesies menggunakan deep learning.
2. Memanfaatkan Mel-frequency Cepstral Coefficients (MFCC) untuk ekstraksi fitur suara.
3. Membandingkan performa model Modified DenseNet-121 dan DenseNet-169 dalam klasifikasi suara katak.

## Dataset
Data suara katak diperoleh dari Platform Xenocanto yang menggunakan suara dari 9 spesies katak , yaitu Boana Cinerascens, Papper Treefrog, Pool Frog, South American White-lipped Grassfrog, Dendropsophus Minutus, Rana Temporaria, Rhinella Marina, Leptodactylus Fuscus, dan Scinax Ruber. Total sampel data yaitu 1.512 data suara. Data suara dikonversi dari format MP3 ke WAV.

## Pra-Proses Data
a. **Segmentasi Data**
  Rekaman suara katak dibagi menjadi segmen-segmen berdurasi 5 detik untuk memastikan konsistensi dalam analisis. Proses dimulai dengan pengurangan noise menggunakan metode noise reduction untuk meningkatkan kejernihan suara. Setelah itu, setiap segmen dikelompokkan berdasarkan nama spesies yang tertera dalam nama file, dan jumlah file untuk setiap kelas dicatat untuk memberikan gambaran distribusi data. Hasil akhir dari segmentasi ini adalah 1.512 segmen audio yang siap untuk analisis lebih lanjut.
b. **Ekstraksi MFCC**
  Sebanyak 13 komponen MFCC diambil untuk menggambarkan frekuensi yang relevan dengan persepsi suara manusia. Hasil ekstraksi kemudian divisualisasikan untuk menunjukkan perubahan koefisien dari waktu ke waktu, mempermudah pemahaman terhadap karakteristik suara. Koefisien MFCC yang telah diekstraksi disimpan dalam format yang memudahkan analisis lebih lanjut, menghasilkan total 1.512 file MFCC yang siap untuk diproses lebih lanjut.

## Model
a. **Modified DenseNet-121**
  Model Modified DenseNet-121 memiliki 121 lapisan konvolusional dengan konektivitas yang memungkinkan setiap lapisan menerima input dari lapisan sebelumnya, sehingga mendukung aliran informasi yang lebih baik dan ekstraksi fitur yang efisien. Modifikasi pada model ini mencakup penerapan Batch Normalization untuk mempercepat konvergensi, penambahan dua lapisan Dropout untuk mengurangi overfitting, serta penggunaan Adaptive Average Pooling untuk mengurangi dimensi fitur menjadi ukuran tetap 1x1 sebelum proses klasifikasi.
  
b. **Modified DenseNet-169**
  Modified DenseNet-169 adalah model dengan 169 lapisan konvolusional yang memiliki konektivitas khas, memungkinkan pemrosesan fitur yang lebih kompleks. Beberapa modifikasi pada model ini meliputi penerapan Batch Normalization untuk menstabilkan distribusi aktivasi dan mempercepat proses konvergensi, penggunaan Dropout untuk mengurangi overfitting dan meningkatkan kemampuan generalisasi, serta penerapan Adaptive Average Pooling untuk mengurangi kompleksitas komputasi dan mempersiapkan fitur sebelum proses klasifikasi.

## Hasil

Berikut ini hasil berdasarkan matrik evalusi serta grafik akurasi pelatihan dan validasi dari kedua model:

![image](https://github.com/user-attachments/assets/f3baa249-a726-4550-bb6e-dd8a18f8fd90)

![image](https://github.com/user-attachments/assets/99dcfee4-7250-4e49-a807-06c7ab674fb9)

Model Modified DenseNet-121 menunjukkan kinerja lebih baik daripada Modified DenseNet-169 dalam klasifikasi suara katak, dengan akurasi 68%. Metrik seperti precision, recall, dan F1-score mendukung efektivitas model ini dalam mengidentifikasi spesies katak. Penelitian ini berkontribusi pada pemantauan keanekaragaman hayati dan konservasi katak. Penelitian selanjutnya dapat mengeksplorasi model atau teknik ekstraksi fitur yang lebih canggih serta mengembangkan dataset yang lebih besar dan beragam untuk meningkatkan generalisasi model.


