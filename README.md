# Klasifikasi-Suara-Katak-Menggunakan-Dua-Model-Deep-Learning-Modified-DenseNet-121-dan-DenseNet-169

**Kelompok 25:**
1. Kharisma Gumilang (121450142)
2. Afwa Fuadi Nugraha (121450019)
3. Isyamaetreya Savitri (121450137)
4. Yunita Amelia Puspitasari (121450118)
5. Jasmine Georgina Sekartaji (121450159)
6. Nadia Fitri Yani (121450101)

## 🐸 Latar Belakang
Anura, yang dikenal secara umum sebagai katak, merepresentasikan kelompok amfibia dengan diversitas taksonomi yang substansial dan memiliki signifikansi ekologis yang vital sebagai regulator populasi arthropoda serta indikator biologis untuk mengevaluasi integritas ekosistem. Akan tetapi, eksistensi taksa ini mengalami degradasi populasi yang mengkhawatirkan sebagai konsekuensi dari fragmentasi habitat, kontaminasi antropogenik, dan fluktuasi iklim global. Vokalisasi spesifik yang diekspresikan oleh setiap spesies dapat diimplementasikan sebagai instrumen surveillans ekologis yang efisien. Melalui ekstraksi karakteristik akustik menggunakan Mel-frequency Cepstral Coefficients (MFCC) yang diintegrasikan dengan arsitektur pembelajaran mendalam DenseNet, identifikasi sinyal akustik dapat dieksekusi dengan presisi yang superior, bahkan dalam kondisi akustik lingkungan yang heterogen. C

## ✍️ Tujuan Penelitian
1. Mengklasifikasikan suara katak dari berbagai spesies menggunakan deep learning.
2. Memanfaatkan Mel-frequency Cepstral Coefficients (MFCC) untuk ekstraksi fitur suara.
3. Membandingkan performa model Modified DenseNet-121 dan DenseNet-169 dalam klasifikasi suara katak.

## 🗃️ Dataset
Akuisisi data akustik dilakukan melalui repositori digital Xenocanto, yang mencakup rekaman vokalisasi dari sembilan spesies anura, meliputi: Boana cinerascens, Hyla squirella (Papper Treefrog), Pelophylax lessonae (Pool Frog), Leptodactylus mystaceus (South American White-lipped Grassfrog), Dendropsophus minutus, Rana temporaria, Rhinella marina, Leptodactylus fuscus, dan Scinax ruber. Korpus data terdiri dari 1.512 sampel rekaman vokalisasi yang mengalami transformasi format dari kompresi MP3 ke format audio digital WAV untuk memfasilitasi analisis lebih lanjut.

## 🔄 Pra-Proses Data
a. **Segmentasi Data**

  Spesimen akustik mengalami proses segmentasi temporal dengan interval quintal untuk menghasilkan uniformitas dalam proses analisis subsekuen. Tahap inisial melibatkan implementasi algoritma reduksi noise untuk optimalisasi rasio signal-to-noise, sehingga meningkatkan kualitas akustik secara signifikan. Selanjutnya, dilakukan kategorisasi segmen berdasarkan nomenklatur spesies yang terintegrasi dalam sistem penamaan file, disertai dengan kuantifikasi frekuensi sampel per kategori taksonomi untuk memfasilitasi analisis distribusi data. Kulminasi dari prosedur segmentasi menghasilkan 1.512 unit sampel akustik yang telah terstandarisasi dan siap untuk disubjekkan pada tahapan analisis lebih komprehensif.
  
b. **Ekstraksi MFCC**

  Ekstraksi fitur spektral dilakukan melalui derivasi tiga belas koefisien Mel-frequency Cepstral Coefficients (MFCC), yang merepresentasikan karakteristik frekuensi yang berkorespondensi dengan sistem auditori manusia. Hasil kuantifikasi ini kemudian direpresentasikan secara visual melalui plot temporal untuk mengilustrasikan dinamika variasi koefisien, memfasilitasi interpretasi karakteristik akustik secara komprehensif. Matriks koefisien MFCC yang telah diekstrak dikodifikasi dalam format yang mengoptimalkan efisiensi analisis subsekuen, menghasilkan korpus data yang terdiri dari 1.512 representasi MFCC yang telah terstruktur untuk pemrosesan lebih lanjut.

## 🌐 Model

a. **Modified DenseNet-121**

  Arsitektur Modified DenseNet-121 diimplementasikan dengan struktur hierarkis yang terdiri dari 121 lapisan konvolusional yang diinterkoneksikan melalui mekanisme Dense Connectivity, memungkinkan propagasi informasi multilateral antar lapisan untuk optimalisasi ekstraksi representasi fitur. Modifikasi arsitektural yang diintegrasikan meliputi: inkorporasi layer Batch Normalization untuk akselerasi konvergensi dalam proses pembelajaran, augmentasi dual layer Dropout untuk mitigasi overfitting, serta implementasi Adaptive Average Pooling untuk melakukan reduksi dimensionalitas ke dalam representasi spasial 1x1 yang mendahului tahap klasifikasi final. Konfigurasi arsitektural ini didesain untuk memaksimalkan kapabilitas ekstraksi fitur diskriminatif sambil mempertahankan efisiensi komputasional.
  
b. **Modified DenseNet-169**

  Arsitektur Modified DenseNet-169 dikonstruksi dengan struktur yang terdiri dari 169 lapisan konvolusional yang terintegrasi melalui pola konektivitas densitas tinggi, memfasilitasi ekstraksi karakteristik akustik dengan tingkat kompleksitas superior. Adaptasi struktural yang diimplementasikan mencakup: integrasi layer Batch Normalization untuk normalisasi distribusi aktivasi dan akselerasi proses optimasi, inkorporasi mekanisme Dropout untuk mitigasi overfitting dan augmentasi kapabilitas generalisasi, serta aplikasi Adaptive Average Pooling untuk reduksi kompleksitas komputasional dan standardisasi dimensi fitur pra-klasifikasi. Konfigurasi arsitektural yang sophisticated ini didesain untuk memaksimalkan ekstraksi representasi fitur diskriminatif sambil mempertahankan efisiensi komputasional dan stabilitas pembelajaran.

## 🎯 Hasil

Berikut ini hasil berdasarkan matrik evalusi serta grafik akurasi pelatihan dan validasi dari kedua model:

![image](https://github.com/user-attachments/assets/f3baa249-a726-4550-bb6e-dd8a18f8fd90)

![image](https://github.com/user-attachments/assets/99dcfee4-7250-4e49-a807-06c7ab674fb9)

Model Modified DenseNet-121 menunjukkan kinerja yang lebih unggul dibandingkan dengan Modified DenseNet-169 dalam konteks klasifikasi suara katak, dengan tingkat akurasi mencapai 68%. Metrik evaluasi seperti precision, recall, dan F1-score memperkuat efektivitas model ini dalam mengidentifikasi spesies katak. Penelitian ini memberikan kontribusi signifikan terhadap pemantauan keanekaragaman hayati serta upaya konservasi katak. Penelitian di masa depan dapat mengeksplorasi penggunaan model atau teknik ekstraksi fitur yang lebih canggih, serta mengembangkan dataset yang lebih luas dan beragam untuk meningkatkan kemampuan generalisasi model.


