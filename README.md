# SIEMLite

🚨 **SIEMLite**: Küçük/orta ölçekli sistemler için geliştirilen, sade ve hızlı kurulumla çalışan bir mini SIEM (Security Information and Event Management) platformudur.

---

## 📌 Ne İşe Yarar?

SIEMLite, sistemlerde gerçekleşen güvenlik olaylarını merkezi bir şekilde toplayıp görselleştirerek:
- Anlık log takibi sağlar.
- Şüpheli aktiviteleri analiz etmenize yardımcı olur.
- Kaynak IP, olay tipi, önem derecesine göre log sorgulama ve filtreleme sunar.
- Basit uyarı ve alarm kuralları ile operasyonel güvenliğe katkı sağlar.

---

## 🎯 Nerelerde Kullanılır?

- 🧪 **Siber güvenlik eğitimi ve lab ortamları**
- 🏢 **Küçük-orta ölçekli işletmeler**
- 🖥️ **Freelancer SOC analistleri**
- 🧑‍💻 **Güvenlik araştırmacıları ve test ortamları**
- 🛡️ **MSSP hizmeti sunan ekiplerin hızlı konuşlandırılabilir aracı**

---

## 🚀 Özellikler

- ✅ FastAPI tabanlı RESTful API
- ✅ React frontend ile gerçek zamanlı log takibi
- ✅ IP, olay türü, öncelik seviyesiyle filtreleme
- ✅ Docker ile kolay kurulum (tek komutla)
- ✅ In-memory log verisi (test için ideal)
- ✅ Basit kurulum, sade arayüz, sıfır karmaşa

---

## 🧠 Avantajları

- 🔧 **Kurulum kolaylığı**: Tek komutla ayağa kalkar
- 💡 **Öğrenme dostu**: SIEM mimarisini anlamak için birebir
- 📦 **Taşınabilir**: Docker ile her yerde çalışır
- 👀 **Şeffaflık**: Açık kaynak, şeffaf yapı, kolay katkı
- 💬 **Özelleştirilebilir**: Kurallar, sorgular, UI geliştirilebilir

---

## 📁 Proje Yapısı

```
siemlite/
├── backend/
│   ├── app.py            # FastAPI sunucusu
│   └── requirements.txt  # Backend bağımlılıkları
├── frontend/
│   ├── public/index.html
│   ├── src/App.jsx
│   └── package.json
├── docker-compose.yml    # Her iki servisi ayağa kaldırır
└── README.md
```

---

## ⚙️ Kurulum ve Çalıştırma

1. Bu repoyu klonla:
```bash
git clone https://github.com/kullaniciadi/siemlite.git
cd siemlite
```

2. Docker ile ayağa kaldır:
```bash
docker-compose up --build
```

3. Tarayıcından uygulamaya eriş:
- Frontend: [http://localhost:3000](http://localhost:3000)
- API Dokümantasyonu: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔄 API Örnekleri

### 🔹 Log Ingest

```bash
curl -X POST http://localhost:8000/api/logs/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "timestamp": "2025-04-21T14:30:00",
    "source_ip": "192.168.1.10",
    "event_type": "login_failure",
    "severity": "warning",
    "message": "Geçersiz kullanıcı adı denemesi"
}'
```

### 🔹 Log Sorgulama

```bash
curl http://localhost:8000/api/logs?source_ip=192.168.1.10
```

---

## 📷 Görsel (Demo)

```
+---------------------+--------------+--------------+----------+-------------------------------+
| Zaman              | IP           | Olay Türü    | Öncelik | Mesaj                        |
+---------------------+--------------+--------------+----------+-------------------------------+
| 2025-04-21T14:30    | 192.168.1.10 | login_failure| warning | Geçersiz kullanıcı adı       |
+---------------------+--------------+--------------+----------+-------------------------------+
```

---

## 🛠️ Kullanılan Teknolojiler

- Python 3.11
- FastAPI
- React + Axios
- Docker / Docker Compose

---

## 📜 Lisans

MIT Lisansı ile sunulmuştur.

---

Made with ❤️ by [burakcanbalta](https://github.com/burakcanbalta)
