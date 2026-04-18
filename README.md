# 📦 Smart Inventory System

![CI](https://github.com/Devinhernando/https://github.com/Devinhernando/Smart-Inventory-System/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.14.3-blue)
![Flask](https://img.shields.io/badge/flask-3.1.0-lightgrey)


---

## 📋 Deskripsi Aplikasi

Smart Inventory System adalah aplikasi web sederhana untuk mengelola stok barang. Pengguna dapat menambahkan barang baru, melihat daftar barang, memperbarui stok, dan menghapus barang — semuanya melalui antarmuka web atau REST API.

**Fitur Utama:**
- ➕ Tambah item baru (nama, stok, harga)
- 📋 Lihat seluruh daftar item
- ✏️ Perbarui jumlah stok item
- 🗑️ Hapus item dari inventori
- ✅ Validasi input (nama wajib, stok ≥ 0, harga > 0)

---

## 🗂️ Struktur Repository

```
smart-inventory/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI pipeline
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── style.css           # Stylesheet
├── app.py                  # Flask routes (API layer)
├── service.py              # Business logic layer
├── test_app.py             # Unit & integration tests
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 Cara Menjalankan Aplikasi

### Prasyarat
- Python 3.11+
- pip

### Langkah Instalasi

```bash
# 1. Clone repository
git clone https://github.com/USERNAME/REPO.git
cd REPO

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan aplikasi
python app.py
```

Aplikasi akan berjalan di `http://127.0.0.1:5000`

---

## 🧪 Cara Menjalankan Test

```bash
# Jalankan seluruh test
pytest test_app.py -v

# Jalankan test dengan laporan coverage
pytest test_app.py -v --cov=app --cov=service --cov-report=term-missing

# Jalankan test dengan target coverage 100%
pytest test_app.py -v --cov=app --cov=service --cov-fail-under=100
```

### Contoh Output Test

```
test_app.py::TestCreateItem::test_create_success          PASSED
test_app.py::TestCreateItem::test_create_no_name          PASSED
test_app.py::TestCreateItem::test_create_negative_stock   PASSED
...
========================= 35 passed in 0.42s =========================
```

---

## 🛡️ Strategi Pengujian

Pengujian dibagi menjadi dua lapisan:

### 1. Unit Testing (24 test case)
Menguji **service layer** (`service.py`) secara terisolasi, tanpa melibatkan HTTP atau framework Flask.

| Kelompok              | Jumlah Test | Yang Diuji                                      |
|-----------------------|-------------|--------------------------------------------------|
| `TestCreateItem`      | 9           | Validasi nama, stok, harga; auto-increment ID   |
| `TestGetItems`        | 2           | List kosong, list setelah insert                |
| `TestUpdateItem`      | 4           | Update sukses, not found, stok negatif, nol     |
| `TestDeleteItem`      | 4           | Hapus sukses, tidak ditemukan, item yang tepat  |

### 2. Integration Testing (11 test case)
Menguji **endpoint API** (`app.py`) melalui Flask test client, memverifikasi interaksi antara route, service, dan respons HTTP.

| Kelompok                  | Jumlah Test | Endpoint               |
|---------------------------|-------------|------------------------|
| `TestHomeEndpoint`        | 1           | `GET /`               |
| `TestCreateEndpoint`      | 4           | `POST /api/items`     |
| `TestGetEndpoint`         | 2           | `GET /api/items`      |
| `TestUpdateEndpoint`      | 3           | `PUT /api/items/<id>` |
| `TestDeleteEndpoint`      | 3           | `DELETE /api/items/<id>` |

**Total: 35 test case** dengan target **100% code coverage**.

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

Pipeline dijalankan otomatis pada setiap **push** dan **pull request** ke semua branch.

```
Push / Pull Request
        │
        ▼
┌─────────────────────┐
│  Checkout Code       │
├─────────────────────┤
│  Setup Python 3.11   │
├─────────────────────┤
│  Install Dependencies│  pip install -r requirements.txt
├─────────────────────┤
│  Run Tests           │  pytest --cov --cov-fail-under=100
├─────────────────────┤
│  Upload Coverage     │  coverage.xml → Artifacts
└─────────────────────┘
```

Jika coverage < 100% atau ada test yang gagal, pipeline akan **gagal (fail)** dan tidak ada merge yang diizinkan.

---

## 📡 API Reference

| Method | Endpoint            | Deskripsi               | Body                                    |
|--------|---------------------|-------------------------|-----------------------------------------|
| GET    | `/`                 | Halaman utama           | —                                       |
| GET    | `/api/items`        | Ambil semua item        | —                                       |
| POST   | `/api/items`        | Tambah item baru        | `{"name":"...", "stock":0, "price":0}` |
| PUT    | `/api/items/<id>`   | Update stok item        | `{"stock": 20}`                         |
| DELETE | `/api/items/<id>`   | Hapus item              | —                                       |
