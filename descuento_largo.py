# Urban Routes — descuento por viaje largo
# Regla de negocio: los viajes de 5 km o más tienen un 15 % de descuento.


def aplicar_descuento_largo(distancia_km, tarifa):
    if distancia_km > 5:
        tarifa = tarifa - tarifa * 15 / 100
    return tarifa


print("4 km:", aplicar_descuento_largo(4, 100), "| esperado: 100")
print("5 km:", aplicar_descuento_largo(5, 100), "| esperado: 85.0")
print("7 km:", aplicar_descuento_largo(7, 100), "| esperado: 85.0")
