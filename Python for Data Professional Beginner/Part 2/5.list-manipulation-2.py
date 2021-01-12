# Fitur .index()
print(">>> Fitur .index()")
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud') + 1
print(score_pertama_sud) # akan menampilkan output 2
# Fitur .insert()
print(">>> Fitur .insert()")
list_score = ['Budi','Sud','Budi','Budi','Sud']
list_score.insert(3, 'Sud')
print(list_score)
# Fitur .pop()
print(">>> Fitur .pop()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_menu.pop(1)
print(list_menu)
# Fitur .remove()
print(">>> Fitur .remove()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.remove('Rendang')
print(list_menu)
# Fitur .reverse()
print(">>> Fitur .reverse()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.reverse()
print(list_menu)
# Fitur .sort()
print(">>> Fitur .sort()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.sort() # Default: Ascending
print(list_menu) 
list_menu.sort(reverse=True)# Descending
print(list_menu) 