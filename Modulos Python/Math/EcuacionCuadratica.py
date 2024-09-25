import math

def Ecuacion_Cuadratica(a, b, c):
    
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * 0)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2
    else:
        return "La ecuacion no tiene solucion"

a = 2
b = 8
c = 1

solucion = Ecuacion_Cuadratica(a, b, c)
print("la solucion cuadratica es:" + solucion)
        