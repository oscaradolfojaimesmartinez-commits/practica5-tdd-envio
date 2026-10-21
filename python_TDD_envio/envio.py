def calcular_envio(peso, tipo):
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que cero")
    if peso > 5:
        costo = 50 + 10 * (peso - 5)
    else:
        costo = 50
    if tipo == "express":
        return costo * 2
    return costo