#Menu

print("======Program Manipulasi String======")
print("Pilihan Menu")
print("1. Hitung Kata")
print("2. Cek Kata")
print("3. Ubah Kata")


opsi = input("Pilihan anda : ")
kata = input("Masukkan sebuah kalimat/kata : ")
hasil = (kata.lower())

#Opsi 1

if opsi == '1' :
    a = input("Masukkan kata yang ingin dihitung : ")
    x = hasil.count(a)

    print("Terdapat sebanyak", x , "kata" , a , "didalam string")

#Opsi 2

if opsi == '2' :
    a = input("Masukkan kata yang ingin di cek : ")
    x = a.upper()
    y = hasil.replace(a,x)

    print("Kata" , a , "terdapat didalam string")
    print("String diubah menjadi : ")
    print(y)

#Opsi 3

if opsi == '3' :
    a = input("Masukkan kata yang ingin di ubah : ")
    b = input("Masukkan kata pengganti : ")

    print("Anda akan mengubah kata" , a , "menjadi" , b , "sebanyak 1x")
    ubah = input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")

    if ubah == 'yes' :
        x = int(input("Masukkan jumlah total penggantian : "))
        print("String berhasil diubah menjadi : ")
        y = hasil.replace(a , b , x)
        print (y)
        
    elif ubah == 'no' :
        x = 1
        print("String berhasil diubah menjadi : ")
        y = hasil.replace(a , b , x)
        print (y)
    
