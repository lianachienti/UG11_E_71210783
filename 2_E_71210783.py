kata =input("Masukkan kata : ")

def kata(x):
    kata = len(x)
    if kata %2 == 1:
        if kata >= 5:
            y = int((kata - 1) / 2)
            return x[y - 1] + x[y] + x[y + 1]
        elif kata < 5:
           y = int((kata - 1) / 2)
           return x[y]
    elif kata %2 == 0:
         if kata < 8:
            y = int(kata / 2)
            return x[y - 1] + x[y]
         else:
            y = int(kata / 2)
            return x[y - 2] + x[y - 1] + x[y] + x[y + 1]

print("Huruf tengah pada kata" , kata, "adalah", x)
