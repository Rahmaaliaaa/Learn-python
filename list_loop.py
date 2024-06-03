# for loop : mengulangi item daftar
my_list = [10, 20, 30]
for x in my_list:
    print(x)


# range() dan len() : untuk iterable yang sesuai   
my_list = ["apple", "banana", "cherry"]
for i in range(len(my_list)):
    print(my_list[i])   


# while loop : untuk menelusuri semua nomor indeks
my_list = [5, 15, 25]
i = 0
while i < len(my_list):
    print(my_list[i])
    i = i + 1


# Pemahaman Daftar menawarkan sintaks terpendek untuk mengulang daftar
# fungsi for : yang akan mencetak semua item dalam daftar
my_list = ["kiwi", "jeruk", "melon"]
[print(x) for x in my_list]   



