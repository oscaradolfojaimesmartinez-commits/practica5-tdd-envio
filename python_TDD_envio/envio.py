def calcular_envio(peso, tipo):
    if tipo == "express":
        return 100
    if peso > 5:
        return 50 + 10 * (peso - 5)
    return 50