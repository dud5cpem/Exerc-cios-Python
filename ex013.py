salario = float(input("Digite o seu salário: "))
vl = salario *15/100
resultado = salario + vl
print("O funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}".format(salario, resultado))