# GeziYorum · Orta Avrupa Cep Rehberi

16–20 Kasım 2026 Orta Avrupa gezisi için telefonda çalışan, çevrimdışı açılan cep rehberi.

- Adres: https://recepgulcanai.github.io/GeziYorum/
- Uygulama şifreyle korumalıdır: içerik `gezi.enc` dosyasında şifreli durur (AES-256-GCM).
- Telefonda bir kez internetle açıp şifreyi girin, "Ana ekrana ekle" ile kaydedin; sonra internetsiz de açılır.
- Düzenleme için: `GEZI_SIFRE=… python3 build.py dec gezi.enc paket.html` (çöz), değiştir, `enc` ile yeniden şifrele.

Harita verisi © OpenStreetMap katkıda bulunanlar.
