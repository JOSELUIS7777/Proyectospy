# 3. PROGRAMA QUE CALCULA EL IMC (INDICE DE MASA CORPORAL) DE UNA PERSONA.

print("3. PROGRAMA QUE CALCULA EL IMC (INDICE DE MASA CORPORAL) DE UNA PERSONA.")

peso = float(input('Escribe si peso (kg): '))
estatura=float(input('Escribe si estarura (metros): '))

d=estatura*estatura

imc=peso/d

if imc < 18.5 :
    print("Peso: Flaco")
    print('Su IMC es: ',imc)
elif ((imc >= 18.5 and imc <= 25) or (imc >= 18.5 and imc <= 24)) :
    print("Peso: normal")
    print('Su IMC es: ',imc)
elif ((imc > 25 and imc <= 30) or (imc >24 and imc <= 28)) :
    print("Peso: Gordo")
    print('Su IMC es: ',imc)
elif ((imc > 30) or (imc >28)) :
    print("Peso: obesidad")
    print('Su IMC es: ',imc)

