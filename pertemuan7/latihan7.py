noPlat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
def cekPlatNomor():
    platGanjil = []
    platGenap = []

    for i in noPlat:
        data = i.split()[1]
        int(data)
        if data % 2 == 0:
            platGanjil.append(noPlat)
            print(platGanjil)
        else: 
            platGenap.append(noPlat)
            print(platGenap)

cekPlatNomor()