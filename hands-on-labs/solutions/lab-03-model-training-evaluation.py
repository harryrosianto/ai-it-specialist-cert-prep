"""
Lab 3 (Domain 3) - SOLUSI LENGKAP
==================================
Jalankan langsung: python solutions/lab-03-model-training-evaluation.py
"""

import os
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    precision_score, recall_score, f1_score, confusion_matrix
)

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

# 1. Train model default (best-guess parameters)
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

def evaluate_model(model, X_tr, y_tr, X_te, y_te, name="Model"):
    train_acc = model.score(X_tr, y_tr)
    test_acc = model.score(X_te, y_te)
    print(f"\n[{name}] Akurasi Train: {train_acc:.3f}")
    print(f"[{name}] Akurasi Test : {test_acc:.3f}")
    gap = train_acc - test_acc
    if gap > 0.10:
        print(f"⚠️  Gap besar ({gap:.2f}) -> indikasi OVERFITTING")
    else:
        print(f"✅ Gap kecil ({gap:.2f}) -> model cukup general")
    return train_acc, test_acc

evaluate_model(tree_model, X_train, y_train, X_test, y_test, "Decision Tree (default, unlimited depth)")

# 3. Tuning: batasi kedalaman untuk mengurangi overfitting
tree_model_shallow = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_model_shallow.fit(X_train, y_train)
evaluate_model(tree_model_shallow, X_train, y_train, X_test, y_test, "Decision Tree (max_depth=3)")
print(">> Model default biasanya punya akurasi train ~1.0 (menghafal data)")
print(">> tapi test lebih rendah -> overfitting. max_depth=3 sedikit mengorbankan")
print(">> akurasi train demi model yang lebih general (avoid overengineering, 3.3).")

# 4. Metrik evaluasi lengkap
y_pred = tree_model_shallow.predict(X_test)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n--- Metrik evaluasi lengkap (Decision Tree max_depth=3) ---")
print(f"Precision: {prec:.3f}")
print(f"Recall   : {rec:.3f}")
print(f"F1-score : {f1:.3f}")
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))
print(">> Di kasus kanker, RECALL untuk kelas malignant (0) sangat penting")
print(">> -> false negative (kanker terlewat) jauh lebih berbahaya daripada")
print(">> false positive (pasien sehat dicurigai, lalu diperiksa ulang).")

# 5. Explainability
top_features = pd.Series(
    tree_model_shallow.feature_importances_, index=X_train.columns
).sort_values(ascending=False).head(5)

print("\n--- 5 fitur paling penting (explainability, sub-3.6) ---")
print(top_features)

# 6. Bandingkan dengan Logistic Regression
logreg = LogisticRegression(max_iter=5000)
logreg.fit(X_train, y_train)
evaluate_model(logreg, X_train, y_train, X_test, y_test, "Logistic Regression")

print("""
--- Kesimpulan trade-off (contoh) ---
Decision tree (max_depth=3) menawarkan EXPLAINABILITY tinggi -- kita bisa
lihat persis fitur mana yang paling menentukan keputusan (feature_importances_),
cocok kalau butuh audit trail yang mudah dijelaskan ke non-teknis (3.3).
Logistic regression sering punya akurasi sedikit lebih tinggi/stabil pada
dataset seperti ini, tapi koefisiennya sedikit lebih sulit dijelaskan ke
orang awam dibanding alur decision tree yang bisa digambar sebagai flowchart.
Pilihan akhir tergantung kebutuhan: kalau regulator/user butuh penjelasan
yang sangat mudah dipahami, decision tree lebih unggul meski akurasi
sedikit lebih rendah -- ini contoh nyata trade-off "avoid overengineering".
""")
