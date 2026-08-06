"""
Lab 2 (Domain 2) - SOLUSI LENGKAP
==================================
Jalankan langsung: python solutions/lab-02-data-processing.py
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Muat data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")
print(f"Jumlah sampel: {X.shape[0]}, Jumlah fitur: {X.shape[1]}")

# 2. Simulasikan data kotor
rng = np.random.RandomState(42)
X_dirty = X.copy()
missing_mask = rng.rand(*X_dirty.shape) < 0.03
X_dirty = X_dirty.mask(missing_mask)

# TODO 1: hitung missing value per kolom
missing_per_column = X_dirty.isna().sum()
print("\n--- Missing values per kolom (5 teratas) ---")
print(missing_per_column.sort_values(ascending=False).head())

# TODO 2: impute dengan median
X_clean = X_dirty.fillna(X_dirty.median())
print("\n--- Sisa missing value setelah imputasi ---")
print(f"Total missing value tersisa: {X_clean.isna().sum().sum()}")

# 3. Representativeness / class balance
class_distribution = y.value_counts(normalize=True) * 100
print("\n--- Distribusi kelas (%) ---")
print(class_distribution)
print(">> Dataset ini relatif seimbang (~63% vs ~37%), tidak separah kasus")
print(">> fraud detection (mis. 0.1% vs 99.9%), tapi tetap perlu diperhatikan")
print(">> saat memilih metrik evaluasi (precision/recall vs akurasi saja).")

# 4. Feature scaling
scaler = StandardScaler()
X_scaled = pd.DataFrame(
    scaler.fit_transform(X_clean), columns=X_clean.columns
)
print("\n--- Statistik setelah scaling (harus mean~0, std~1) ---")
print(X_scaled.describe().loc[["mean", "std"]].iloc[:, :3])

# 5. Train/test split dengan stratify
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)
print("\n--- Ukuran train/test split ---")
print(f"Train: {X_train.shape[0]} sampel, Test: {X_test.shape[0]} sampel")
print("Distribusi kelas di test set (%):")
print(y_test.value_counts(normalize=True) * 100)
print(">> Dengan stratify=y, proporsi kelas di test set MIRIP dengan")
print(">> keseluruhan data -> test set representatif (sub-objektif 2.8).")

# 6. Dokumentasi keputusan (contoh jawaban)
print("""
--- Contoh dokumentasi keputusan data (sub-objektif 2.9) ---
1. Missing value (~3% dari total sel) diisi dengan median per kolom,
   bukan dihapus barisnya, untuk menghindari kehilangan data yang
   signifikan mengingat dataset relatif kecil (569 sampel).
2. Fitur distandarkan (StandardScaler) karena skala antar fitur sangat
   berbeda (mis. 'mean area' vs 'mean smoothness'), penting untuk
   algoritma yang sensitif terhadap skala seperti kNN atau regresi logistik.
3. Split data menggunakan stratify=y untuk menjaga proporsi kelas
   malignant/benign tetap representatif di train maupun test set,
   supaya evaluasi model tidak bias akibat distribusi kelas yang timpang
   secara kebetulan pada satu split tertentu.
""")

# Simpan untuk Lab 3
X_train.to_csv("lab02_X_train.csv", index=False)
X_test.to_csv("lab02_X_test.csv", index=False)
y_train.to_csv("lab02_y_train.csv", index=False)
y_test.to_csv("lab02_y_test.csv", index=False)
print("✅ Data hasil Lab 2 disimpan (lab02_*.csv), siap dipakai di Lab 3.")
