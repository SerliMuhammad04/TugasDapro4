# Meminta input dari pengguna 
nilai = int(input("Masukkan angka pilihan Anda: "))


# Konversi ke biner
convert = bin(nilai)[2:]
biner = convert.zfill(nilai)

print("Biner:", biner)

# Konversi ke oktal
oktal = oct(nilai)[2:]
print("Oktal:", oktal)

# Konversi ke desimal
desimal = (nilai)
print("Desimal:", desimal)

# Konversi ke heksadesimal
heksadesimal = hex(nilai)[2:]

print("Heksadesimal:", heksadesimal)

