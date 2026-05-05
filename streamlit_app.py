import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Veri Bilimi Staj Projesi | E-Ticaret Analizi", layout="wide")

# CSS ile biraz makyaj (Opsiyonel ama şık durur)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)


# 2. VERİ YÜKLEME FONKSİYONLARI
@st.cache_data
def load_segment_data():
    return pd.read_csv("customer_segments.csv")


@st.cache_data
def load_forecast_data():
    df = pd.read_csv("sales_forecast.csv")
    df['ds'] = pd.to_datetime(df['ds'])
    return df


# Verileri yükle
try:
    df_rfm = load_segment_data()
    df_forecast = load_forecast_data()
except FileNotFoundError:
    st.error(
        "Lütfen 'customer_segments.csv' ve 'sales_forecast.csv' dosyalarının app.py ile aynı klasörde olduğundan emin olun.")
    st.stop()

# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=100)
st.sidebar.title("Proje Menüsü")
page = st.sidebar.selectbox("Bölüm Seçin:", ["Müşteri Segmentasyonu", "Satış Tahmini", "Proje Hakkında"])

# --- SAYFA 1: MÜŞTERİ SEGMENTASYONU ---
if page == "Müşteri Segmentasyonu":
    st.title("👥 K-Means ile Müşteri Segmentasyonu")

    # Üst Metrikler
    m1, m2, m3 = st.columns(3)
    m1.metric("Toplam Müşteri", len(df_rfm))
    m2.metric("Ortalama Monetary", f"{df_rfm['Monetary'].mean():,.2f}")
    m3.metric("Küme Sayısı (k)", df_rfm['Clusters'].nunique())

    st.divider()

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("3D Müşteri Dağılımı")
        # Clusters sütununu renk için kategoriye çevirelim
        df_rfm['Clusters'] = df_rfm['Clusters'].astype(str)
        fig_3d = px.scatter_3d(df_rfm, x='Recency', y='Frequency', z='Monetary',
                               color='Clusters',
                               color_discrete_sequence=px.colors.qualitative.Vivid,
                               opacity=0.7, height=600)
        st.plotly_chart(fig_3d, use_container_width=True)

    with col_right:
        st.subheader("Segment Özetleri")
        cluster_summary = df_rfm.groupby('Clusters')[['Recency', 'Frequency', 'Monetary']].mean().reset_index()
        st.dataframe(cluster_summary.style.format(precision=2), hide_index=True)
        st.info("💡 **Yorum:** Monetary değeri yüksek, Recency değeri düşük olan kümeler 'Şampiyon' müşterilerimizdir.")

# --- SAYFA 2: SATIŞ TAHMİNİ ---
elif page == "Satış Tahmini":
    st.title("📈 Gelecek Dönem Satış Öngörüsü")
    st.write("Prophet modeli kullanılarak haftalık ciro tahmini yapılmıştır.")

    # Tahmin Grafiği
    fig_forecast = go.Figure()

    # Üst ve alt bantlar (Güven aralığı)
    fig_forecast.add_trace(go.Scatter(
        x=df_forecast['ds'].tolist() + df_forecast['ds'].tolist()[::-1],
        y=df_forecast['yhat_upper'].tolist() + df_forecast['yhat_lower'].tolist()[::-1],
        fill='toself',
        fillcolor='rgba(0,176,246,0.2)',
        line_color='rgba(255,255,255,0)',
        name='Güven Aralığı',
    ))

    # Ana tahmin çizgisi
    fig_forecast.add_trace(go.Scatter(
        x=df_forecast['ds'], y=df_forecast['yhat'],
        line_color='rgb(0,176,246)',
        name='Tahmin (yhat)',
    ))

    fig_forecast.update_layout(title="Haftalık Ciro Tahmini", xaxis_title="Tarih", yaxis_title="Ciro (TL)")
    st.plotly_chart(fig_forecast, use_container_width=True)

    st.success("Modelimiz önümüzdeki 4 hafta için stabil bir trend öngörmektedir.")

# --- SAYFA 3: PROJE HAKKINDA ---
elif page == "Proje Hakkında":
    st.title("📄 Proje Detayları ve Metodoloji")
    st.markdown("""
    ### Kullanılan Teknolojiler
    * **Veri İşleme:** SQL, Pandas, NumPy
    * **Kümeleme:** Scikit-Learn (K-Means)
    * **Tahminleme:** Facebook Prophet
    * **Görselleştirme:** Plotly, Streamlit

    ### İş Problemi
    E-ticaret verilerini analiz ederek müşteri sadakatini ölçümlemek (RFM) ve gelecekteki nakit akışını tahmin etmek.

    **Geliştiren:** [Senin Adın Soyadın]
    """)