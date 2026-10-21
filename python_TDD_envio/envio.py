def calcular_envio(peso, tipo):
    if peso > 5:
        return 50 + 10 * (peso - 5)
    return 50