salario = float(input())
porc = float(input())
novo = salario + ((salario * porc) / 100)
print("Seu salario teve aumento de {} %, passando de R$ {} para R$ {}".format(porc, salario, novo))
