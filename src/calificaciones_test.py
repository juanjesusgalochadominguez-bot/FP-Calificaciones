from calificaciones import *

#9.1, 7.2 ==> 8.15
#4.0, 6.0 ==> 5.0
#4.0, 3.0 ==> 3.5
#None, 3.0 ==>1.5
#9.0, None ==> 4.5
#None, None ==> 0.0

print(nota_teoria(9.1, 7.2))

print(nota_teoria(4.0, 6.0))

print(nota_teoria(4.0, 3.0))

print(nota_teoria(None, 3.0))

print(nota_teoria(9.0, None))

print(nota_teoria(None, None))

#9.1, 7.2, 8.1 ==> 8.110000000000001
#4.0, 6.0, 5.0 ==> 5.0
#4.0, 3.0, None ==> 0
#None, 3.0, None  ==>0
#9.0, None, 4.5 ==> 4.5
#9.0, None, None ==> 1.3499999999999999
#None, None, None ==> 0

print(nota_cuatrimestre(9.1, 7.2, 8.1))
print(nota_cuatrimestre(4.0, 6.0, 5.0))
print(nota_cuatrimestre(4.0, 3.0, None))
print(nota_cuatrimestre(None, 3.0, None))
print(nota_cuatrimestre(9.0, None, 4.5))
print(nota_cuatrimestre(9.0, None, None))
print(nota_cuatrimestre(None, None, None))


#notas teoría:  9.6, 9.9, 10.0, 9.8 notas_práctico: 9.7, 9.5 ==> 9.6675
#notas teoría: 4.4, 4.9, 5.1, 4.7 notas_práctico: 4.6, 4.8 ==> 4.0
#notas teoría: 4.0, 6.0, 4.0, 3.0 notas_práctico: 5.0, None ==> 2.5
#notas teoría: 9.0, None, 4.0, 3.0 notas_práctico: 4.5, None ==> 2.25
#notas teoría: 9.0, 5.0, 4.0, None notas_práctico: 4.5, None ==> 2.25

print("Notas continuas")
print(nota_continua([9.6, 9.9, 10.0, 9.8], [9.7, 9.5]))
print(nota_continua([4.4, 4.9, 5.1, 4.7], [4.6, 4.8]))
print(nota_continua([4.0, 6.0, 4.0, 3.0], [5.0, None]))
print(nota_continua([9.0, None, 4.0, 3.0], [4.5, None]))   
print(nota_continua([9.0, 5.0, 4.0, None], [4.5, None]))
