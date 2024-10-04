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

# Menampilkan jumlah rata-rata peminjam berdasarkan temperatur
average_borrowers_count = avg_hourly_borrowers_by_temp['cnt'].mean()
st.markdown(f"**Jumlah Rata-rata Peminjam berdasarkan Temperatur**: {average_borrowers_count:.2f}")

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

# Menampilkan jumlah peminjam per bulan
monthly_total_borrowers = monthly_borrowers['cnt'].sum()
st.markdown(f"**Jumlah Total Peminjam per Bulan**: {monthly_total_borrowers}")

# Menghitung jumlah peminjam berdasarkan season
avg_hourly_borrowers_by_season = all_data_df.groupby('season')['cnt'].sum().reset_index()

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
season_total_borrowers = avg_hourly_borrowers_by_season['cnt'].sum()
st.markdown(f"**Jumlah Total Peminjam Berdasarkan Season**: {season_total_borrowers}")

# Visualisasi presentase jumlah peminjam registered dan casual
total_casual = all_data_df['casual'].sum()
total_registered = all_data_df['registered'].sum()

st.subheader('Presentase Jumlah Peminjam Registered dan Casual')
labels = ("Registered", "Casual")
votes = (total_registered, total_casual)
colors = ('#87CEFA', '#D3D3D3')
explode = (0.1, 0)

fig4, ax4 = plt.subplots()
ax4.pie(votes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode)
ax4.set_title('Presentase Peminjam Registered vs Casual')
st.pyplot(fig4)

# Menampilkan jumlah peminjam registered dan casual
st.markdown(f"**Jumlah Peminjam Registered**: {total_registered}")
st.markdown(f"**Jumlah Peminjam Casual**: {total_casual}")

st.caption('Copyright © Destyawan 2024')
