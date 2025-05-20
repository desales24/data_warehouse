import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data asli
file_path = "Sport car price.csv"
df = pd.read_csv(file_path)

# Bersihkan harga
df["Price (in USD)"] = df["Price (in USD)"].replace(",", "", regex=True).astype(float)

# Group by Car Make dan ambil harga tertinggi tiap tipe mobil
df_grouped = df.groupby("Car Make")["Price (in USD)"].max().reset_index()

# Sort descending berdasarkan harga tertinggi
df_plot = df_grouped.sort_values(by="Price (in USD)", ascending=False).head(50).reset_index(drop=True)

# Buat daftar warna berdasarkan colormap
colors = plt.cm.plasma(np.linspace(0, 1, len(df_plot)))  # Menggunakan colormap "plasma" untuk variasi warna

# Membuat figure dan mengubah warna background
fig, ax = plt.subplots(figsize=(12, 6))
fig.set_facecolor("#E3F2FD")  # Background seluruh figure (biru muda)
ax.set_facecolor("#F9F9F9")  # Background area plot (abu-abu terang)

# Buat diagram batang
ax.bar(df_plot["Car Make"], df_plot["Price (in USD)"], color=colors)

# Label sumbu X sesuai Car Make
plt.xticks(rotation=45, ha="right", fontsize=9)

# Judul
plt.title("Harga Tertinggi Sport Car per Merek", fontsize=16, weight='bold')

# Grid horizontal
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.5)

# Format label sumbu Y dengan pemisah ribuan
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
plt.ylabel("Harga (USD)")

plt.tight_layout()
plt.show()