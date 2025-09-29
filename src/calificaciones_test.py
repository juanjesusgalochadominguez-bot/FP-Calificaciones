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