"""
Lab 4 (Domain 4) - SOLUSI LENGKAP
==================================
Jalankan langsung: python solutions/lab-04-deployment-simulation.py
"""

import time
import pandas as pd
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

# 0. Siapkan model terlatih
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

# 1. Simpan model & scaler ("deploy")
joblib.dump(model, "deployed_model.joblib")
joblib.dump(scaler, "deployed_scaler.joblib")
print("Model & scaler disimpan ke disk (simulasi packaging untuk deployment).")

# 2. Muat ulang (simulasi aplikasi produksi saat startup)
loaded_model = joblib.load("deployed_model.joblib")
loaded_scaler = joblib.load("deployed_scaler.joblib")
print("Model berhasil dimuat ulang?", loaded_model is not None)

FEATURE_NAMES = list(X.columns)

def predict_with_validation(raw_input: dict, model, scaler):
    # 3a. Validasi fitur hilang
    missing = [f for f in FEATURE_NAMES if f not in raw_input]
    if missing:
        raise ValueError(f"Fitur berikut tidak ditemukan di input: {missing}")

    # 3b. Validasi tipe data
    for k, v in raw_input.items():
        if not isinstance(v, (int, float)):
            raise ValueError(f"Nilai fitur '{k}' harus berupa angka, dapat: {type(v)}")

    # 3c. Prediksi
    row = pd.DataFrame([[raw_input[f] for f in FEATURE_NAMES]], columns=FEATURE_NAMES)
    row_scaled = pd.DataFrame(scaler.transform(row), columns=FEATURE_NAMES)
    pred = model.predict(row_scaled)[0]
    proba = model.predict_proba(row_scaled)[0]
    return pred, proba

sample_valid = X_test.iloc[0].to_dict()

print("\n--- Uji prediksi dengan input valid ---")
pred, proba = predict_with_validation(sample_valid, loaded_model, loaded_scaler)
print(f"Prediksi: {pred}, Probabilitas: {proba}")

print("\n--- Uji prediksi dengan input TIDAK LENGKAP (harus error) ---")
sample_incomplete = {k: v for i, (k, v) in enumerate(sample_valid.items()) if i < 5}
try:
    predict_with_validation(sample_incomplete, loaded_model, loaded_scaler)
    print("⚠️  Seharusnya error, tapi malah berhasil")
except ValueError as e:
    print(f"✅ Berhasil menangkap error seperti seharusnya: {e}")

print("\n--- Uji prediksi dengan tipe data SALAH (harus error) ---")
sample_bad_type = dict(sample_valid)
sample_bad_type[FEATURE_NAMES[0]] = "bukan_angka"
try:
    predict_with_validation(sample_bad_type, loaded_model, loaded_scaler)
    print("⚠️  Seharusnya error, tapi malah berhasil")
except ValueError as e:
    print(f"✅ Berhasil menangkap error seperti seharusnya: {e}")

# 4. Uji kecepatan
N = 100
start = time.perf_counter()
for _ in range(N):
    predict_with_validation(sample_valid, loaded_model, loaded_scaler)
end = time.perf_counter()
avg_latency_ms = (end - start) / N * 1000

print("\n--- Uji kecepatan (speed) ---")
print(f"Rata-rata waktu inferensi: {avg_latency_ms:.4f} ms/prediksi")
if avg_latency_ms > 50:
    print("⚠️  Cukup lambat untuk aplikasi real-time (mis. mobile).")
else:
    print("✅ Cukup cepat untuk kebanyakan use case real-time.")

# 5. Uji robustness terhadap edge case (nilai ekstrim)
sample_edge_case = dict(sample_valid)
edge_feature = FEATURE_NAMES[0]
original_value = sample_edge_case[edge_feature]
sample_edge_case[edge_feature] = original_value * 1000  # simulasi sensor error

pred_normal, proba_normal = predict_with_validation(sample_valid, loaded_model, loaded_scaler)
pred_edge, proba_edge = predict_with_validation(sample_edge_case, loaded_model, loaded_scaler)

print(f"\n--- Uji robustness (ubah '{edge_feature}' jadi {sample_edge_case[edge_feature]:.2f}, semula {original_value:.2f}) ---")
print(f"Prediksi normal   : {pred_normal}, proba={proba_normal}")
print(f"Prediksi edge case: {pred_edge}, proba={proba_edge}")
if pred_normal != pred_edge:
    print("⚠️  Prediksi BERUBAH akibat satu nilai ekstrim -> model tidak robust")
    print("   terhadap outlier/sensor error pada fitur ini. Di produksi, ini")
    print("   perlu ditangani dengan validasi range nilai wajar SEBELUM prediksi")
    print("   (mis. tolak atau clip nilai di luar rentang yang pernah dilihat")
    print("   model saat training) -- bagian dari 'test robustness' (4.3).")
else:
    print("✅ Prediksi tidak berubah meski satu fitur ekstrim -- model cukup robust")
    print("   untuk kasus ini (tapi tetap perlu diuji dengan fitur lain juga).")
