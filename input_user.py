# input user

# data yang dimasukan pasti string
data = input("Masukan Data : ")
print("data = ", data, "type = ", type(data))

# jika kita ingin mengambil integer
angka = float(input("Masukan angka : "))
print("data = ", angka, "type = ", type(angka))

# bagaimana dengan bolean
data_bool = bool( int( input("Masukan Data boolen : ") ) )
print("data = ", data_bool, "type = ", type(data_bool))