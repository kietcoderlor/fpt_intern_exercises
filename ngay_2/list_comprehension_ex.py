tap_so = [int(x.strip()) for x in input("Nhập các số nguyên (cách nhau bằng dấu phẩy): ").split(",")]
so_chan = [x ** 2 for x in tap_so if x % 2 == 0]
print(so_chan)
