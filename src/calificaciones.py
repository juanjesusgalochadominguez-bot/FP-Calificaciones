def nota_teoria(nota_t1, nota_t2):
    '''Dadas las notas de los dos exámenes teóricos de un cuatrimestre, permite calcular la nota que un alumno
    tiene  en el bloque teórico de ese cuatrimestre.
    La nota se calcula como la media de las notas de ambos cuatrimestres.
    Una nota con valor None indica que el alumno no se ha presentado al examen, y se considerará como un cero.'''
    return (a_cero(nota_t1) + a_cero(nota_t2))/2

def a_cero(valor):
    resultado = 0
    if valor is not None:
        resultado = valor
    return resultado

def a_cero_alt(valor):
    if valor is None:
        return 0
    return valor

def nota_cuatrimestre(nota_t1, nota_t2, nota_p):
    
    t1=a_cero(nota_t1)
    t2=a_cero(nota_t2)
    p=a_cero(nota_p)

    media_teoria = nota_teoria(t1, t2)
    if media_teoria < 4:
        nota_cuatri = 0
        return nota_cuatri
    
    nota_cuatri = 0.15*t1 + 0.15*t2 + 0.7*p
    return nota_cuatri

def nota_continua(lista_t, lista_p):
    
    for i in range(len(lista_t)):
        lista_t[i] = a_cero(lista_t[i])
        i=i+1
    for j in range(len(lista_p)):
        lista_p[j] = a_cero(lista_p[j])
        j=j+1

    nota_cuatri1 = nota_cuatrimestre(lista_t[0], lista_t[1], lista_p[0])
    nota_cuatri2 = nota_cuatrimestre(lista_t[2], lista_t[3], lista_p[1])

    if nota_cuatri1 < 5 or nota_cuatri2 < 5:
        nota_curso = min(4.0, (nota_cuatri1 + nota_cuatri2)/2)
        return nota_curso
    
    nota_curso = (nota_cuatri1 + nota_cuatri2)/2
    return nota_curso