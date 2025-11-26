# Analysis Dashboard ✨

## Setup Environment - Anaconda
```
conda create --name proyek_analisis_data python=3.11
conda activate proyek_analisis_data
pip install -r submission/requirements.txt
```

## Setup Environment - Shell/Terminal
```
conda create --name proyek_analisis_data python=3.11
conda activate proyek_analisis_data
pip install -r submission/requirements.txt
```

## Run steamlit app
```
cd submission/dashboard
streamlit run Dashboard.py
```
# 🚴‍♂️ Bike Sharing Demand Analysis  
### *Data Science & Machine Learning Project*

Proyek ini menganalisis bagaimana **faktor cuaca** mempengaruhi permintaan penyewaan sepeda menggunakan dataset *Bike Sharing*. Analisis mencakup eksplorasi data, korelasi, visualisasi, partial correlation, hingga rekomendasi model Machine Learning.

---

## 📌 Tujuan Proyek

- Mengidentifikasi variabel cuaca yang paling mempengaruhi permintaan sepeda.  
- Membuat visualisasi hubungan antara fitur cuaca dan jumlah peminjaman.  
- Menyusun insight berbasis data untuk mendukung pengembangan model prediksi.  
- Menyediakan laporan analisis yang rapi dan siap digunakan sebagai portofolio.

---

## 📂 Dataset

Dataset yang digunakan:  
**Bike Sharing Dataset** (daily/hourly records).

Fitur utama:

- `temp` — temperatur  
- `atemp` — temperatur terasa  
- `hum` — kelembapan  
- `windspeed` — kecepatan angin  
- `weathersit` — kondisi cuaca  
- `cnt` — total permintaan  

---

## 🔍 Ringkasan Analisis

### 1️⃣ Korelasi Fitur Cuaca ke Permintaan

| Fitur         | Korelasi ke `cnt` | Insight |
|---------------|-------------------|---------|
| **temp**      | **+0.40**         | Cuaca hangat → permintaan naik |
| **atemp**     | +0.40             | Penguatan dari `temp` |
| **hum**       | **−0.32**         | Lembap → permintaan turun |
| **windspeed** | +0.09             | Pengaruh lemah |
| **weathersit**| −0.14             | Cuaca buruk → pengguna turun |

📌 **Temperatur adalah faktor cuaca paling dominan.**

---

### 2️⃣ Visualisasi yang Dibangun

- Scatter Plot (temp vs cnt, hum vs cnt, windspeed vs cnt)
  
  <img width="553" height="397" alt="scatter Plot cnt vs temp" src="https://github.com/user-attachments/assets/bb647e65-45d7-497b-bcbb-e0ad345bfc24" />
  <img width="553" height="397" alt="scatter Plot cnt vs hum" src="https://github.com/user-attachments/assets/7d83fff1-df19-4c6d-8bec-d0853a06ad63" />
  <img width="553" height="397" alt="scatter Plot cnt vs windspeed" src="https://github.com/user-attachments/assets/17db8844-0277-4e3f-9b0b-00671c0b53ca" />

- Pairplot
  <img width="985" height="986" alt="Pairplot" src="https://github.com/user-attachments/assets/ff47fd59-0ab7-41fe-9aeb-be88ff003a38" />

- Heatmap korelasi
  <img width="982" height="903" alt="Correlation Heatmap" src="https://github.com/user-attachments/assets/320f7bc1-44a4-46ba-bf6b-b742bee27192" />
- Partial correlation  

---

### 3️⃣ Partial Correlation

Analisis menunjukkan:

✔ **Temperatur tetap konsisten mempengaruhi permintaan** meskipun variabel lain dikontrol.

Hal ini memperkuat bahwa temperatur adalah fitur paling relevan untuk prediksi berbasis Machine Learning.

---

## 🤖 Pengembangan Machine Learning

Model yang direkomendasikan:

- **Linear Regression**  
- **Random Forest Regressor**  
- **XGBoost Regressor**  
- **Gradient Boosting Regressor**

Analysis tambahan yang disarankan:

- Feature Importance  
- SHAP Value (Explainable AI)  
- Hyperparameter tuning  

---

## 🧩 Struktur Proyek

