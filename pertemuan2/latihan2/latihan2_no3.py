keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

keahlian_C = keahlian_A.union(keahlian_B)
print("Keahlian yang dimiliki kedua mahasiswa:", keahlian_C)
keahlian_A.difference_update(keahlian_B)
print("Keahlian yang hanya dimiliki mahasiswa A:", keahlian_A)
keahlian_B.symmetric_difference(keahlian_A)
print("Keahlian unik mahasiswa:", keahlian_A, keahlian_B)