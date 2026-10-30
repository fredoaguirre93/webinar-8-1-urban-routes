# Urban Routes — cálculo de la tarifa final de un viaje con código promocional
# Caso: viaje de 8 km, tarifa base de $30, $12 por km y promo del 10 %.
# Resultado esperado: 113.4


def calcular_tarifa_final(distancia_km, tarifa_base, tarifa_por_km, promo_pct):
    total = tarifa_base + distancia_km * tarifa_por_km
    total_con_descuento = total - total * promo_pct / 100
    return total


tarifa = calcular_tarifa_final(8, 30, 12, 10)
print("Tarifa final:", tarifa)
print("Esperado: 113.4")
