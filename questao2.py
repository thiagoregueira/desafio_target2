palavra = input('Digite uma palavra:\n')

contador = 0

for letra in palavra:
    if letra.lower() == 'a':
        contador += 1


if contador > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) aparece {contador} vezes na palavra '{palavra}'.")
else:
    print(f"A letra 'a' (maiúscula ou minúscula) não foi encontrada na palavra '{palavra}'.")
