print('Program Menghitung Luas Bangun Datar\n')
p = int(input('masukan panjang persegi panjang: '))
l = int(input('masukan lebar persegi panjang: '))
s = int(input('masukan sisi persegi: '))

def luas(p,l):
    L = p * l
    return L

def luas_persegi(s):
    S = s * s
    return S

print('Jadi hasil luas bangun datar ialah :\n luas persegi panjang:\n{}, luas persegi:\n{}'.
format(p,l,s, luas(p,l), luas_persegi(s)))    