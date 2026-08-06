"""
Lab 5 (Domain 5) - SOLUSI LENGKAP
==================================
Jalankan langsung: python solutions/lab-05-monitoring-drift-detection.py
"""

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score

# 0. Siapkan model & data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
X_train, X_ref, y_train, y_ref = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

baseline_acc = model.score(X_ref, y_ref)
baseline_recall = recall_score(y_ref, model.predict(X_ref))
print(f"Baseline accuracy (batch awal, mirip training): {baseline_acc:.3f}")
print(f"Baseline recall  (batch awal, mirip training): {baseline_recall:.3f}")

# 1. Simulasikan drift -- geser fitur yang PALING berpengaruh ke keputusan
# model (sesuai feature_importances_ dari Lab 3: 'worst concave points'
# dan 'worst radius' adalah fitur paling dominan), supaya efek drift
# terhadap performa benar-benar terasa, bukan cuma bergeser di fitur
# yang kurang relevan bagi model ini.
rng = np.random.RandomState(7)
X_drifted = X_ref.copy()
drift_features = ["worst concave points", "worst radius", "mean texture"]
for col in drift_features:
    X_drifted[col] = X_drifted[col] - 2.5  # simulasikan sensor bergeser signifikan

# 2. Ukur dampak pada performa
drifted_acc = model.score(X_drifted, y_ref)
drifted_recall = recall_score(y_ref, model.predict(X_drifted))

print("\n--- Performa model setelah drift ---")
print(f"Accuracy setelah drift: {drifted_acc:.3f} (baseline: {baseline_acc:.3f})")
print(f"Recall setelah drift  : {drifted_recall:.3f} (baseline: {baseline_recall:.3f})")
print(f"Penurunan akurasi: {baseline_acc - drifted_acc:.3f}")

# 3. Deteksi drift statistik (KS test)
def detect_drift(X_reference: pd.DataFrame, X_new: pd.DataFrame, alpha=0.05):
    drifted_columns = []
    for col in X_reference.columns:
        stat, p_value = stats.ks_2samp(X_reference[col], X_new[col])
        if p_value < alpha:
            drifted_columns.append(col)
    return drifted_columns

detected = detect_drift(X_ref, X_drifted)
print(f"\n--- Deteksi drift otomatis (uji statistik KS, alpha=0.05) ---")
print(f"⚠️  ALERT: Drift terdeteksi pada {len(detected)} dari {X_ref.shape[1]} fitur:")
print(detected)
print(">> Perhatikan: KS test berhasil menandai TEPAT fitur-fitur yang")
print(f">> sengaja kita geser ({', '.join(drift_features)})")
print(">> -- inilah cara kerja drift detector otomatis di sistem produksi nyata (4.4/5.1).")

# 4. Dampak pada subgrup kritis (kelas malignant = 0)
mask_malignant = y_ref == 0
y_pred_before = model.predict(X_ref)
y_pred_after = model.predict(X_drifted)

recall_malignant_before = recall_score(
    y_ref[mask_malignant], y_pred_before[mask_malignant.values], pos_label=0
) if mask_malignant.sum() > 0 else None
recall_malignant_after = recall_score(
    y_ref[mask_malignant], y_pred_after[mask_malignant.values], pos_label=0
) if mask_malignant.sum() > 0 else None

print("\n--- Dampak drift khusus kelas malignant (paling kritis) ---")
print(f"Recall malignant SEBELUM drift: {recall_malignant_before:.3f}")
print(f"Recall malignant SESUDAH drift: {recall_malignant_after:.3f}")

# 5. Keputusan
print("""
--- Contoh keputusan (sub-objektif 5.5) ---
Drift terdeteksi secara statistik pada beberapa fitur kunci, DAN penurunan
recall pada kelas malignant (kelas paling kritis secara medis) cukup
signifikan. Dalam konteks medis, penurunan kemampuan mendeteksi kasus
positif (malignant) adalah risiko yang tidak bisa diterima meski akurasi
keseluruhan masih terlihat "lumayan".

Keputusan yang tepat: RETRAIN model dengan data baru yang mencerminkan
distribusi produksi saat ini SEGERA, bukan menunggu siklus retraining
terjadwal berikutnya -- dan sementara menunggu proses retrain selesai,
pertimbangkan menaikkan ambang kehati-hatian (mis. rujuk manual semua
kasus borderline) sebagai mitigasi sementara. Ini juga jadi masukan untuk
memperkuat sub-objektif 4.2 (rencana mitigasi tantangan produksi) di masa
depan -- drift akibat perubahan alat/sensor seharusnya sudah diantisipasi
sejak desain awal pipeline monitoring.
""")
