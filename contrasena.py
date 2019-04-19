"""
Autor: Diego Castro
Correo: diegomecatronico@gmail.com

Un método de seguridad comúnmente utilizado por los bancos es preguntar tres
caracteres aleatorios de una contraseña. Por ejemplo, si la contraseña es 531278, el banco
puede preguntar por el 2do, 3er, y 5to, carácter; esperando que el usuario responda con la 
secuencia 3-1-7.
El archivo keylog.txt contiene 50 secuencias correctas para una contraseña especifica.
Dado que cada una de las secuencias está en orden de primer carácter a ultimo carácter,
¿cuál es la contraseña más corta para la cual todas las secuencias son correctas?
"""



def cantidadDeHijos(numeros, datos):

    """De acuerdo a los dígitos y a las combinaciones, se hace un conteo de predecesores o hijos por cada dígito"""
    numeroHijos = list()
    for numero in numeros:
        hijos_c = list()
        for dato in datos:
            try:
                index = dato.index(numero)
                hijos_c.extend(list(dato[index + 1 :]))
            except ValueError:
                continue
        numeroHijos.append((len(set(hijos_c)), numero))
    return numeroHijos
                

def obtenerDatos():
    
    """Lee el contenido del archivo keylog.txt"""

    return set([str(number.rstrip()) for number in open("keylog.txt", "r")])

def obtenerDigitos(datos):
    """Obtiene los dígitos únicos que componen la contraseña buscada"""
    caracteres = set()
    for dato in datos:
        for c in dato:
            caracteres.add(c)
    return caracteres
        
if __name__ == "__main__":
    datos = obtenerDatos()
    digitos = obtenerDigitos(datos)
    numero_hijos = cantidadDeHijos(digitos, datos)
    
    #Organizo los numeros de mayor a menor número de predecesores.

    solucion = ''.join([x[1] for x in sorted(numero_hijos, reverse=True)])
    print ("La contraseña buscada es {0}".format(solucion))
   





