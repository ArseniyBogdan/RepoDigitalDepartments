# TODO Найдите количество книг, которое можно разместить на дискете
disk_volume_bytes = int(1.44 * 1024 * 1024)
volume_of_book_bytes = 100 * 50 * 25 * 4

print("Количество книг, помещающихся на дискету:", disk_volume_bytes // volume_of_book_bytes)
