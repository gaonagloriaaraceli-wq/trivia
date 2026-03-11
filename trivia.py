nombre_usuario=input("Ingrese su nombre")
print(f"Bienvenid@ {nombre_usuario} a esta trivia ")
puntos=0

pregunta1=int(input("Cuánto es 2+2?"))
if pregunta1==4:
    puntos=puntos+1
else: 
    print("La respuesta no es correcta")
pregunta2=int(input("Cuánto es 6-2?"))
if pregunta2==4:
    puntos=puntos+1
else: 
    print("La respuesta no es correcta")
pregunta3=int(input("Cuanto es 2 x 2?"))
if pregunta3==4:
    puntos=puntos+1
else: 
    print("La respuesta no es correcta")
pregunta4=int(input("Cuánto es 8/2?"))
if pregunta4==4:
    puntos=puntos+1
else: 
    print("La respuesta no es correcta")

print(puntos)

if puntos==4:
    print("Excelente")
elif puntos >= 2:
    print("Muy bien")
else: print("Puedes mejorar")



    

