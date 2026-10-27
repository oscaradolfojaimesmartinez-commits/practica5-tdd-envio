# Práctica 5: Desarrollo de una funcionalidad siguiendo TDD
Modelado y Programación

## **Integrantes:**
    - Ruth Sarai Guadalupe Balanzar
    - Alondra Campos Mendoza
    - Edith Alejandra Mendoza Aragón
    - Evelyn Vianey Mondragón Ceballos
    - Oscar Adolfo Jaimez Martinez
    - Jorge Guadalupe Mancilla Laguna


## 1. Antes de programar

1. **¿Qué significa que una prueba esté en estado ROJO?**
Que la prueba se ejecutó y falló, porque el comportamiento que describe todavía no está implementado. Confirma que la prueba realmente verifica algo.

2. **¿Qué debe hacerse para llegar a VERDE?**
Escribir la cantidad mínima de código para que la prueba nueva pase, sin romper las pruebas anteriores.

3. **¿Qué diferencia existe entre agregar funcionalidad y refactorizar?**
Agregar funcionalidad cambia el comportamiento del programa y siempre empieza con una prueba que falla. Refactorizar mejora la estructura del código (nombres, constantes, duplicación) sin cambiar su comportamiento, y se hace con todas las pruebas en verde.

4. **¿Por qué en TDD no conviene implementar todos los requisitos desde el inicio?**
Porque se escribe código que ninguna prueba justifica, se pierde la guía de las pruebas y los errores son más difíciles de ubicar. Con ciclos pequeños cada cambio es fácil de revisar.

## 2. Registro de ciclos

| Ciclo | Prueba agregada | Por qué falló (ROJO) | Cambio realizado (VERDE) | Resultado |
|---|---|---|---|---|
| 1 | test_estandar_menor_a_5kg_cuesta_50 | El esqueleto devolvía 0 (0 != 50) | return 50 | 1 prueba en verde |
| 2 | test_estandar_6kg_cuesta_60; después 5 kg exactos y 7 kg | Devolvía 50 fijo (50 != 60) | Si peso > 5: 50 + 10 * (peso - 5) | 4 pruebas en verde. Las de 5 kg y 7 kg pasaron de inmediato |
| 3 | test_express_menor_a_5kg_cuesta_100; luego test_express_mayor_a_5kg_cuesta_140 | 50 != 100; luego 100 != 140 | Primero return 100 para exprés; después se calculó un costo base y se duplicó | 6 pruebas en verde |
| 4 | test_peso_cero_lanza_error; test_peso_negativo_lanza_error | ValueError not raised | Validar peso <= 0 al inicio de la función | 8 pruebas en verde |
| 5 | test_tipo_invalido_lanza_error | ValueError not raised | Validar que el tipo sea estandar o express | 9 pruebas en verde |

Notas:
- Ciclo 1: el primer ROJO falló por un error de importación (el archivo del esqueleto se guardó con nombre incorrecto). Se corrigió el nombre del archivo y se repitió el ROJO, que ya falló por 0 != 50. Ambos commits están en el historial.
- Ciclo 2: las pruebas de 5 kg y 7 kg pasaron sin cambiar el código; sirven para proteger el límite y la fórmula.
- Ciclo 3: al agregar el exprés pesado se evitó duplicar la fórmula del exceso, calculando primero el costo base.
- En todos los ciclos se ejecutaron todas las pruebas anteriores y siguieron pasando.
- La evidencia de cada ejecución está en la carpeta evidencias/.

## 3. Refactorización

Commits: `fa25846` y `045730d` (Refactorizacion de envio.py). No se agregaron requisitos ni se modificaron las pruebas.

Cambios realizados en `envio.py`:
- Constantes con nombre para los valores fijos: `PESO_LIMITE` (5), `COSTO_ESTANDAR` (50) y `COSTO_KILAD` (10, costo por kilogramo adicional).
- El diccionario `TIPOS` asocia cada tipo de envío con su multiplicador (estandar: 1, express: 2). Se usa tanto para validar el tipo como para calcular el costo, así desaparecen las condiciones por tipo.
- El costo adicional por peso se calcula con `max(0, peso - PESO_LIMITE)`, lo que elimina el if/else entre paquete ligero y pesado.
- La función termina con un solo cálculo y un solo return.

Verificación: las 9 pruebas pasaron antes (evidencias/ciclo5_verde.txt) y después de refactorizar (evidencias/refactor_verde.txt), por lo que el comportamiento observable no cambió.

## 4. Reflexión final (máximo 5 líneas)

1. **¿En qué momento una prueba te obligó a modificar el diseño?**
La prueba del exprés pesado (7 kg) obligó a dejar el costo fijo de 100 y calcular primero un costo base para después duplicarlo.

2. **¿Qué ventaja encontraste al ejecutar todas las pruebas después de cada cambio?**
Permite identificar errores al instante en el lugar exacto donde ocurren, reduciendo el tiempo de depuración al asegurarme de que cada pequeño cambio mantiene la integridad de todo el sistema.

3. **¿Qué parte del proceso TDD te resultó más difícil?**
Mantener la disciplina de escribir solo la prueba mínima e implementar únicamente el código necesario para pasar a verde, resistiendo la tentación de anticipar casos o validar todo desde el inicio.