"""
Lab 2 (Domain 2): Data Collection, Processing, and Engineering
================================================================
Dataset: Breast Cancer Wisconsin (bawaan sklearn, tidak perlu download)
Tujuan: latihan cek kualitas data, representativeness (class balance),
        scaling fitur, dan split train/test.

Isi bagian yang ditandai "# TODO" di bawah ini.
Jawaban lengkap ada di solutions/lab-02-data-processing.py
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ------------------------------------------------------------------
# 1. Muat data (anggap ini "data yang sudah dikumpulkan" - sub-objektif 2.1)
# ------------------------------------------------------------------
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")  # 0 = malignant, 1 = benign

print(f"Jumlah sampel: {X.shape[0]}, Jumlah fitur: {X.shape[1]}")

# ------------------------------------------------------------------
# 2. Simulasikan data yang "kotor" (real-world data jarang sempurna)
#    Kita sengaja rusak beberapa nilai jadi NaN untuk latihan.
# ------------------------------------------------------------------
rng = np.random.RandomState(42)
X_dirty = X.copy()
missing_mask = rng.rand(*X_dirty.shape) < 0.03  # ~3% nilai jadi hilang
X_dirty = X_dirty.mask(missing_mask)

# TODO 1 (sub-objektif 2.2 - Assess data quality):
# Hitung berapa banyak nilai yang hilang (missing) per kolom pada X_dirty.
# Simpan hasilnya ke variabel `missing_per_column` (pandas Series).
# Petunjuk: gunakan .isna().sum()
missing_per_column = None  # <-- ganti dengan kode kamu

print("\n--- TODO 1: Missing values per kolom (5 teratas) ---")
if missing_per_column is not None:
    print(missing_per_column.sort_values(ascending=False).head())
else:
    print("Belum diisi!")

# TODO 2 (sub-objektif 2.2 - Assess data quality):
# Tangani missing value dengan mengisi (impute) menggunakan median tiap kolom.
# Simpan hasilnya ke variabel `X_clean`.
# Petunjuk: gunakan .fillna(X_dirty.median())
X_clean = None  # <-- ganti dengan kode kamu

print("\n--- TODO 2: Sisa missing value setelah imputasi ---")
if X_clean is not None:
    print(f"Total missing value tersisa: {X_clean.isna().sum().sum()}")
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 3. Cek representativeness data (sub-objektif 2.3)
# ------------------------------------------------------------------
# TODO 3: Hitung distribusi kelas target (y).
# Berapa persen data yang malignant (0) vs benign (1)?
# Simpan ke variabel `class_distribution` (dalam persen).
# Petunjuk: gunakan y.value_counts(normalize=True) * 100
class_distribution = None  # <-- ganti dengan kode kamu

print("\n--- TODO 3: Distribusi kelas (%) ---")
if class_distribution is not None:
    print(class_distribution)
    print("\n>> Pertanyaan refleksi: apakah data ini termasuk imbalanced?")
    print(">> (bandingkan dengan aturan umum: imbalanced jika kelas minoritas < 20-30%)")
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 4. Feature scaling (sub-objektif 2.5 - convert ke format yang sesuai)
# ------------------------------------------------------------------
# TODO 4: Gunakan StandardScaler untuk menstandarkan X_clean
# (mean=0, std=1). Simpan hasilnya ke `X_scaled` (tetap sebagai DataFrame
# dengan nama kolom yang sama).
scaler = StandardScaler()
X_scaled = None  # <-- ganti dengan kode kamu

print("\n--- TODO 4: Statistik setelah scaling (harus mean~0, std~1) ---")
if X_scaled is not None:
    print(X_scaled.describe().loc[["mean", "std"]].iloc[:, :3])
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 5. Train/test split (sub-objektif 2.8)
# ------------------------------------------------------------------
# TODO 5: Split X_scaled dan y menjadi train (80%) dan test (20%).
# PENTING: gunakan stratify=y agar proporsi kelas di test set representatif
# terhadap keseluruhan data (poin penting sub-objektif 2.8!).
# Simpan ke X_train, X_test, y_train, y_test. random_state=42
X_train, X_test, y_train, y_test = None, None, None, None  # <-- ganti

print("\n--- TODO 5: Ukuran train/test split ---")
if X_train is not None:
    print(f"Train: {X_train.shape[0]} sampel, Test: {X_test.shape[0]} sampel")
    print("Distribusi kelas di test set (%):")
    print(y_test.value_counts(normalize=True) * 100)
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 6. Dokumentasi keputusan data (sub-objektif 2.9)
# ------------------------------------------------------------------
# TODO 6 (tidak perlu kode, cukup jawab dalam komentar di bawah ini):
# Tuliskan 2-3 asumsi/keputusan yang kamu buat di lab ini yang PERLU
# didokumentasikan untuk regulator/pengguna akhir yang menuntut transparansi.
# Contoh: "Missing value diisi dengan median, bukan dihapus, karena..."
#
# JAWABANMU:
# 1. ...
# 2. ...
# 3. ...

# ------------------------------------------------------------------
# Simpan hasil untuk dipakai di Lab 3 (jika semua TODO sudah diisi)
# ------------------------------------------------------------------
if X_train is not None:
    X_train.to_csv("lab02_X_train.csv", index=False)
    X_test.to_csv("lab02_X_test.csv", index=False)
    y_train.to_csv("lab02_y_train.csv", index=False)
    y_test.to_csv("lab02_y_test.csv", index=False)
    print("\n✅ Data hasil Lab 2 disimpan (lab02_*.csv), siap dipakai di Lab 3.")
else:
    print("\n⚠️  Selesaikan semua TODO dulu sebelum lanjut ke Lab 3.")
