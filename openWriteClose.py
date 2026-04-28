arquivo = open("novo_poema.txt", "w")

print(arquivo.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"))
print(arquivo.write("In nec nulla consequat, bibendum ex in, eleifend dui.\n"))
print(arquivo.write("FIM\n  -Caique GS"))

arquivo.close()