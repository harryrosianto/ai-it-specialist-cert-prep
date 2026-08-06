# Lab 1 (Domain 1): Worksheet Analisis Masalah AI

Domain 1 (AI Problem Definition) bukan soal coding — ini soal **pengambilan keputusan**. Cara paling hands-on melatihnya adalah dengan benar-benar **menulis jawaban** untuk skenario nyata, bukan sekadar membaca teori.

## Skenario yang Harus Kamu Analisis

> Kampusmu (FT UI / mitra kampus lain) ingin membangun sistem AI untuk **memprediksi mahasiswa yang berisiko drop out atau telat lulus**, berdasarkan data akademik (IPK per semester, kehadiran, jumlah SKS diulang) dan data non-akademik (status kerja paruh waktu, jarak tempat tinggal ke kampus).

Isi worksheet di bawah ini **dengan tulisan sendiri** (bukan definisi generik dari buku). Kalau kamu ragu suatu jawaban benar, cek pembahasan singkat di bagian akhir file ini.

---

### 1.1 — Identifikasi Masalah

- Kebutuhan apa yang ingin diatasi?
  `> jawabanmu di sini`
- Apa saja input yang tersedia, dan output apa yang diharapkan?
  `> jawabanmu di sini`
- Apakah AI **benar-benar diperlukan** di sini, atau cukup dengan aturan sederhana (mis. "IPK < 2.0 selama 2 semester berturut-turut = flag")? Jelaskan alasanmu.
  `> jawabanmu di sini`
- Tuliskan satu **ukuran keberhasilan yang terukur** (measurable success) untuk proyek ini.
  `> jawabanmu di sini`

### 1.2 — Klasifikasi Masalah

- Apakah data yang tersedia **berlabel**? Kalau ya, label seperti apa?
  `> jawabanmu di sini`
- Menurutmu ini termasuk classification, regression, unsupervised, atau reinforcement? Kenapa?
  `> jawabanmu di sini`

### 1.3 — Keahlian yang Dibutuhkan

Sebutkan satu contoh konkret (nama peran, bukan cuma kategori) untuk masing-masing:

- Business expertise: `> ...`
- Domain expertise: `> ...`
- AI expertise: `> ...`
- Implementation expertise: `> ...`

### 1.4 — Rencana Keamanan

- Siapa saja yang seharusnya **punya akses** untuk melihat skor risiko drop-out seorang mahasiswa? Siapa yang **tidak boleh**?
  `> jawabanmu di sini`
- Apa risiko terburuk kalau data ini bocor atau disalahgunakan?
  `> jawabanmu di sini`

### 1.5 — Penggunaan yang Tepat

- Kelompok mahasiswa mana yang **berisiko paling besar dirugikan** kalau model ini salah prediksi (false positive/false negative)? Kenapa?
  `> jawabanmu di sini`
- Bagaimana kalau hasil skor ini "bocor" dan digunakan dosen PA untuk menilai mahasiswa secara subjektif, bukan sekadar early-warning? Bagaimana kamu mencegah ini (out-of-context use)?
  `> jawabanmu di sini`

### 1.6 — Transparansi

- Siapa yang harus tahu bahwa data mereka digunakan untuk model ini?
  `> jawabanmu di sini`
- Regulasi apa yang mungkin relevan (mis. terkait data pribadi mahasiswa)?
  `> jawabanmu di sini`

---

## Setelah Selesai: Bandingkan dengan Pembahasan

<details>
<summary>Klik untuk melihat poin-poin pembahasan (bukan "jawaban tunggal" — ini panduan cek diri)</summary>

- **1.1**: Kebutuhan = deteksi dini agar bisa intervensi sebelum mahasiswa benar-benar DO. AI masuk akal di sini **kalau** hubungan antar faktor risiko cukup kompleks/non-linear (kombinasi banyak variabel) — kalau cuma 1-2 variabel dengan pola jelas, aturan sederhana mungkin sudah cukup dan lebih transparan. Ukuran keberhasilan yang baik: mis. "meningkatkan tingkat intervensi dini pada mahasiswa berisiko sebesar X%, diukur lewat penurunan jumlah DO aktual di semester berikutnya" — bukan sekadar "akurasi model tinggi".
- **1.2**: Kalau ada histori mahasiswa yang benar-benar DO/lulus terlambat di masa lalu, ini data **berlabel** → **classification** (DO/tidak DO) atau **regression** (prediksi lama waktu kelulusan).
- **1.3**: Business = Wakil Dekan Akademik; Domain = Dosen Pembimbing Akademik/Konselor; AI = Data Scientist; Implementation = Software Engineer sistem akademik kampus (SIAK/SIAKAD).
- **1.4**: Akses idealnya terbatas pada dosen PA mahasiswa bersangkutan + tim BK, bukan seluruh dosen atau mahasiswa lain. Risiko terburuk: stigma terhadap mahasiswa yang di-flag, atau digunakan secara punitif alih-alih suportif.
- **1.5**: Mahasiswa dari latar belakang yang kurang terwakili dalam data historis (mis. mahasiswa kerja paruh waktu, mahasiswa daerah) berisiko paling besar kena bias model. Mitigasi out-of-context use: buat kebijakan tegas bahwa skor ini **hanya untuk early-warning/dukungan**, bukan untuk evaluasi kinerja akademik formal atau syarat administratif apa pun.
- **1.6**: Mahasiswa berhak tahu datanya dipakai (transparansi), idealnya lewat kebijakan privasi kampus. Relevan dengan UU PDP (Perlindungan Data Pribadi) di Indonesia karena melibatkan data pribadi mahasiswa.

</details>
