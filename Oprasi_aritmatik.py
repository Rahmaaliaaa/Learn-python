a = 17
b = 5

# operasi tambah +
# output 17 + 5 = 22
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan -
# output 17 - 5 = 12
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian *
# output 17 * 5 = 85
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian /
# output 17 / 5 = 3.4
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (pangkat) **
# output 17 ** 5 = 1419857
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus %
# modulus adalah sisa bagi
# mod 17 / 5 int 3
# 5 * 3 = 15
# 17 - 15 = 2 -> mod 17 = 2
# output 17 % 5 = 2
hasil = a % b
print(a, '%', b, '=', hasil)

# oprasi floor division //
#floor division adalah kebalikan dari modulus
# output floor division dari 17 // 5 = 3
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi, operational precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x , '=', hasil )

hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil)
hasil = (x + y) * z
print('(',x, '+', y, ') *', z, '=', hasil)