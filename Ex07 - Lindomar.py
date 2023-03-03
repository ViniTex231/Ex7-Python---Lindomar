peso_list = []
nome_list = []
qtd = 0

while True:
    nome = (input(f"Digite o seu nome: "))
    nome_list.append(nome)
    qtd += 1
    peso = float(input(f"Digite o seu peso: "))
    peso_list.append(peso)
    continuar = input(f"Deseja inserir outros dados?Digite S ou N. ").lower()
    if continuar != "s":
        pesoord = peso_list[:]
        pesoord.sort()
        menorpeso = pesoord[0]
        maiorpeso = pesoord[-1]
        break
print(f"Dados cadastrados: ", qtd)
print(f"O menor peso é: ", menorpeso, "kg")
print(f"O maior peso é: ", maiorpeso, "kg")