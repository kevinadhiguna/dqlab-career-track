# Definsikan fungsi dengan nilai default argument kedua adalah "".
def fungsi_dengan_argumen(nama_depan, nama_belakang=""):
	print(nama_depan+" "+nama_belakang)
# Panggil fungsi dengan memasukkan argumen nama_depan "John"
fungsi_dengan_argumen("John")
# Panggil fungsi dengan memasukkan argumen
# nama_depan yaitu "John" dan nama_belakang "Doe"
fungsi_dengan_argumen("John", "Doe")