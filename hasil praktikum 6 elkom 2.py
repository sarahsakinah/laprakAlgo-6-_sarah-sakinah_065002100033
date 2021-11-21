# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 00:07:04 2021

@nama :sarah sakinah
prodi:sistem informasi
nim :065002100033
"""
from math import pi

loop=1
while loop==1:
    def fungsikubus (a):
        print("sisi=",a,"luas=",6*a)
        return 6*a
    def fungsibalok(a,b,c):
        print('maka hasilnya adalah',(2*(a*b)) + (2*(a*c)) + (2*(b*c)))
        return (2*(a*b)) + (2*(a*c)) + (2*(b*c))
    def fungsitabung(a,b):
        print('maka hasilnya adalah',int(2*(pi*(a**2)))*(a+b))
        return float((2*(pi*(a**2)))*(a+b))
    def fungsikerucut(a,b):
        print('maka hasilnya adalah',pi*a*(a+b))
        return pi*a*(a+b)                 
    def fungsibola(a):
        print('maka hasilnya adalah',4*(pi*(a**2)))
        return 4*(pi*(a**2))
    print("KALKULATOR MENCARI LUAS\n1.Kubus\n2.Balok\n3.Tabung\n4.kerucut\n5.bola\n6.exit")
    tentukan=int(input('pilih menu yang tersedia: '))
    if tentukan==1:
        no1=int(input('masukkan nilai rusuk: '))
        fungsikubus(no1)
    elif tentukan==2:
        number1=int(input('masukkan panjang: '))
        number2=int(input('masukkan lebar: '))
        number3=int(input('masukkan tinggi'))
        fungsibalok(number1,number2,number3)
    elif tentukan==3:
        nummer1=float(input('masukkan jari jari: '))
        nummer2=float(input('masukan tinggi: '))
        float(fungsitabung(nummer1, nummer2))
    elif tentukan==4:
        numero1=float(input('masukkan jari jari: '))
        numero2=float(input('masukkan garis(s): '))
        fungsikerucut(numero1,numero2)
    elif tentukan==5:
        nomer1=float(input('masukkan jari jari:'))
        fungsibola(nomer1)
    elif tentukan==6:
        print('TERIMAKASIH!')
        break