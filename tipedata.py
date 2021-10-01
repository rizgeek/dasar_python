# a = 10, a adalah variabel dengan nilai 10

# macam macam tipe data di python
# angka satuan (integer)
data_integer = 123
print("data : ", data_integer)
print(" - bertipe : ", type(data_integer))

# angka dengan koma (float), double tidak ada di python
data_float = 31.2
print("data : ", data_float)
print(" - bertipe : ", type(data_float))

# kumpulan karakter (string)
data_string = "ini adalah ucup"
print("data : ", data_string)
print(" - bertipe : ", type(data_string))

# biner atau true / false (boolean)
data_string = False
print("data : ", data_string)
print(" - bertipe : ", type(data_string))



## tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print("data : ", data_complex)
print(" - bertipe : ", type(data_complex))

# tipe data dari bahasa C (karena python dibuat dengan bahasa C kita bisa memakai variabel dari bahasa C)
from ctypes import c_double, c_char, c_long, c_ulong 

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print(" - bertipe : ", type(data_c_double))
