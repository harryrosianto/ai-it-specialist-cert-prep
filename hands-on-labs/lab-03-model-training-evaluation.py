"""
Lab 3 (Domain 3): AI Algorithms and Models
============================================
Tujuan: latihan training model, tuning hyperparameter, deteksi overfitting,
        evaluasi metrik (accuracy/precision/recall/F1), cek explainability
        (feature importance), dan bias check sederhana.

Isi bagian "# TODO" di bawah ini.
Jawaban lengkap ada di solutions/lab-03-model-training-evaluation.py

Catatan: script ini otomatis fallback memuat data langsung dari sklearn
kalau file dari Lab 2 (lab02_*.csv) belum ada, supaya tetap bisa dicoba
standalone.
"""

import os
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)

# ------------------------------------------------------------------
# 0. Muat data (dari Lab 2 kalau ada, atau langsung dari sklearn)
# ------------------------------------------------------------------
if os.path.exists("lab02_X_train.csv"):
    X_train = pd.read_csv("lab02_X_train.csv")
    X_test = pd.read_csv("lab02_X_test.csv")
    y_train = pd.read_csv("lab02_y_train.csv").iloc[:, 0]
    y_test = pd.read_csv("lab02_y_test.csv").iloc[:, 0]
    print("Memuat data hasil Lab 2.")
else:
    print("File Lab 2 tidak ditemukan, memuat data langsung dari sklearn.")
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="target")
    X = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

# ------------------------------------------------------------------
# 1. Sub-objektif 3.2: Train model dengan best-guess starting parameters
# ------------------------------------------------------------------
# TODO 1: Buat DecisionTreeClassifier dengan random_state=42 (parameter
# lain default dulu / "best-guess"), lalu latih (.fit) dengan X_train, y_train.
# Simpan ke variabel `tree_model`.
tree_model = None  # <-- ganti dengan kode kamu

# ------------------------------------------------------------------
# 2. Sub-objektif 3.5: Evaluasi performa model (cek overfitting)
# ------------------------------------------------------------------
def evaluate_model(model, X_tr, y_tr, X_te, y_te, name="Model"):
    """Fungsi bantu: cetak akurasi train vs test untuk cek overfitting."""
    # TODO 2: Hitung akurasi model pada data TRAIN dan data TEST.
    # Simpan ke train_acc dan test_acc.
    # Petunjuk: model.score(X, y) langsung mengembalikan akurasi.
    train_acc = None  # <-- ganti dengan kode kamu
    test_acc = None   # <-- ganti dengan kode kamu

    print(f"\n[{name}] Akurasi Train: {train_acc}")
    print(f"[{name}] Akurasi Test : {test_acc}")
    if train_acc is not None and test_acc is not None:
        gap = train_acc - test_acc
        if gap > 0.10:
            print(f"⚠️  Gap besar ({gap:.2f}) -> indikasi OVERFITTING")
        else:
            print(f"✅ Gap kecil ({gap:.2f}) -> model cukup general")
    return train_acc, test_acc

if tree_model is not None:
    evaluate_model(tree_model, X_train, y_train, X_test, y_test, "Decision Tree (default)")

# ------------------------------------------------------------------
# 3. Sub-objektif 3.2/3.3: Tuning hyperparameter, hindari overengineering
# ------------------------------------------------------------------
# TODO 3: Decision tree tanpa batas kedalaman (max_depth=None) sering
# overfit karena "menghafal" data training. Latih ULANG decision tree
# dengan max_depth=3 (lebih sederhana), simpan ke `tree_model_shallow`,
# lalu evaluasi dengan evaluate_model() seperti di atas.
tree_model_shallow = None  # <-- ganti dengan kode kamu

if tree_model_shallow is not None:
    evaluate_model(tree_model_shallow, X_train, y_train, X_test, y_test, "Decision Tree (max_depth=3)")
    print(">> Bandingkan gap train-test antara model default vs max_depth=3.")
    print(">> Model mana yang lebih general (avoid overengineering, 3.3)?")

# ------------------------------------------------------------------
# 4. Sub-objektif 3.5: Metrik evaluasi lengkap (bukan cuma akurasi!)
# ------------------------------------------------------------------
# TODO 4: Untuk tree_model_shallow, hitung precision, recall, dan f1-score
# pada data TEST. Simpan ke prec, rec, f1.
# Petunjuk: gunakan precision_score(y_test, y_pred), dst.
# Jangan lupa buat y_pred dulu dengan tree_model_shallow.predict(X_test)
y_pred = None  # <-- ganti dengan kode kamu
prec, rec, f1 = None, None, None  # <-- ganti dengan kode kamu

print("\n--- TODO 4: Metrik evaluasi lengkap (Decision Tree max_depth=3) ---")
if prec is not None:
    print(f"Precision: {prec:.3f}")
    print(f"Recall   : {rec:.3f}")
    print(f"F1-score : {f1:.3f}")
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 5. Sub-objektif 3.6: Explainability & feature importance
# ------------------------------------------------------------------
# TODO 5: Ambil feature_importances_ dari tree_model_shallow, urutkan dari
# yang paling penting, tampilkan 5 fitur teratas. Simpan ke `top_features`
# (pandas Series dengan index = nama fitur, value = importance).
top_features = None  # <-- ganti dengan kode kamu

print("\n--- TODO 5: 5 fitur paling penting (explainability, sub-3.6) ---")
if top_features is not None:
    print(top_features)
else:
    print("Belum diisi!")

# ------------------------------------------------------------------
# 6. Sub-objektif 3.3: Bandingkan dengan algoritma lain (trade-off)
# ------------------------------------------------------------------
# TODO 6 (opsional, eksplorasi): Latih LogisticRegression(max_iter=5000)
# pada data yang sama, evaluasi, dan bandingkan trade-off (akurasi vs
# explainability) dengan Decision Tree. Tulis kesimpulanmu di komentar.
#
# KESIMPULANMU:
# ...
