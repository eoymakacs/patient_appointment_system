# Django REST API – Appointment Scheduling System

Bu proje, basit fakat gerçekçi bir **Randevu Yönetim Sistemi (Appointment Scheduling API)** örneğidir. Proje Django + Django REST Framework kullanılarak inşa edilmiştir ve temel CRUD işlemleri ile randevu çakışma kontrolü içerir.

---

## 🛠 Özellikler
- Patients, Providers, Appointments için CRUD API
- Provider randevularında çakışma kontrolü
- Django REST Framework ile hızlı API geliştirme
- SQLite destekli basit ve hafif veritabanı
- DRF'de ViewSet + Router kullanımı
- JSON tabanlı request/response
- Genişletilebilir uygulama mimarisi

## 📂 Proje Yapisi
```plaintext
 patient_appointment_system/          <- Proje root (ana klasör)
│
├── db.sqlite3               <- SQLite veritabanı (otomatik oluşturulur)
├── manage.py                <- Django yönetim komutu (server çalıştırma, migrate vb.)
├── requirements.txt         <- Kullanılan Python paketleri listesi (opsiyonel ama iyi)
│
├── patient_appointment_system/       <- Ana proje klasörü (settings, global urls, wsgi/asgi)
│   ├── __init__.py          <- Python package olduğunu belirtir
│   ├── settings.py          <- Tüm proje ayarları (DB, apps, middleware, static, template vb.)
│   ├── urls.py              <- Proje genel URL yönlendirmeleri
│   ├── asgi.py              <- Asynchronous Server Gateway Interface (opsiyonel)
│   └── wsgi.py              <- WSGI server için giriş noktası (prod ortamı)
│
└── appointments/            <- Django App klasörü (bizim CRUD / API logic)
    ├── __init__.py          <- Python package olduğunu belirtir
    ├── admin.py             <- Admin panelde modellerin görünmesini sağlar
    ├── apps.py              <- App config bilgileri
    ├── models.py            <- DB tabloları (ORM) burada tanımlanır
    ├── serializers.py       <- Model verilerini JSON’a çeviren serializerlar
    ├── views.py             <- API / business logic / ViewSetler burada
    ├── urls.py              <- App’e özel URL routing (API endpointleri)
    ├── tests.py             <- Basit test case’leri (opsiyonel ama önerilir)
    └── migrations/          <- Model değişiklikleri için migration dosyaları
        ├── __init__.py
        └── 0001_initial.py (ilk migration)

```
Her app — modeller, view’ler, serializer’lar ve URL yönlendirmeleri gibi kendi logic’ini içerir. Django’nun modüler mimarisine uygundur.

---

## 🚀 Kurulum

**1.** Repoyu Klonla
```bash
git clone https://github.com/.../patient_appointment_system.git
cd patient_appointment_system
```

**2.** Sanal Ortam
```bash
python3 -m venv venv
source venv/bin/activate
```

**3.** Gerekli paketleri yükle
```bash
pip install -r requirements.txt
```

**4.** Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

**5.** Veritabanı Ayarları
 ## Varsayılan DB: SQLite (hazır geliyor)
 Ekstra kurulum gerektirmez.

 ## PostgreSQL kullanmak istersen
 - requirements.txt’ye ekle:
   ```bash
   psycopg2-binary
   ```
 - settings.py → DATABASES bölümünü değiştir:
  ```python 
   DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "appointments",
        "USER": "postgres",
        "PASSWORD": "yourpassword",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

 ## Migration Çalıştır
 
 ```bash
 python manage.py makemigrations
 python manage.py migrate
 ```

**6**. (Opsiyonel) Admin Kullanıcısı
```bash
python manage.py createsuperuser
```

**7**. Server’ı Başlat
```bash
python manage.py runserver
```

---

## 📡 API Endpoint’leri
Tüm API’ler /api/ prefix’i ile yayınlanır.

# 👤 Patients

| Method    | Endpoint              | Açıklama   |
| --------- | --------------------- | ---------- |
| GET       | `/api/patients/`      | Liste      |
| POST      | `/api/patients/`      | Yeni hasta |
| GET       | `/api/patients/<id>/` | Detay      |
| PUT/PATCH | `/api/patients/<id>/` | Güncelle   |
| DELETE    | `/api/patients/<id>/` | Sil        |

# 🩺 Providers
```bash
/api/providers/
```

Aynı CRUD yapısı provider’lar için geçerlidir.

# 📅 Appointments

| Method    | Endpoint                  | Açıklama     |
| --------- | ------------------------- | ------------ |
| GET       | `/api/appointments/`      | Liste        |
| POST      | `/api/appointments/`      | Yeni randevu |
| GET       | `/api/appointments/<id>/` | Detay        |
| PUT/PATCH | `/api/appointments/<id>/` | Güncelle     |
| DELETE    | `/api/appointments/<id>/` | Sil          |

# ✔ Çakışma Kontrolü

Randevu POST ederken:

- Provider’ın aynı aralıkta başka randevusu varsa → 400 Bad Request

---

## 🗄 Veri Modelleri

# Patient
```bash
first_name: string
last_name: string
birth_date: date
email: string
```

# Provider
```bash
first_name: string
last_name: string
speciality: string
```

# Appointment
```bash
patient: ForeignKey
provider: ForeignKey
start_time: DateTime
end_time: DateTime
```

---

## 🧪 Testler

Test çalıştırmak için:
```bash
python manage.py test
```

---

## 🔧 Teknolojiler

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite
- Python Virtual Environment

---

## 📌 Notlar

```bash 
.gitignore
```

```bash __pycache__ ``` klasörlerini ignore etmek için:

```bash
__pycache__/
**/__pycache__/
```
