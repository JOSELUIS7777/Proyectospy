# B. PROGRAMA QUE CALCULA EL PROMEDIO DE UN ESTUDIANTE QUE CURSA LAS SIGUIENTES MATERIAS: METROLOGIA, ALGEBRA, CALCULO, ECONOMIA, ESTADISTICA, ESTUDIO DELTRABAJO.

print("B. PROGRAMA QUE CALCULA EL PROMEDIO DE UN ESTUDIANTE QUE CURSA LAS SIGUIENTES MATERIAS: METROLOGIA, ALGEBRA, CALCULO, ECONOMIA, ESTADISTICA, ESTUDIO DELTRABAJO.")



m=float(input('Escribe calificion en METROLOGIA : '))
a=float(input('Escribe calificion en ALGEBRA : '))
c=float(input('Escribe calificion en CALCULO : '))
e=float(input('Escribe calificion en ECONOMIA : '))
ec=float(input('Escribe calificion en ESTADISTICA : '))
et=float(input('Escribe calificion en ESTUDIO DEL TRABAJO : '))

prom= (m+a+c+e+ec+et) /6

if(prom<= 5):
    print("su promedio es: ",str(prom))
    print("Reprobado")  
else:
    print("su promedio es: ",str(prom))
    print("Felizadades has aprobado")

 