from model import Muhasebe

# Create an instance of Muhasebe
muhasebe = Muhasebe()

# Get current stock data and item names
pismaniye_data, kestane_sekeri_data, cekme_helva_data, pismaniye_isim, kestane_sekeri_isim, cekme_helva_isim = muhasebe.sayim()

# Update stock and get the new data
chelva_yeni_data, kestane_sekeri_yeni_data, pismaniye_yeni_data = muhasebe.yeni_stok(pismaniye_data, kestane_sekeri_data, cekme_helva_data, pismaniye_isim, kestane_sekeri_isim, cekme_helva_isim)

# Calculate and print the sales data
muhasebe.satis_hesabi(chelva_yeni_data, kestane_sekeri_yeni_data, pismaniye_yeni_data)
