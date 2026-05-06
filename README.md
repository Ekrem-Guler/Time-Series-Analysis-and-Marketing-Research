**E-Ticaret Veri Bilimi Projesi: Segmentasyon ve Satış Tahmini**

Bu proje, bir e-ticaret işletmesinin geçmiş verilerini kullanarak Müşteri Segmentasyonu (RFM) ve Gelecek Dönem Satış Tahmini süreçlerini uçtan uca otomatize eden bir dashboard uygulamasıdır.

**Proje Hakkında**

Bu çalışma kapsamında, müşteri bağlılığını ölçümlemek ve işletmenin finansal geleceğini öngörmek amacıyla veri madenciliği ve zaman serisi analizleri uygulanmıştır.

**Ana Özellikler**:

RFM Analizi: Müşteriler; Yenilik (Recency), Sıklık (Frequency) ve Parasal Değer (Monetary) metriklerine göre analiz edilmiştir.

K-Means Kümeleme: Müşteri tabanı, makine öğrenmesi algoritmaları kullanılarak 3 ana segmente ayrılmış ve 3D olarak görselleştirilmiştir.

Prophet ile Satış Tahmini: Geçmiş satış trendleri analiz edilerek gelecek 4 haftalık ciro öngörüsü oluşturulmuştur.

İnteraktif Dashboard: Tüm analizler Streamlit kullanılarak kullanıcı dostu bir arayüzde sunulmuştur.

**Kullanılan Teknolojiler**

Programlama: Python

Veri Analizi: Pandas, NumPy

Makine Öğrenmesi: K-Means, Facebook Prophet

Görselleştirme: Plotly, Matplotlib,Seaborn

Web Framework: Streamlit

Projede kullanılan veri seti, İngiltere merkezli bir perakende mağazasının 2010-2011 yıllarına ait işlemlerini içermektedir.

Veri seti yaklaşık 305 günlük bir süreci kapsamaktadır.

Eksik değerler ve aykırı değerler (outliers) IQR yöntemiyle temizlenmiştir.

Negatif değerler (iade işlemleri) analiz dışı bırakılmıştır.

**Model Performansı**

Müşteri Segmentasyonu: K-Means modeli için Elbow yöntemi kullanılarak optimum küme sayısı (k=3) belirlenmiştir.

Tahminleme: Günlük verideki yüksek varyans nedeniyle model haftalık (weekly) olarak güncellenmiş; bu sayede gürültü azaltılarak daha tutarlı trendler elde edilmiştir. (Ortalama Hata Payı: %23).

<img width="906" height="830" alt="image" src="https://github.com/user-attachments/assets/cfa19482-695a-41a8-afca-7fe095b852b5" />

<img width="1716" height="565" alt="image" src="https://github.com/user-attachments/assets/85194f2b-d1c7-4a32-b7b5-6ae32451eefc" />

<img width="1749" height="343" alt="image" src="https://github.com/user-attachments/assets/cb79eeb6-2047-4ec9-8b20-a8361e8d5684" />


👤 İletişim
Ekrem Güler

E-posta: Ekrem Güler
