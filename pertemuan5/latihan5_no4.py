gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]

for barang in gudang_pc:
    if barang["item"] == "Keyboard" :
        barang["kategori"] = "Aksesoris"

print("Setelah ditambah headset:")
item_baru = {
    "item" : "Headset",
    "harga" : 350000,
    "stok" : 8
}
gudang_pc.append(item_baru)
print(gudang_pc)

for barang in gudang_pc:
    hasil = barang["harga"] * barang["stok"]
    print(f"Item: {barang["harga"]} | Total Aset: Rp {hasil}")
 