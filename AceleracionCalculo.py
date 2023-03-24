# calculo del coeficiente de amplificación

# entrada de datos

ab=float(input("Aceleración basica adimensional ab="))
rho=float(input("Coeficinte de riesgo rho=[ 1 o 1.3]="))
c=float (input("Coeficiente del terreno C="))


# Calculo del coficiente de amplificación del terreno
producto=ab*rho

print("Producto =",producto)

# calculo según loa rangos
if (producto<=0.1):
    S=c/1.25
elif (0.1<=producto<0.4):
    S=c/1.25+3.33*(rho*ab-0.1)*(1-c/1.25)
elif(0.4<producto):
    S=1.0

# IMpresion 
print("El valor del coeficiente de amplificacion, S=",S)

