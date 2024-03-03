# List Pembelian dan Diskon
rokok_price = 20000
minyak_price = 25000
gula_price = 11000
diskon = 10000

# Menghitung Jumlah Pembelian dan Diskon
total_price = rokok_price + minyak_price + gula_price - diskon

# Jumlah Uang Yang Di Bawa Ucup
paid_by_ucup = 100000

# Menghitung Kembalian
change = paid_by_ucup - total_price

# Print Struk List Pembelian
print("======== WARUNG ========")
print("Rokok\t: {}".format(rokok_price))
print("Minyak\t: {}".format(minyak_price))
print("Gula\t: {}".format(gula_price))
print("Diskon\t: {}".format(diskon))
print("======================")
print("Total\t: {}".format(total_price))
print("Dibayar\t: {}".format(paid_by_ucup))
print("Kembalian\t: {}".format(change))
print("====== TERIMA KASIH ======")
