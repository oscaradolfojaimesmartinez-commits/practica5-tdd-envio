TIPOS = {"estandar":1, "express":2}
PESO_LIMITE = 5 
COSTO_ESTANDAR = 50
COSTO_KILAD = 10

def calcular_envio(peso, tipo):
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que cero")

    if tipo not in TIPOS:
        raise ValueError("Tipo de envío inválido")

    calcular_peso_adicional = COSTO_KILAD * max(0, peso - PESO_LIMITE) 
    costo = (COSTO_ESTANDAR + calcular_peso_adicional) * TIPOS[tipo]

        
    return costo
