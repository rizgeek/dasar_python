# operasi aritmatika

a = 10
b = 3

# penjumlahan
hasil = a + b
print(hasil)

# pengurangan
hasil = a - b
print(hasil)

# perkalian
hasil = a * b
print(hasil)

# pembagian
hasil = a / b
print(hasil)

# eksponen(pangkat)
hasil = a ** b
print(hasil)

# modulus
hasil = a % b
print(hasil)

# floor division
hasil = a // b
print(hasil)

# prioritas operasi, operational precendence
"""
    1. ()
    2. exponen
    3. perkalian dan teman teman * / ** % //
    4. perjumlahan dan pengurangan
"""

x = 3
y = 2 
z = 4

hasil =  x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)