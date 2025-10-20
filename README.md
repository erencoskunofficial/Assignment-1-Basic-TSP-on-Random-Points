# 🧭 Ödev 1 - Rastgele Noktalar Üzerinde Temel TSP (Nearest Neighbor)

**Yazar:** Eren Coşkun  
**Tarih:** 20.10.2025  

---

## 📘 Proje Açıklaması
Bu proje, **Gezgin Satıcı Problemi (Traveling Salesman Problem - TSP)** için basit bir sezgisel çözüm yaklaşımı uygular.  
Kullanılan yöntem **Nearest Neighbor (En Yakın Komşu)** algoritmasıdır.  
Amaç, rastgele üretilmiş noktalar arasında her noktayı **yalnızca bir kez ziyaret ederek** başladığı noktaya **en kısa mesafe** ile geri dönen bir rota bulmaktır.

---

## ⚙️ Uygulama Adımları
1. **Rastgele Nokta Üretimi:**  
   20 adet rastgele (x, y) koordinatı oluşturuldu.  
   Sabit `seed=22` kullanılarak sonuçların tekrar üretilebilir olması sağlandı.
2. **Graf Yapısı:**  
   Noktalar, **NetworkX** kütüphanesiyle bir grafik üzerinde temsil edildi.  
   Kenar ağırlıkları, noktalar arasındaki **Öklid mesafesi (Euclidean distance)** ile hesaplandı.
3. **Sezgisel Algoritma (Heuristic):**  
   En Yakın Komşu algoritmasıyla her adımda mevcut konuma en yakın ziyaret edilmemiş nokta seçildi.  
   Tüm noktalar ziyaret edildikten sonra başlangıç noktasına dönülerek tur tamamlandı.
4. **Sonuç ve Görselleştirme:**  
   Tur sırası ve toplam mesafe ekrana yazdırıldı.  
   Matplotlib ile rota, yön okları ve ziyaret sırası numaraları görselleştirildi.
5. **Tekrar Üretilebilirlik:**  
   Rastgelelik kontrol altına alındı (`random.seed(22)`).

---


