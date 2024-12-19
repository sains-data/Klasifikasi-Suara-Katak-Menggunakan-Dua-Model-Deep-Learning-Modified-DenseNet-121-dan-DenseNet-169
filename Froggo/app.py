import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from model import ModifiedDenseNet169  # Pastikan ini sesuai dengan file model Anda
import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import tempfile

# Inisialisasi model
@st.cache_resource
def load_model():
    model = ModifiedDenseNet169(num_classes=9)
    model.load_state_dict(torch.load("model_densenet169_frog_classifier.pth", map_location=torch.device('cpu')))  # Pastikan file model.pth ada
    model.eval()
    return model

# Fungsi untuk konversi MP3 ke MFCC
def process_audio_to_mfcc(mp3_path):
    try:
        # Konversi MP3 ke WAV menggunakan Librosa
        y, sr = librosa.load(mp3_path, sr=None)
        
        # Ekstrak MFCC
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfcc_normalized = (mfcc - np.min(mfcc)) / (np.max(mfcc) - np.min(mfcc)) * 255  # Normalisasi
        mfcc_image = Image.fromarray(mfcc_normalized.astype(np.uint8)).convert("L")  # Konversi ke grayscale
        return mfcc_image
    except Exception as e:
        raise RuntimeError(f"Error processing audio to MFCC: {e}")

# Fungsi untuk prediksi
def predict(image, model, transform, label_dict):
    image = transform(image).unsqueeze(0)  # Tambahkan batch dimension
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    label = [k for k, v in label_dict.items() if v == predicted.item()]
    return label[0] if label else "Unknown"

# Fungsi untuk menampilkan gambar kodok berdasarkan label prediksi
def get_frog_image(label):
    image_path = f"frog_images/{label}.jpg"
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        return None

# Transformasi gambar
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Dictionary label
label_dict = {
    'Boana': 0,
    'Pool': 1,
    'PepperFrog': 2,
    'South': 3,
    'Dendropsophus': 4,
    'Leptodactylus': 5,
    'Rana': 6,
    'Rhinella': 7,
    'Scinax': 8
}

# Streamlit antarmuka
st.title("Klasifikasi Suara Katak")
st.write("Unggah file audio MP3 untuk memprediksi jenis suara katak.")

uploaded_file = st.file_uploader("Unggah file .mp3", type=["mp3"])

if uploaded_file is not None:
    try:
        # Simpan file audio sementara
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
            temp_audio_file.write(uploaded_file.getbuffer())
            temp_audio_path = temp_audio_file.name

        # Proses MP3 ke MFCC
        mfcc_image = process_audio_to_mfcc(temp_audio_path)

        # Tampilkan gambar MFCC
        st.image(mfcc_image, caption="MFCC dari Audio Input", use_container_width=True)

        # Load model
        model = load_model()

        # Lakukan prediksi
        label = predict(mfcc_image, model, transform, label_dict)

        st.success(f"Prediksi: {label}")

        # Tampilkan gambar kodok berdasarkan prediksi
        frog_image = get_frog_image(label)
        if frog_image:
            st.image(frog_image, caption=f"Gambar: {label}", use_container_width=True)
        else:
            st.warning(f"Tidak ada gambar yang cocok untuk label: {label}")

        # Hapus file sementara
        os.remove(temp_audio_path)
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
