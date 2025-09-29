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