from random import randint

#Menu

k = '+'
l = '-'
m = '/'
n = '*'
op = [ k , l , m , n]

print("=====Program test aritmatika dasar=====")
print("Pilihan level yang tersedia : ")
print("1. Easy")
print("2. Medium")
print("3. Hard")

opsi = input("Masukkan tingkatan yang ingin anda coba : ")
op = [ '+' , '-' , '/' , '*']

#Opsi 1

if opsi == '1' :
    a = randint(20,50)
    b = randint(1,4)
    c = randint(20,50)

    if b == 1 :
        print("Berapakah hasil dari", a ,"+", c)
        x = a + c
        ans = input("Masukkan Jawaban Anda : ")

        if ans == x :
                    print("Jawaban Anda Benar !")
        elif ans != x :
            print("Jawaban Anda Masih Salah !")
            print("Hasil dari" , a , "+", c ,"=" , x)

    elif b == 2 :
        print("Berapakah hasil dari", a ,"-", c)
        x = a - c
        ans = input("Masukkan Jawaban Anda : ")

        if ans == x :
                    print("Jawaban Anda Benar !")
        elif ans != x :
            print("Jawaban Anda Masih Salah !")
            print("Hasil dari" , a , "-", c ,"=" , x)

    elif b == 3 :
        print("Berapakah hasil dari", a ,"/", c)
        x = a / c
        ans = input("Masukkan Jawaban Anda : ")

        if ans == x :
                    print("Jawaban Anda Benar !")
        elif ans != x :
            print("Jawaban Anda Masih Salah !")
            print("Hasil dari" , a , "/", c ,"=" , x)

    elif b == 4 :
        print("Berapakah hasil dari", a ,"*", c)
        x = a * c
        ans = input("Masukkan Jawaban Anda : ")

        if ans == x :
                    print("Jawaban Anda Benar !")
        elif ans != x :
            print("Jawaban Anda Masih Salah !")
            print("Hasil dari" , a , "*", c ,"=" , x)
        
#Opsi 2
if opsi == '2' :
    a = randint(20,70)
    b = randint(20,70)
    c = randint(20,70)
    d = choice(op)

    hasil = input("Masukan Jawaban Anda : ")
    x = a, d , b ,d , c
    if hasil == x :
        print("Jawaban Anda Benar !")
    elif hasil != x :
        print("Jawaban Anda Masih Salah !")
        print("Hasil dari", a , d , b , d , c , "=", x)
#Opsi 3
if opsi == '3' :
    a = randint(20,100)
    b = randint(20,100)
    c = randint(20,100)
    d = randint(20,100)
    e = choice(op)

    hasil = input("Masukan Jawaban Anda : ")
    x = a, e , b , e , c , e , d

    if hasil == x :
       print("Jawaban Anda Benar !")
    elif hasil != x :
        print("Jawaban Anda Masih Salah !")
        print("Hasil dari", a, e , b , e , c , e , d, "=", x) 
