"""

Autor: Diego Castro
Correo: diegomecatronico@gmail.com

¿Durante el siglo 20 (1 de enero de 1901 hasta 31 de diciembre de 2000), cuántos meses
han empezado un domingo?

"""

from datetime import date
from dateutil.rrule import rrule, MONTHLY

def obtenerCantidadDeDomingos(FECHA_INICIO, FECHA_FINAL):
    """Obtiene la cantidad de domingos, dado un rango de fechas"""

    numero_domingos = 0
    nombre_dia_semana = "Sunday"

    #Se usa rrule para obtener una lista iterable de fechas. MONTLY para extraer el primer día del mes.
    
    for fecha in rrule(MONTHLY, dtstart=FECHA_INICIO, until=FECHA_FINAL):
        dia_semana = fecha.strftime("%A")
        if dia_semana == nombre_dia_semana:
            numero_domingos += 1

    print("Desde el {0} hasta el {1}, {2} meses han empezado un {3}".format(
        FECHA_INICIO.strftime("%Y-%m-%d"), FECHA_FINAL.strftime("%Y-%m-%d"), numero_domingos, nombre_dia_semana
    ))

if __name__ == "__main__":
    FECHA_INICIO = date(1901,1,1)
    FECHA_FINAL = date(2000,12,31)

    obtenerCantidadDeDomingos(FECHA_INICIO, FECHA_FINAL)


    
            
