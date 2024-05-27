#Tipe data adalah macam macam data
#a = 10, a adalah variabel dengan nilai 10

#Tipe data : angka satuan yang gak ada koma(integer)
data_integer = 11
print("data :", data_integer)
print("- bertipe :", type(data_integer))

#Tipe data : angka dengan koma(float)
data_float = 1.5
print("data :", data_float)
print("- bertipe :", type(data_float))

#Tipe data : kumpulan karakter (string)
data_string = "rahma"
print("data :", data_string)
print("- bertipe :", type(data_string))

#Tipe data : biner true/false (boolean)
data_bool = True
print("data :", data_bool)
print("- bertipe :", type(data_bool))

##tipe data khusus
#bilangan kompleks
#misal 5 + 6i (i = imajiner)
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertipe :", type(data_complex))

#tipe data dari bahasa C
#karena py dibuat menggunakan bahasa C maka kita bisa mengunakan bahasa C
from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe :", type(data_c_double))