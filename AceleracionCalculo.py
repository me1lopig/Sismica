# calculo de la aceleración sísmica

# entrada de datos

# numero de unidades
n_unidades=int(input("Número de unidades ="))

suma_espesores=0
producto_c=0

for i in range(0,n_unidades):
    print("Unidad ",i+1)
    espesor=float(input("Espesor de la unidad "))
    c_parcial=float(input("Valor del coef. parcial C="))
    producto_c+=espesor*c_parcial
    suma_espesores+=espesor # comprobamos que la suma es 30

# comprobaciones de los datos introducidos, espesores
if (suma_espesores!=30):
    print("La suma de los espesores no es de 30 m")
    print("Compruebe los valores de entrada")
    exit() # se sale del programa



ab=float(input("Aceleración basica adimensional ab="))
rho=float(input("Coeficinte de riesgo rho=[ 1 o 1.3]="))
c=producto_c/30 # promedio ponderado del coeficiente del terreno


# Calculo del coficiente de amplificación del terreno
producto=ab*rho

# calculo según los rangos
if (producto<=0.1):
    S=c/1.25
elif (0.1<=producto<0.4):
    S=c/1.25+3.33*(rho*ab-0.1)*(1-c/1.25)
elif(0.4<producto):
    S=1.0

# IMpresion 
print("El valor del coeficiente de amplificacion, S=",S)

