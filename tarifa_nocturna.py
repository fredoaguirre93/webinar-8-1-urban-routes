# Archivo agregado por el tutor durante el webinario 8.1
# Reto para casa: agrega llamadas con las horas 22 y 5, predice el resultado y ejecútalo.
# Regla: entre las 22:00 y las 6:00 se aplica un recargo nocturno del 20 %.


def aplicar_recargo_nocturno(tarifa, hora):
    if hora >= 22 or hora < 6:
        tarifa = tarifa + tarifa * 20 / 100
    return tarifa


print("23 h:", aplicar_recargo_nocturno(100, 23), "| esperado: 120.0")
print("6 h:", aplicar_recargo_nocturno(100, 6), "| esperado: 100")
