#Menu

print("Menu Program Yang Tersedia")
print("1. Pangkatkan angka")
print("2. Akarkan bilangan")

#Pilihan
opsi = input("Masukan pilihan yang diinginkan : ")

#Opsi 1
if opsi  == '1' :
    a1 = float(input("Masukkan angka yang ingin dipangkatkan angka : "))
    modif = input("Ingin memodifikasi pangkat? (yes/no) : ") 

    if modif == 'yes' :
        m1 = float(input("Masukkan nilai pangkat : "))
        print("Hasil dari" , a1 , "^" , m1 , "=" , pow(a1, m1))

    elif modif == 'no' :
          m2 = 2
          print("Hasil dari" , a1 , "^" , m2 , "=" , pow(a1, m2))


#Opsi 2
if opsi == '2' :
    a1 = float(input("Masukkan angka yang ingin diakar angka : "))
    modif = input("Ingin memodifikasi pangkat? (yes/no) : ")

    if modif == 'yes' :
        m1 = float(input("Masukan nilai akar : "))
        hasil = round(pow(a1,1/m1), 2)
        print("Hasil akar pangkat" , m1 , "dari" , a1 , "=" , hasil)

    elif modif == 'no' :
        m2 = 2
        hasil = round(pow(a1,1/m2), 2)
        print("Hasil akar pangkat", m2 , "dari" , a1 , "=" , hasil)
