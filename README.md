# Django REST API – Appointment Scheduling System

Bu proje, basit fakat gerçekçi bir **Randevu Yönetim Sistemi (Appointment Scheduling API)** örneğidir. Proje Django + Django REST Framework kullanılarak inşa edilmiştir ve temel CRUD işlemleri ile randevu çakışma kontrolü içerir.

---

## 🛠 Özellikler

✔ Patients, Providers, Appointments için CRUD API
✔ Provider randevularında çakışma kontrolü
✔ Django REST Framework ile hızlı API geliştirme
✔ SQLite destekli basit ve hafif veritabanı
✔ DRF'de ViewSet + Router kullanımı
✔ JSON tabanlı request/response
✔ Genişletilebilir uygulama mimarisi

## 📂 Proje Yapisi
```plaintext
patient_appointment_system/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── patient_appointment_system/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── appointments/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── urls.py
    ├── admin.py
    ├── tests.py
    └── migrations/
```
Her app — modeller, view’ler, serializer’lar ve URL yönlendirmeleri gibi kendi logic’ini içerir. Django’nun modüler mimarisine uygundur.

---

## 🚀 Kurulum

1. Repoyu Klonla
```bash
git clone https://github.com/.../patient_appointment_system.git
cd patient_appointment_system
```

2. Sanal Ortam
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

4. Veritabanını Oluştur
```bash
python manage.py makemigrations
python manage.py migrate
```

5. (Opsiyonel) Admin Kullanıcısı
```bash
python manage.py createsuperuser
```

6. Server’ı Başlat
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

Python 3.10+
Django 4.x
Django REST Framework
SQLite
Python Virtual Environment

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
