"""
Lab 5 (Domain 5): Maintaining and Monitoring AI in Production
================================================================
Tujuan: mensimulasikan DATA DRIFT (distribusi data produksi berubah dari
        data training), mendeteksinya secara statistik, mengukur dampak
        pada performa model, dan latihan membuat keputusan
        retrain/lanjutkan/decommission (5.5).

Isi bagian "# TODO" di bawah ini.
Jawaban lengkap ada di solutions/lab-05-monitoring-drift-detection.py
"""

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score

# ------------------------------------------------------------------
# 0. Siapkan model & data "produksi" awal (mirroring kondisi saat training)
# ------------------------------------------------------------------
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")

scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

X_train, X_ref, y_train, y_ref = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)
# X_ref/y_ref berperan sebagai "batch data produksi awal" (mirip distribusi training)

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

baseline_acc = model.score(X_ref, y_ref)
baseline_recall = recall_score(y_ref, model.predict(X_ref))
print(f"Baseline accuracy (batch awal, mirip training): {baseline_acc:.3f}")
print(f"Baseline recall  (batch awal, mirip training): {baseline_recall:.3f}")

# ------------------------------------------------------------------
# 1. Simulasikan DATA DRIFT pada batch data baru
#    (mis. sensor/alat ukur di rumah sakit diganti, hasil sedikit bergeser)
# ------------------------------------------------------------------
rng = np.random.RandomState(7)
X_drifted = X_ref.copy()
# Fitur ini dipilih karena PALING berpengaruh terhadap keputusan model
# (lihat feature_importances_ di Lab 3) -- supaya efek drift ke performa
# benar-benar terasa, bukan bergeser di fitur yang kurang relevan.
drift_features = ["worst concave points", "worst radius", "mean texture"]
# TODO 1: Untuk kolom-kolom di `drift_features`, kurangi semua nilainya
# sebesar 2.5 (dalam skala data yang sudah di-scale, ini pergeseran besar).
# Ini mensimulasikan perubahan distribusi input di dunia nyata (data drift),
# mis. karena alat ukur/sensor diganti.
# Petunjuk: X_drifted[col] = X_drifted[col] - 2.5
for col in drift_features:
    pass  # <-- ganti dengan kode kamu

# ------------------------------------------------------------------
# 2. Sub-objektif 5.1/5.2: Ukur dampak drift pada performa model
# ------------------------------------------------------------------
# TODO 2: Hitung accuracy dan recall model pada X_drifted (dengan label
# y_ref, karena label sebenarnya sama, yang berubah cuma fitur inputnya).
# Simpan ke drifted_acc dan drifted_recall.
drifted_acc = None     # <-- ganti dengan kode kamu
drifted_recall = None  # <-- ganti dengan kode kamu

print("\n--- TODO 2: Performa model setelah drift ---")
if drifted_acc is not None:
    print(f"Accuracy setelah drift: {drifted_acc:.3f} (baseline: {baseline_acc:.3f})")
    print(f"Recall setelah drift  : {drifted_recall:.3f} (baseline: {baseline_recall:.3f})")
    drop = baseline_acc - drifted_acc
    print(f"Penurunan akurasi: {drop:.3f}")
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 3. Sub-objektif 5.1: Deteksi drift SECARA STATISTIK (bukan cuma nebak)
#    Gunakan Kolmogorov-Smirnov test untuk membandingkan distribusi
#    setiap fitur antara data referensi (training-like) vs data baru.
# ------------------------------------------------------------------
def detect_drift(X_reference: pd.DataFrame, X_new: pd.DataFrame, alpha=0.05):
    """
    TODO 3: Untuk setiap kolom di X_reference, lakukan uji KS
    (stats.ks_2samp) antara distribusi di X_reference[col] dan X_new[col].
    Jika p-value < alpha, tandai kolom tersebut sebagai "drifted".
    Return: list nama kolom yang terdeteksi drift.
    """
    drifted_columns = []
    for col in X_reference.columns:
        # TODO: lakukan stats.ks_2samp(X_reference[col], X_new[col])
        # ambil p-value, jika < alpha -> tambahkan `col` ke drifted_columns
        pass
    return drifted_columns

print("\n--- TODO 3: Deteksi drift otomatis (uji statistik KS) ---")
detected = detect_drift(X_ref, X_drifted)
if detected:
    print(f"⚠️  ALERT: Drift terdeteksi pada {len(detected)} fitur: {detected}")
else:
    print("Belum diisi, atau tidak ada drift terdeteksi (cek TODO 3)")

# ------------------------------------------------------------------
# 4. Sub-objektif 5.3: Cek dampak pada subgrup (di sini: per kelas)
# ------------------------------------------------------------------
# TODO 4: Bandingkan recall SEBELUM dan SESUDAH drift, KHUSUS untuk
# kelas malignant (label=0) -- kelas paling kritis di kasus medis.
# Petunjuk: filter y_ref == 0 dan y_drifted (sama saja y_ref) == 0,
# lalu hitung recall_score hanya pada subset itu (atau gunakan
# recall_score dengan pos_label=0).
recall_malignant_before = None  # <-- ganti dengan kode kamu
recall_malignant_after = None   # <-- ganti dengan kode kamu

print("\n--- TODO 4: Dampak drift khusus kelas malignant (paling kritis) ---")
if recall_malignant_before is not None:
    print(f"Recall malignant SEBELUM drift: {recall_malignant_before:.3f}")
    print(f"Recall malignant SESUDAH drift: {recall_malignant_after:.3f}")
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 5. Sub-objektif 5.5: Keputusan retrain / lanjutkan / decommission
# ------------------------------------------------------------------
# TODO 5 (tidak perlu kode, jawab dengan tulisan di komentar):
# Berdasarkan hasil TODO 2-4 di atas, apa keputusan yang akan kamu ambil?
# Pertimbangkan: seberapa besar penurunan performa, apakah drift terjadi
# di banyak fitur atau sedikit, dan apakah dampaknya lebih parah pada
# kelas kritis (malignant).
#
# KEPUTUSANMU (retrain / lanjutkan apa adanya / decommission) & ALASAN:
# ...
