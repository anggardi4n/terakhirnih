import streamlit as st

# Menampilkan bagian header
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #e0f7fa;
            margin: 0;
            padding: 0;
            color: #333;
        }
        header {
            background-color: #0288d1;
            color: white;
            padding: 20px 0;
            text-align: center;
            font-size: 2rem;
            border-bottom: 5px solid #01579b;
        }
        .container {
            padding: 30px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 30px auto;
            max-width: 800px;
        }
        h2 {
            color: #0288d1;
            text-align: center;
        }
        label {
            font-size: 1rem;
            font-weight: bold;
            display: block;
            margin: 10px 0;
        }
        select, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            font-size: 1rem;
        }
        .result {
            margin-top: 20px;
        }
        .result-item {
            padding: 15px;
            margin-bottom: 10px;
            background-color: #f4f4f4;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .cluster-info {
            margin-top: 20px;
            padding: 15px;
            background-color: #f4f4f4;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .footer {
            background-color: #0288d1;
            color: white;
            padding: 10px 0;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
    <header>
        <h1>Alat Tangkap Ikan dan Clustering</h1>
    </header>
""", unsafe_allow_html=True)

# Menampilkan form pilihan alat tangkap
st.markdown("""
    <div class="container">
        <h2>Temukan Data Alat Tangkap dan Jenis Ikan</h2>
        <label for="gear-select">Pilih Alat Tangkap:</label>
        <select id="gear-select">
            <option value="all">Semua Alat Tangkap</option>
            <option value="Rawai Tuna">Rawai Tuna</option>
            <option value="Jaring Insang Hanyut">Jaring Insang Hanyut</option>
            <option value="Bubu">Bubu</option>
            <option value="Bouke Ami">Bouke Ami</option>
            <option value="Pancing Ulur">Pancing Ulur</option>
            <option value="Bagan Berperahu">Bagan Berperahu</option>
        </select>
    </div>
""", unsafe_allow_html=True)

# Membuat daftar data ikan dan alat tangkap (menghapus Pukat Cincin Pelagis dan Layangan Benggol)
data = [
    {"ikan": "Cakalang", "alat": "Rawai Tuna", "cluster": 2},
    {"ikan": "Bawal Hitam", "alat": "Jaring Insang Hanyut", "cluster": 2},
    {"ikan": "Kerapu Karang", "alat": "Bubu", "cluster": 0},
    {"ikan": "Lemuru", "alat": "Bouke Ami", "cluster": 0},
    {"ikan": "Tenggiri", "alat": "Pancing Ulur", "cluster": 1},
    {"ikan": "Rajungan", "alat": "Bagan Berperahu", "cluster": 1}
]

# Filter data berdasarkan alat tangkap yang dipilih
selected_gear = st.selectbox("Pilih Alat Tangkap:", ["Semua Alat Tangkap", "Rawai Tuna", "Jaring Insang Hanyut", "Bubu", "Bouke Ami", "Pancing Ulur", "Bagan Berperahu"])

filtered_data = [item for item in data if selected_gear == "Semua Alat Tangkap" or item["alat"] == selected_gear]

# Menampilkan hasil pencarian berdasarkan filter
st.markdown("<div id='result-container' class='result'></div>", unsafe_allow_html=True)
for item in filtered_data:
    st.markdown(f"""
        <div class="result-item">
            <h3>{item['ikan']}</h3>
            <p><strong>Alat Tangkap:</strong> {item['alat']}</p>
            <p><strong>Cluster:</strong> {item['cluster']}</p>
        </div>
    """, unsafe_allow_html=True)

# Menampilkan informasi cluster
st.markdown("""
    <div id="cluster-info" class="cluster-info">
        <h3>Informasi Tentang Cluster</h3>
        <p><strong>Cluster 0:</strong> Ikan-ikan dalam cluster ini cenderung memiliki nilai dan volume produksi yang lebih rendah. Mereka sering kali ditangkap menggunakan alat tangkap tradisional atau kecil, seperti "Bubu" dan "Jaring Insang Hanyut." Ikan dalam cluster ini mencakup jenis yang kurang bernilai ekonominya namun memiliki potensi pasar lokal yang besar.</p>
        <p><strong>Cluster 1:</strong> Cluster ini terdiri dari ikan-ikan yang lebih bernilai komersial dan sering kali ditangkap dengan alat tangkap yang lebih besar dan modern. Alat tangkap yang digunakan seperti "Bagan Berperahu" dan "Pancing Ulur," yang menunjukan usaha penangkapan dengan skala yang lebih besar dan komersial. Ikan di cluster ini lebih sering dikonsumsi secara luas di pasar internasional.</p>
        <p><strong>Cluster 2:</strong> Ikan-ikan dalam cluster ini adalah yang paling bernilai dan memiliki produksi yang tinggi. Mereka ditangkap menggunakan metode industri dan teknologi canggih seperti "Rawai Tuna" dan "Jaring Insang Hanyut." Cluster ini berfokus pada ikan-ikan yang memiliki permintaan tinggi dan sangat penting untuk sektor perikanan komersial.</p>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>&copy; 2025 Alat Tangkap Ikan - Semua Hak Cipta Dilindungi</p>
    </div>
""", unsafe_allow_html=True)
