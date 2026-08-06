"""
Lab 4 (Domain 4): Application Integration and Deployment
============================================================
Tujuan: latihan membungkus model jadi "pipeline produksi" -- validasi
        input, uji kecepatan (speed), uji ketahanan (robustness) terhadap
        input aneh/edge case, dan simpan/muat ulang model (simulasi deploy).

Isi bagian "# TODO" di bawah ini.
Jawaban lengkap ada di solutions/lab-04-deployment-simulation.py
"""

import os
import time
import numpy as np
import pandas as pd
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

# ------------------------------------------------------------------
# 0. Siapkan model terlatih (anggap ini hasil dari Lab 3)
# ------------------------------------------------------------------
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# ------------------------------------------------------------------
# 1. Sub-objektif 4.3: Simpan model (simulasikan "deploy")
# ------------------------------------------------------------------
# TODO 1: Simpan `model` dan `scaler` ke file menggunakan joblib.dump().
# Simpan model ke "deployed_model.joblib" dan scaler ke "deployed_scaler.joblib".
# Ini mensimulasikan proses "packaging" solusi AI untuk diintegrasikan
# ke aplikasi (bukan lagi hidup di notebook eksperimen).
# TODO: tulis kode joblib.dump(...) di sini


# TODO 2: Muat ulang model dan scaler dari file yang baru disimpan.
# Simpan ke `loaded_model` dan `loaded_scaler`.
# Ini mensimulasikan aplikasi produksi yang me-load model saat startup.
loaded_model = None   # <-- ganti dengan kode kamu
loaded_scaler = None  # <-- ganti dengan kode kamu

print("Model berhasil dimuat ulang?" , loaded_model is not None)

# ------------------------------------------------------------------
# 2. Sub-objektif 4.3: Bangun "inference function" dengan validasi input
# ------------------------------------------------------------------
FEATURE_NAMES = list(X.columns)

def predict_with_validation(raw_input: dict, model, scaler):
    """
    Fungsi inference untuk 'aplikasi produksi'.
    raw_input: dict {nama_fitur: nilai}

    TODO 3: Lengkapi validasi berikut (sub-objektif 4.1 - inform users of
    model limitations & 4.3 - build robust pipeline):
      a) Jika ada fitur yang HILANG dari raw_input, raise ValueError dengan
         pesan yang menyebutkan fitur mana yang hilang.
      b) Jika ada nilai yang BUKAN angka (bukan int/float), raise ValueError.
      c) Jika semua valid, ubah jadi DataFrame satu baris dengan urutan
         kolom SAMA seperti FEATURE_NAMES, scale dengan `scaler`, lalu
         prediksi dengan `model`. Return hasil prediksi (0 atau 1) dan
         confidence/probability-nya (model.predict_proba).
    """
    # TODO 3a: validasi fitur yang hilang
    missing = None  # <-- ganti dengan kode kamu (list fitur yang hilang)
    if missing:
        raise ValueError(f"Fitur berikut tidak ditemukan di input: {missing}")

    # TODO 3b: validasi tipe data
    for k, v in raw_input.items():
        pass  # <-- ganti dengan validasi kamu (raise ValueError jika bukan angka)

    # TODO 3c: prediksi
    # Petunjuk: bungkus hasil scaler.transform() kembali jadi DataFrame
    # dengan columns=FEATURE_NAMES supaya tidak ada warning "missing feature names".
    row = None       # <-- ganti: buat DataFrame 1 baris sesuai FEATURE_NAMES
    row_scaled = None  # <-- ganti: pd.DataFrame(scaler.transform(row), columns=FEATURE_NAMES)
    pred = None       # <-- ganti: model.predict(row_scaled)[0]
    proba = None      # <-- ganti: model.predict_proba(row_scaled)[0]

    return pred, proba

# Uji dengan satu sampel valid dari test set
sample_valid = X_test.iloc[0].to_dict()
# (catatan: sample ini sudah di-scale, untuk contoh sederhana kita anggap
#  scaler di sini adalah "identity" -- di real project, raw_input harus data MENTAH
#  sebelum scaling. Untuk latihan ini kita tetap panggil scaler agar terbiasa
#  dengan pola pipeline lengkap.)

print("\n--- TODO 3: Uji prediksi dengan input valid ---")
try:
    pred, proba = predict_with_validation(sample_valid, loaded_model or model, loaded_scaler or scaler)
    print(f"Prediksi: {pred}, Probabilitas: {proba}")
except Exception as e:
    print(f"Belum berhasil / error: {e}")

print("\n--- TODO 3: Uji prediksi dengan input TIDAK LENGKAP (harus error) ---")
sample_incomplete = {k: v for i, (k, v) in enumerate(sample_valid.items()) if i < 5}
try:
    pred, proba = predict_with_validation(sample_incomplete, loaded_model or model, loaded_scaler or scaler)
    print(f"⚠️  Seharusnya error, tapi malah berhasil: {pred}")
except ValueError as e:
    print(f"✅ Berhasil menangkap error seperti seharusnya: {e}")
except Exception as e:
    print(f"Error lain (cek lagi TODO 3a): {e}")

# ------------------------------------------------------------------
# 3. Sub-objektif 4.3: Uji kecepatan (speed) model
# ------------------------------------------------------------------
# TODO 4: Ukur waktu rata-rata untuk melakukan 100 kali prediksi berturut-turut
# menggunakan sample_valid. Simpan ke `avg_latency_ms` (dalam milidetik).
# Petunjuk: gunakan time.perf_counter() sebelum & sesudah loop.
avg_latency_ms = None  # <-- ganti dengan kode kamu

print("\n--- TODO 4: Uji kecepatan (speed) ---")
if avg_latency_ms is not None:
    print(f"Rata-rata waktu inferensi: {avg_latency_ms:.4f} ms/prediksi")
    if avg_latency_ms > 50:
        print("⚠️  Cukup lambat untuk aplikasi real-time (mis. mobile).")
    else:
        print("✅ Cukup cepat untuk kebanyakan use case real-time.")
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 4. Sub-objektif 4.3: Uji robustness terhadap edge case
# ------------------------------------------------------------------
# TODO 5: Uji apa yang terjadi kalau salah satu nilai fitur diganti dengan
# nilai EKSTRIM (mis. 1000x lebih besar dari normal) -- simulasikan sensor
# error di dunia nyata. Apakah model masih menghasilkan prediksi yang
# "masuk akal" (probabilitas tidak terlalu ekstrim mendekati 0/1 secara
# aneh) atau justru sangat yakin secara salah?
# Cukup jalankan predict_with_validation dengan satu fitur diubah jadi
# ekstrim, lalu amati hasilnya secara manual (print).
sample_edge_case = dict(sample_valid)
edge_feature = FEATURE_NAMES[0]
# TODO: ubah sample_edge_case[edge_feature] jadi nilai ekstrim
print(f"\n--- TODO 5: Uji robustness (ubah '{edge_feature}' jadi ekstrim) ---")
print("(isi TODO 5 lalu jalankan predict_with_validation pada sample_edge_case)")
