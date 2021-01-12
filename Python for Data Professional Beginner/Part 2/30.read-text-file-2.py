# Membaca file hello.txt dengan fungsi readlines()
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open("hello.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)
# Membaca file hello.txt dengan menerapkan looping
print(">>> Membaca file hello.txt dengan menerapkan looping")
file = open("hello.txt", "r")
for line in file:
    print(line)