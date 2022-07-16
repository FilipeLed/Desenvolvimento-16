def calculadora(num1, num2, opc):
    
    if opc == 1:
        res = num1+num2
    elif opc == 2:
        res = num1-num2
    elif opc == 3:
        res = num1*num2
    elif opc == 4:
        res = num1/num2
    else:
        res = "Operação invalida"
    return res

a= float(input("Digite o primeiro número \n"))
b = float(input("Digite o segundo número \n"))
c = int(input("Digite a operação: 1. Soma 2. Subtração 3. Multiplicação 4. Divisão \n"))
resultado = calculadora(a, b, c)
print(resultado)


