# Statement if
x = 4
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua") # statemen aksi lebih menjorok ke dalam
# Statement if ... elif ... else
x = 7
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")
elif x % 3 == 0: # jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi tiga")
elif x % 5 == 0: # jika sisa bagi x dengan 5 sama dengan 0
    print("x habis dibagi lima")
else:
    print("x tidak habis dibagi dua, tiga ataupun lima")