# Práctica 5: Desarrollo de una funcionalidad siguiendo TDD
Modelado y Programación, Facultad de Ciencias, UNAM

## **Integrantes:** 
    - Ruth Sarai Guadalupe Balanzar
    - Alondra Campos Mendoza
    - Edith Alejandra Mendoza Aragón
    - Evelyn Vianey Mondragón Ceballos
    - Oscar Adolfo Jaimez Martinez
    - Jorge Guadalupe Mancilla Laguna

## Introducción

En esta práctica se desarrolló una función que calcula el costo de envío de un paquete, pero el objetivo principal no fue solo obtener el resultado correcto, sino aprender a construir el programa con **Test-Driven Development (TDD)**.

TDD consiste en escribir primero una prueba para el comportamiento que se quiere lograr y programar después, avanzando en ciclos muy pequeños:

1. **ROJO:** se escribe una prueba para un comportamiento nuevo y se ejecuta. Debe fallar, porque todavía no existe el código que la satisface. Ver el fallo confirma que la prueba realmente verifica algo.
2. **VERDE:** se escribe la cantidad mínima de código que hace pasar la prueba, y se ejecutan todas las pruebas anteriores para comprobar que nada se rompió.
3. **REFACTORIZACIÓN:** con todo en verde, se mejora la estructura del código (nombres, constantes, código repetido) sin cambiar su comportamiento. Las pruebas son la red de seguridad que avisa si algo cambió.

De esta forma el programa no se diseña todo de golpe: cada prueba agrega una regla y obliga a tomar una pequeña decisión de diseño.

## El problema

La función `calcular_envio(peso, tipo)` recibe el peso del paquete en kilogramos y el tipo de envío, y devuelve su costo con estas reglas:

- **Envío estándar de hasta 5 kg:** costo fijo de $50.
- **Más de 5 kg:** $50 más $10 por cada kilogramo adicional sobre los 5 kg.
- **Envío exprés:** cuesta el doble de lo que costaría el mismo paquete con envío estándar.
- **Peso inválido:** el peso debe ser mayor que cero; si es cero o negativo se lanza un `ValueError`.
- **Tipo inválido:** solo se aceptan `"estandar"` y `"express"`; cualquier otro valor lanza un `ValueError`.

Ejemplos:

| Llamada | Resultado | Por qué |
|---|---|---|
| `calcular_envio(3, "estandar")` | 50 | Hasta 5 kg es costo fijo |
| `calcular_envio(5, "estandar")` | 50 | El límite exacto todavía no cobra extra |
| `calcular_envio(7, "estandar")` | 70 | 50 + 10 × (7 − 5) |
| `calcular_envio(3, "express")` | 100 | El doble de 50 |
| `calcular_envio(7, "express")` | 140 | El doble de 70 |
| `calcular_envio(0, "estandar")` | `ValueError` | El peso debe ser mayor que cero |
| `calcular_envio(3, "urgente")` | `ValueError` | Tipo de envío no válido |

## Cómo se desarrolló

El trabajo se hizo en cinco ciclos. Cada uno empezó con una prueba que falló y terminó con el cambio mínimo para que pasara:

1. **Envío estándar pequeño.** La primera prueba esperaba que 3 kg en estándar costaran 50. Como la función todavía no existía, se creó primero un esqueleto que devolvía 0, para que la prueba fallara por el resultado y no por un error de importación. Después bastó con devolver 50.
2. **Paquete pesado.** La prueba de 6 kg (debe costar 60) hizo fallar el `return 50`, y eso obligó a introducir la fórmula del exceso sobre 5 kg. Luego se agregaron las pruebas de 5 kg exactos y de 7 kg. Estas dos pasaron de inmediato: sirven para proteger el límite y la fórmula, no para guiar código nuevo.
3. **Envío exprés.** Primero se probó un exprés pequeño (3 kg → 100), que se resolvió de forma mínima. Después, el exprés pesado (7 kg → 140) hizo fallar esa solución y obligó a un mejor diseño: calcular primero un costo base y duplicarlo si el envío es exprés, sin repetir la fórmula del exceso.
4. **Validación del peso.** Las pruebas de peso cero y negativo fallaron porque la función devolvía un costo en lugar de reportar un error. Se resolvió con una validación al inicio de la función, antes de calcular nada.
5. **Tipo de envío inválido.** Hasta ese momento cualquier tipo distinto de `"express"` se trataba como estándar, así que `"urgente"` devolvía 50. La prueba nueva obligó a rechazar los tipos desconocidos en lugar de adivinar qué quiso decir el usuario.

Al final se hizo una **refactorización**, descrita más abajo.

## Las pruebas

El archivo `test_envio.py` contiene 9 pruebas con `unittest`, que cubren los casos normales, los límites y los casos inválidos:

| Prueba | Qué comprueba |
|---|---|
| `test_estandar_menor_a_5kg_cuesta_50` | Estándar de 3 kg |
| `test_estandar_exactamente_5kg_cuesta_50` | Límite exacto de 5 kg |
| `test_estandar_6kg_cuesta_60` | Primer valor por encima del límite |
| `test_estandar_7kg_cuesta_70` | Fórmula con más de un kilogramo de exceso |
| `test_express_menor_a_5kg_cuesta_100` | Exprés pequeño |
| `test_express_mayor_a_5kg_cuesta_140` | Exprés pesado |
| `test_peso_cero_lanza_error` | Peso igual a cero |
| `test_peso_negativo_lanza_error` | Peso negativo |
| `test_tipo_invalido_lanza_error` | Tipo de envío inexistente |

Ninguna prueba se borró ni se modificó para adaptarla al código: el código se fue ajustando a las pruebas, no al revés.

## Decisiones de diseño

- **Errores con `ValueError`.** Para peso y tipo inválidos se usa una excepción en lugar de devolver un valor especial, así el error no se confunde con un costo válido.
- **La validación va antes del cálculo.** Primero se revisa el peso, luego el tipo, y solo después se calcula el costo. Así no se hace trabajo con datos inválidos.
- **Un diccionario para los tipos.** Después de la refactorización, `TIPOS` asocia cada tipo con su multiplicador (`estandar: 1`, `express: 2`). El mismo diccionario sirve para validar el tipo y para calcular el costo, y agregar un tipo nuevo ya no requiere tocar la fórmula.
- **Constantes con nombre.** Los valores 5, 50 y 10 se convirtieron en `PESO_LIMITE`, `COSTO_ESTANDAR` y `COSTO_KILAD`, para que las reglas de negocio se lean sin adivinar qué significa cada número.
- **Un solo cálculo.** El costo adicional se obtiene con `max(0, peso - PESO_LIMITE)`, lo que elimina la condición entre paquete ligero y pesado. La fórmula también admite pesos decimales, aunque las pruebas solo usan enteros.

## Refactorización

Una vez que las 9 pruebas estaban en verde se mejoró la estructura de `envio.py` sin agregar requisitos: se introdujeron las constantes, el diccionario `TIPOS` y el cálculo con `max(...)`. Se ejecutaron de nuevo todas las pruebas y siguieron pasando (evidencia en `evidencias/refactor_verde.txt`), lo que confirma que el comportamiento observable no cambió. El detalle está en `registro_ciclos.md`.

## Cómo ejecutar las pruebas

Se necesita Python 3. No hay que instalar nada, porque `unittest` viene incluido.

```bash
cd python_TDD_envio
python -m unittest -v
```

Deben pasar las 9 pruebas y la salida debe terminar con `OK`.

## Estructura del repositorio

```
.
├── README.md
├── registro_ciclos.md      # preguntas previas, tabla de ciclos, refactorización y reflexión final
├── evidencias/             # salida de las pruebas en cada ROJO y VERDE
└── python_TDD_envio/
    ├── envio.py            # función calcular_envio
    └── test_envio.py       # pruebas
```

## Cómo revisar la evidencia del proceso

- **Historial de Git.** Cada paso tiene su propio commit, con mensajes del tipo `ROJO ciclo N: ...` y `VERDE ciclo N: ...`, además de los de la refactorización. Con `git log --oneline` se ve el orden real: en cada ciclo la prueba aparece antes que la solución.
- **Carpeta `evidencias/`.** Guarda la salida de ejecución de cada ROJO y VERDE (por ejemplo `ciclo3_rojo_pesado.txt` y `ciclo3_verde_pesado.txt`). En los archivos de ROJO se ve la prueba fallando con su mensaje de error, y en los de VERDE, todas las pruebas pasando.
- **`registro_ciclos.md`.** Contiene las respuestas previas, la tabla de ciclos con la prueba agregada, el motivo del fallo y el cambio realizado, la descripción de la refactorización y la reflexión final.