# 🧭 Ödev 1 - Rastgele Noktalar Üzerinde Temel TSP (Nearest Neighbor)

**Yazar:** Eren Coşkun  
**Tarih:** 20.10.2025  

---

## 📘 Proje Açıklaması
Bu proje, **Gezgin Satıcı Problemi (Traveling Salesman Problem - TSP)** için basit bir sezgisel çözüm yaklaşımı uygular.  
Kullanılan yöntem **Nearest Neighbor (En Yakın Komşu)** algoritmasıdır.  
Amaç, rastgele üretilmiş noktalar arasında her noktayı **yalnızca bir kez ziyaret ederek** başladığı noktaya **en kısa mesafe** ile geri dönen bir rota bulmaktır.

Bu ödev **Symmetric TSP (STSP)** türündedir.  
Yani A → B ve B → A arasındaki mesafe aynıdır.

---

## ⚙️ Uygulama Adımları

### 1️⃣ Nokta Üretimi
- `generate_random_points()` fonksiyonu ile 0–100 arası koordinatlarda **20 rastgele nokta** oluşturulur.  
- `random.seed(22)` sabiti sayesinde **her çalıştırmada aynı sonuçlar** alınır (tekrarlanabilirlik).

### 2️⃣ Graf Oluşturma
- **NetworkX** kütüphanesi ile her nokta bir düğüm olarak eklenir.  
- Tüm düğümler arasındaki **Öklid mesafesi** hesaplanarak `weight` (kenar ağırlığı) olarak graf yapısına eklenir.

### 3️⃣ Nearest Neighbor Algoritması
- `nearest_neighbor_tsp()` fonksiyonu başlangıç olarak 0 numaralı noktayı alır.  
- Her adımda, mevcut konumdan **en yakın ziyaret edilmemiş noktaya** gider.  
- Ziyaret edilen her kenarın uzaklığı `total_distance` değişkenine eklenir.  
- Tüm noktalar ziyaret edildikten sonra başlangıç noktasına geri dönülür.  
- Çıktı olarak:
  - **Tur sırası** (ziyaret edilen noktaların sırası)
  - **Toplam mesafe** (geçilen tüm yolların toplam uzunluğu) döndürülür.

### 4️⃣ Görselleştirme
- `plot_tour()` fonksiyonu ile rota matplotlib üzerinde çizilir.  
- Başlangıç noktası **yeşil**, bitiş noktası **kırmızı**, diğerleri **gri** olarak gösterilir.  
- Oklar **tur yönünü**, sayılar ise **ziyaret sırasını** belirtir.  
- Görsel `tsp_result_final_v2.png` dosyasına kaydedilir.


