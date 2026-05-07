ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

print("Mahasiswa yang mendaftar di ukm coding saja:")
coding_saja = ukm_coding - ukm_robotik
print(coding_saja)

print("Mahasiswa yang mendaftar di salah satu atau kedua ukm:")
unik = ukm_robotik & ukm_coding
print(unik)

if "Andi" not in ukm_robotik:
    print("False")