# 🚀 Marketing AI Agent (DeepSeek + Corey Haines Skills)

Repositori ini berisi AI Agent khusus pemasaran yang menggunakan **DeepSeek API** sebagai otak penalaran dan framework **[Marketing Skills](https://github.com/coreyhaines31/marketingskills)** dari Corey Haines sebagai instruksi sistemnya.

Dengan alat ini, Anda bisa memiliki asisten ahli di berbagai bidang mulai dari *Copywriting*, *SEO*, hingga *Pricing Strategy* dalam satu antarmuka chat yang simpel.

---

## 🛠️ Fitur Utama
* **35+ Marketing Skills:** Terintegrasi otomatis dengan instruksi profesional (Framework PAS, AIDA, SEO Audit, dll).
* **DeepSeek Integration:** Menggunakan model `deepseek-chat` yang cerdas dan ekonomis.
* **Streamlit UI:** Antarmuka chat yang modern, responsif, dan ringan.
* **Streaming Response:** Jawaban muncul secara real-time layaknya ChatGPT.
* **Persistent Memory:** AI mengingat konteks percakapan dalam satu sesi chat.

---

## 📋 Prasyarat
* Python 3.8 atau versi lebih baru.
* DeepSeek API Key (Dapatkan di [platform.deepseek.com](https://platform.deepseek.com)).
* PM2 (Opsional, untuk penggunaan di VPS/Production).

---

## 🚀 Panduan Instalasi

### 1. Klon Repositori
```bash
git clone https://github.com/username-anda/marketing-ai-chatbot.git
cd marketing-ai-chatbot
```

### 2. Buat & Aktifkan Virtual Environment
Sangat disarankan untuk menjaga kebersihan library sistem Anda.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instal Dependensi
```bash
pip install -r requirements.txt
```

### 4. Uji Coba Lokal
Jalankan aplikasi untuk memastikan semuanya bekerja dengan baik:
```bash
streamlit run main_1.py
```
* Buka browser di: `http://localhost:8501`
* Masukkan API Key Anda di sidebar.
* Selamat berdiskusi dengan asisten marketing Anda!

---

## ⚙️ Deployment (Production)

Untuk menjalankan aplikasi secara terus-menerus di background (seperti pada VPS Debian/Ubuntu), gunakan **PM2**:

1. Matikan venv jika masih aktif:
   ```bash
   deactivate
   ```
2. Jalankan dengan PM2:
   ```bash
   pm2 start "streamlit run main_1.py --server.port 8501" --name marketing-ai
   ```
3. Cek status: `pm2 status`

---

## 📂 Struktur Folder
* `main_1.py`: File utama aplikasi (Streamlit UI & Logic).
* `requirements.txt`: Daftar library Python yang dibutuhkan.
* `README.md`: Dokumentasi proyek (file ini).

---

## 🤝 Kontribusi
Instruksi pemasaran ditarik secara dinamis dari repositori [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills). Jika Anda ingin menambahkan framework marketing baru, Anda bisa berkontribusi langsung ke repositori sumber tersebut.

---

## 📜 Lisensi
Proyek ini bersifat open-source. Pastikan untuk mematuhi ketentuan penggunaan API dari DeepSeek.

---
*Dibuat dengan ❤️ untuk para pengembang dan pemasar.*
