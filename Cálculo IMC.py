#Cálculo IMC
print("----------Cálculo IMC----------")
print("------------ALTURA-------------")

#Altura deve ser inserida com ponto flutuante ex.:(1.75)
altura = float(input("Informe a Altura: "))
massa = float(input("Informe a Massa: "))
#peso

"""
altura = float(a)
assa = float(m)
"""
print(type(altura))

imc = massa/(altura*altura)
print(imc)

if imc < 17 :
    print("Você está MUITO abaixo do Peso")  

elif (imc >= 17 and imc < 18.5):
    print("Você está abaixo do peso")

elif(imc >= 18.5 and imc <25):
    print("Você está no Peso Ideal")

elif(imc > 25 and imc <= 30):
    print("Você está acima do peso")

elif(imc > 30 and imc <=35):
    print("Você está com Obesidade")
    
elif(imc > 35 and imc <= 40):
    print("Você está com Obesidade Severa")

else:
    print("Você está com Obesidade Mórbida")
