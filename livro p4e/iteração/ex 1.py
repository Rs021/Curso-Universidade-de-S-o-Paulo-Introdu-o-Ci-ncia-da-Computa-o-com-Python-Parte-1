count = 0
total = 0
maior = 0
menor = 0
while True:
    try:
        n = input("Digite um número: ")
        if n == "pronto":
            break
        a = int(n)
        if maior == 0 or a > maior:
            maior = a
        if menor == 0 or a < menor:
            menor = a

        total += int(n)
        count += 1
    except:
        print("Entrada Inválida")


print(total, count, maior, menor, sep=" ")
