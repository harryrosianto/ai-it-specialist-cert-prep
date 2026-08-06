# Domain 4: Application Integration and Deployment

---

## 4.1 Melatih Pelanggan Cara Menggunakan Produk

- **Informasikan keterbatasan model** (model limitations) ke pengguna
- **Informasikan penggunaan model yang dimaksud** (intended usage)
- **Bagikan dokumentasi**
- **Kelola ekspektasi pelanggan** (manage expectations) — penting agar pengguna tidak berharap AI 100% sempurna

## 4.2 Merencanakan Penanganan Tantangan Model di Produksi

- Pahami **jenis tantangan** yang mungkin dihadapi (mis. data drift, latency, edge case)
- Pahami **indikator tantangan tersebut** (mis. penurunan akurasi bertahap sebagai indikator drift)
- Pahami **bagaimana setiap jenis tantangan dapat dimitigasi**

## 4.3 Merancang Production Pipeline, Termasuk Integrasi Aplikasi

- Buat **pipeline** (training, prediction) yang memenuhi kebutuhan produk — **bisa berbeda dari saat eksperimen** (lingkungan produksi punya kebutuhan skala & keandalan berbeda)
- Cari solusi yang **kompatibel dengan data store yang ada** dan tersambung ke aplikasi
- Bangun **koneksi antara AI dan aplikasi**
- Bangun **mekanisme mengumpulkan feedback pengguna**
- **Uji akurasi AI melalui aplikasi** (bukan hanya di lingkungan eksperimen)
- **Uji robustness** (ketahanan) AI
- **Uji kecepatan (speed)** AI
- **Uji aplikasi agar sesuai skala use case** (mis. AI untuk aplikasi mobile perlu diuji untuk keterbatasan device)

## 4.4 Mendukung Solusi AI (Support)

- **Dokumentasikan fungsi-fungsi** dalam solusi AI untuk keperluan maintenance (update, perbaikan bug, penanganan edge case)
- **Latih tim support**
- **Implementasikan mekanisme feedback**
- **Implementasikan drift detector** — alat untuk mendeteksi ketika distribusi data/performa model mulai bergeser dari kondisi saat dilatih
- **Implementasikan cara mengumpulkan data baru** untuk keperluan retraining di masa depan

---

## Ringkasan Cepat

| Sub-topik | Kata Kunci untuk Diingat |
|-----------|---------------------------|
| 4.1 | limitations, intended use, dokumentasi, ekspektasi |
| 4.2 | jenis tantangan, indikator, mitigasi |
| 4.3 | pipeline produksi ≠ eksperimen, uji akurasi/robustness/speed/skala |
| 4.4 | dokumentasi maintenance, tim support, drift detector, data baru |

## Perbedaan Kunci: Eksperimen vs Produksi

| Aspek | Fase Eksperimen | Fase Produksi |
|-------|------------------|----------------|
| Data | Statis, sudah dibersihkan | Dinamis, real-time, bisa "kotor" |
| Fokus utama | Akurasi model | Akurasi + kecepatan + skalabilitas + keandalan |
| Perubahan | Jarang | Perlu monitoring & retraining berkelanjutan |
| Risiko | Rendah (belum dipakai user) | Tinggi (berdampak langsung ke pengguna nyata) |
