import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca dataset dari 'all_data.csv'
all_data_df = pd.read_csv("https://raw.githubusercontent.com/DESTYAWANSATRIA/Proyek-Analisis-Data/refs/heads/main/dashboard/all_data.csv")

# Menghitung rata-rata jumlah peminjam berdasarkan temperatur
avg_hourly_borrowers_by_temp = all_data_df.groupby('temp')['cnt'].mean().reset_index()

st.markdown("""
    <style>
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #4A90E2;  /* Warna biru menarik */
        position: relative;
    }
    .title:before, .title:after {
        content: '★';  /* Menambahkan bintang sebelum dan setelah teks */
        font-size: 36px;
        color: gold;
        position: absolute;
    }
    .title:before {
        left: -50px;  /* Mengatur posisi bintang sebelah kiri */
    }
    .title:after {
        right: -50px;  /* Mengatur posisi bintang sebelah kanan */
    }
    </style>
    <h1 class="title">Analisis Peminjaman Sepeda</h1>
    """, unsafe_allow_html=True)

# Scatter plot untuk jumlah peminjam berdasarkan temperatur
st.subheader('\nRata-rata Jumlah Peminjam Berdasarkan Temperatur (Hourly Data)')
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.scatter(avg_hourly_borrowers_by_temp['temp'], avg_hourly_borrowers_by_temp['cnt'], color='blue', alpha=0.7)
ax1.set_title('Average Bike Rentals based on Temperature (Hour)', fontsize=14)
ax1.set_xlabel('Temperature (temp)', fontsize=12)
ax1.set_ylabel('Average Rentals (cnt)', fontsize=12)
ax1.grid(True)
st.pyplot(fig1)

# Menghitung jumlah peminjam per bulan di tahun 2011 dan 2012
all_data_df['dteday'] = all_data_df['dteday'].astype(str)
all_data_df['year'] = all_data_df['dteday'].str[:4]
all_data_df['month'] = all_data_df['dteday'].str[5:7]
monthly_borrowers = all_data_df.groupby(['year', 'month'])['cnt'].sum().reset_index()

# Bar plot untuk jumlah peminjam per bulan di tahun 2011 dan 2012
st.subheader('Jumlah Peminjam Tiap Bulan (2011 & 2012)')
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.barplot(data=monthly_borrowers, x='month', y='cnt', hue='year', palette='viridis', ax=ax2)
ax2.set_title('Jumlah Peminjam Tiap Bulan pada Tahun 2011 dan 2012')
ax2.set_xlabel('Bulan')
ax2.set_ylabel('Jumlah Peminjam')
ax2.set_xticks(range(12))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
ax2.legend(title='Tahun')
ax2.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig2)

# Menghitung jumlah peminjam berdasarkan season
avg_hourly_borrowers_by_season = all_data_df.groupby('season')['cnt'].sum().reset_index()

# Mendapatkan jumlah peminjam untuk setiap musim
winter_borrowers = avg_hourly_borrowers_by_season.loc[avg_hourly_borrowers_by_season['season'] == 1, 'cnt'].values[0]
spring_borrowers = avg_hourly_borrowers_by_season.loc[avg_hourly_borrowers_by_season['season'] == 2, 'cnt'].values[0]
summer_borrowers = avg_hourly_borrowers_by_season.loc[avg_hourly_borrowers_by_season['season'] == 3, 'cnt'].values[0]
fall_borrowers = avg_hourly_borrowers_by_season.loc[avg_hourly_borrowers_by_season['season'] == 4, 'cnt'].values[0]

# Bar plot untuk jumlah peminjam per season
st.subheader('Jumlah Peminjam Berdasarkan Season')
fig3, ax3 = plt.subplots(figsize=(6, 5))
ax3.bar(avg_hourly_borrowers_by_season['season'], avg_hourly_borrowers_by_season['cnt'], 
        color=["#D3D3D3", "#D3D3D3", "#87CEFA", "#D3D3D3"])
ax3.set_xticks([1, 2, 3, 4])
ax3.set_xticklabels(['Winter', 'Spring', 'Summer', 'Fall'])
ax3.set_xlabel('Season', fontsize=12)
ax3.set_ylabel('Total Peminjam', fontsize=12)
ax3.set_title('Jumlah Peminjam Berdasarkan Season', fontsize=14)
st.pyplot(fig3)

# Menampilkan jumlah peminjam berdasarkan season
st.markdown(f"""
**Jumlah Peminjam per Musim:**
- **Winter**: {winter_borrowers}
- **Spring**: {spring_borrowers}
- **Summer**: {summer_borrowers}
- **Fall**: {fall_borrowers}
""")

#Rata-rata jumlah peminjam berdasarkan cuaca
avg_borrowers_by_weather = all_data_df.groupby('weathersit')['cnt'].mean().reset_index()

st.subheader('Rata-rata Jumlah Peminjam Berdasarkan Cuaca')
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(data=avg_borrowers_by_weather, x='weathersit', y='cnt', palette='Blues', ax=ax4)
ax4.set_title('Rata-rata Peminjam Berdasarkan Cuaca', fontsize=14)
ax4.set_xlabel('Kondisi Cuaca (1: Cerah, 2: Mendung, 3: Hujan)', fontsize=12)
ax4.set_ylabel('Rata-rata Peminjam', fontsize=12)
st.pyplot(fig4)

# Jumlah peminjam berdasarkan jenis hari
avg_borrowers_by_daytype = all_data_df.groupby('workingday')['cnt'].mean().reset_index()

st.subheader('Rata-rata Jumlah Peminjam Berdasarkan Jenis Hari')
fig5, ax5 = plt.subplots(figsize=(8, 5))
sns.barplot(data=avg_borrowers_by_daytype, x='workingday', y='cnt', palette='Set1', ax=ax5)
ax5.set_title('Rata-rata Peminjam Berdasarkan Jenis Hari', fontsize=14)
ax5.set_xlabel('Hari Kerja (0: Libur, 1: Kerja)', fontsize=12)
ax5.set_ylabel('Rata-rata Peminjam', fontsize=12)
st.pyplot(fig5)

# Distribusi jumlah peminjam per jam
hourly_borrowers = all_data_df.groupby('hr')['cnt'].sum().reset_index()

st.subheader('Distribusi Jumlah Peminjam per Jam')
fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hourly_borrowers, x='hr', y='cnt', marker='o', ax=ax6, color='purple')
ax6.set_title('Distribusi Jumlah Peminjam per Jam', fontsize=14)
ax6.set_xlabel('Jam', fontsize=12)
ax6.set_ylabel('Jumlah Peminjam', fontsize=12)
st.pyplot(fig6)

#Persentase perubahan peminjam per bulan
monthly_borrowers['change'] = monthly_borrowers['cnt'].pct_change() * 100

st.subheader('Persentase Perubahan Peminjam per Bulan')
fig7, ax7 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=monthly_borrowers, x='month', y='change', marker='o', hue='year', ax=ax7, palette='dark')
ax7.set_title('Persentase Perubahan Peminjam per Bulan', fontsize=14)
ax7.set_xlabel('Bulan', fontsize=12)
ax7.set_ylabel('Persentase Perubahan (%)', fontsize=12)
ax7.set_xticks(range(12))
ax7.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
st.pyplot(fig7)

st.caption('Copyright © Destyawan 2024')
