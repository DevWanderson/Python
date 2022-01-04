#Cálculo IMC
print("----------Cálculo IMC----------")
print("-------------ALTURA------------")

altura = float(input("Informe a Altura: "))
massa = float(input("Informe a Massa: "))
#peso

#altura = float(a)
#assa = float(m)
print(type(altura))

imc = massa/(altura*altura)
print(imc)
if imc < 18.5: {
    print("Você está abaixo do peso")
}
elif (imc >18.4 & imc <25): {
    print("Você está no Peso Ideal")
}
elif imc > 24.9 & <30{
    print("Você está com sobrepeso")
}