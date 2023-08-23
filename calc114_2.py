print("Qual sistema você quer?")
print("Digite 1 para calculadora")
print("")
print("Digite 2 para jogar um jogo de adivinhar o número")
print("")

e = float(input(""))

if e == 1:
    print("CALCULADORA")
    print(" ")
    while True:
        a = float(input("Digite o primeiro número: "))
        aff = input("")
        if aff == "teste" or aff == "TESTE":
            print("")
        else:
            bb = float(input("Digite o segundo número: "))
        c = input("Você quer um terceiro número? ")
        if c.lower() == "sim":
            cc = float(input("Digite o terceiro número: "))
            print("ok")
            print(" ")
            print("Digite a operação que você quer fazer?")
            print(" ")
            print("mais, menos ou multiplicação")
            print(" ")
            b = input("")
            print(" ")
            beb = a + bb + cc
            be = a - bb - cc
            bcb = a * bb * cc
            f = a ** bb
            if b.lower() == "mais" or b.lower() == "adição" or b.lower() == "soma" or b == "+":
                print(beb)
            elif b.lower() == "menos" or b.lower() == "subtração" or b == "-":
                print(be)
            else:
                print(bcb)
        else:
            print("ok")
            print(" ")
            print("Digite a operação que você quer fazer")
            print(" ")
            print("mais, menos, multiplicação, divisão, potência ou porcentagem?")
            print(" ")
            aa = input("")
            if aa.lower() == "mais" or aa.lower() == "soma" or aa == "+":
                e = a + bb
                print(e)
            elif aa.lower() == "menos" or aa.lower() == "subtração" or aa == "-":
                ee = a - bb
                print(ee)
            elif aa.lower() == "multiplicação" or aa.lower() == "mult" or aa == "x":
                eeee = a * bb
                print(eeee)
            elif aa.lower() == "divisao" or aa.lower() == "div" or aa == "÷":
                eee = a / bb
                print(eee)
            elif aa.lower() == "porcentagem" or aa.lower() == "por" or aa == "%":
                eeeee = a * bb / 100
                print(eeeee)
            elif aa.lower() == "potencia" or aa.lower() == "pot":
                f = a ** bb
                print(f)
            i = input("Você quer calcular mais? ")
            if i.lower() == "nao":
                print("Ok")
                print("Saindo da calculadora...")
                break

else:
    print("ADIVINHADOR DE NÚMEROS")
    print("")
    while True:
        import random
        print("Você quer customizar o jogo ou deixar o padrão?")
        print("(o padrão é de 0 a 100)")
        pootis = input("")
        if pootis.lower() == "padrao" or pootis.lower() == "deixar padrão":
            print("ok")
            print("")
            pootisr = random.randint(0, 100)
            while True:
                r = float(input(""))
                if r > pootisr:
                    print("Você passou")
                    print(".")
                elif r < pootisr:
                    print("Falta números")
                    print(".")
                else:
                    print("Você acertou")
                    break
        else:
            print("ok")
            er = float(input("digite o número que começa a contagem: "))
            err = float(input("digite o número que terminar a contagem: "))
            pootisrr = random.randint(er, err)
            while True:
                r = float(input(""))
                if r > pootisrr:
                    print("Você passou")
                elif r < pootisrr:
                    print("Falta números")
                else:
                    print("Você acertou")
                    break
        o = input("você quer jogar de novo? ")
        if o.lower() == "sim" or o.lower() == "s":
            print("ok")
        else:
            break
    