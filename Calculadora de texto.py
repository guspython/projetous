while True:
    print("========================")
    print("[1]Adição.")
    print("[2]Subtração.")
    print("[3]Multiplicação.")
    print("[4]Divisão.")
    print("[5]Sair.")
    print("========================")

    escolha = input("_")

    if escolha == '1':
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        r = x + y
        print(f"{x} + {y} = {r}")

    elif escolha == '2':
        x1 = int(input("Digite o primeiro número: "))
        y1 = int(input("Digite o segundo número: "))
        r1 = x1 - y1
        print(f"{x1} - {y1} = {r}")

    elif escolha == '3':
        x2 = int(input("Digite o primeiro número: "))
        y2 = int(input("Digite o segundo número: "))
        r2 = x2 * y2
        print(f"{x2} x {y2} = {r2}")

    elif escolha == '4':
        x3 = int(input("Digite o primeiro número: "))
        y3 = int(input("Digite o terceiro número: "))

        if y3 != '0':
            print("************************\n*Erro, divisão por zero*\n************************")
            continue

        r3 = x3 / y3
        print(f"{x3} / {y3} = {r3}")

    elif escolha == '5':
        print("Saindo.")
        break

    else:
        print("**********************\n*Escolha corretamente*\n**********************")