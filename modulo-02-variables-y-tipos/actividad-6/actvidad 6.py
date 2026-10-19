

NOMBRE_SENSOR = "distancia"
UNIDAD = "cm"

distancia_texto = "45"
bateria = 80
distancia = float(distancia_texto)

for nombre, valor in [
    ("NOMBRE_SENSOR", NOMBRE_SENSOR),
    ("UNIDAD", UNIDAD),
    ("distancia_texto", distancia_texto),
    ("bateria", bateria),
    ("distancia", distancia),
]:
    print(nombre, valor, type(valor).__name__)


