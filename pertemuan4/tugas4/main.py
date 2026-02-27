import kurs as ku
import konverter as ko
from tabulate import tabulate
print("=== KONVERSI MATA UANG ===")
print(tabulate(ku.kurs_data.items(), headers=["Kode", "Kurs"], tablefmt="psql"))

ko.konversi_mata_uang()
