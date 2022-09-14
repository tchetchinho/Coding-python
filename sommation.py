print("Ceci est un programme qui calcule ln somme de 0 a N \n\n")

n = int(input("Entrez un nombre : "))
som = n

for i in range(0, n):
    print(i,"+ ", end='')
    som += i

print(f"{n} = {som}")
