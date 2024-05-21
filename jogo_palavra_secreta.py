palavra_secreta = 'elefante'
adivinhou = ''
num_tentativas = 0

while True:

    num_tentativas += 1

    letra = input("Digite uma letra: ").lower()

    if len(letra) > 1:
        print("---Digite apenas uma letra---")
        continue

    if letra in palavra_secreta:
        adivinhou += letra

    palavra_formada = ''

    for simbolo in palavra_secreta:
        if simbolo in adivinhou:
            palavra_formada += simbolo
        else:
            palavra_formada += "*"
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print("\nVOCÊ ACERTOU!!")
        print(f"A palavra era {palavra_secreta}")
        print(f"Numero de tentativas: {num_tentativas}\n")
