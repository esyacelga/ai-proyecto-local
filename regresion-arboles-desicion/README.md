## Descripción del proyecto árbol de decisión

Los árboles de decisión son modelos de aprendizaje automático que se utilizan tanto en problemas de clasificación como de regresión. Son una representación gráfica de un conjunto de reglas de decisión que se utilizan para predecir la etiqueta de una muestra.

En un árbol de decisión:

1. **Nodos**: Cada nodo representa una característica en los datos y una pregunta asociada con esa característica. Por ejemplo, "¿La edad del cliente es mayor que 30 años?"
2. **Aristas**: Las aristas conectan los nodos y representan las posibles respuestas a la pregunta del nodo padre. Por ejemplo, "Sí" y "No".
3. **Hoja**: Los nodos hoja son los nodos finales del árbol y representan las etiquetas de clasificación o los valores de regresión predichos para una muestra.

El proceso de construcción de un árbol de decisión implica dividir repetidamente el conjunto de datos en subconjuntos más pequeños basados en las características, de modo que las muestras en cada subconjunto sean lo más homogéneas posible en términos de la variable objetivo (clasificación o regresión). Esto se hace seleccionando la característica y el punto de corte que mejor separan las clases en cada paso.

Los árboles de decisión son interpretables y fáciles de entender, ya que reflejan un conjunto de reglas de decisión intuitivas. Sin embargo, pueden ser propensos a sobreajustarse a los datos de entrenamiento si no se controlan correctamente. Para mitigar esto, se pueden usar técnicas como la poda del árbol, la limitación de la profundidad del árbol o el uso de métodos ensemble como Random Forest o Gradient Boosting.


Supongamos que tenemos un conjunto de datos con dos características: "Edad" y "Ingresos", y queremos predecir si una persona comprará un producto (1) o no (0).

Primero, tenemos el siguiente conjunto de datos:


| Edad | Ingresos | Compra |
| ---- | -------- | ------ |
| 20   | 20000    | 0      |
| 25   | 35000    | 0      |
| 30   | 40000    | 1      |
| 35   | 60000    | 1      |
| 40   | 80000    | 1      |


Ahora, vamos a construir un árbol de decisión paso a paso:

1. **Nodo raíz**: Calculamos la mejor división para el nodo raíz. En este caso, podríamos elegir dividir por edad o ingresos. Supongamos que elegimos dividir por edad si es menor o igual a 30 años.
2. **Nodo 1 (Edad <= 30)**:

   * Si Edad <= 30:
     * **Sí**: 2 muestras (1 compra, 1 no compra)
     * **No**: 1 muestra (no compra)

   En este nodo, si la edad es menor o igual a 30 años, preguntamos sobre ingresos.
3. **Nodo 2 (Ingresos <= 37500)**:

   * Si Ingresos <= 37500:
     * **Sí**: 1 muestra (no compra)
     * **No**: 2 muestras (1 compra, 1 no compra)

   En este nodo, si los ingresos son menores o iguales a 37500, la persona probablemente no comprará.
4. **Nodo 3 (Ingresos > 37500)**:

   * Si Ingresos > 37500:
     * **Sí**: 1 muestra (compra)
     * **No**: 1 muestra (compra)

   En este nodo, si los ingresos son mayores a 37500, la persona probablemente comprará.

Este sería un árbol de decisión simple para este conjunto de datos. La construcción del árbol implica seleccionar la característica y el punto de división que mejor separa las clases en cada paso. Una vez construido, podemos usar este árbol para predecir si una nueva persona comprará o no un producto, siguiendo las preguntas en los nodos del árbol.


### Descripción del Ejemplo

El archivo CSV Ice Cream Selling es un conjunto de datos que suelen utilizar los principiantes en el aprendizaje automático, especialmente para practicar la regresión polinómica. Es un conjunto de datos sencillo y adecuado para personas que están comenzando su viaje en el aprendizaje automático y desean adquirir experiencia práctica con algoritmos de regresión.

El conjunto de datos está organizado en formato tabular y contiene dos columnas. La primera columna representa los valores de temperatura, que sirven como variable independiente en el análisis de regresión. Los valores de temperatura normalmente se miden en grados Celsius o Fahrenheit. La segunda columna corresponde al número de unidades de helado vendidas, que es la variable dependiente en el análisis de regresión.

Al utilizar este conjunto de datos, los principiantes pueden explorar la relación entre la temperatura y las ventas de helado y aplicar técnicas de regresión polinómica para predecir la cantidad de unidades de helado vendidas en función de la temperatura. Este conjunto de datos ofrece un ejemplo práctico y identificable para comprender e implementar algoritmos de regresión en el aprendizaje automático.

## Instalación de ambiente

`virtualenv env` : Creacion de ambiente virtual

`source proyecto-a-ejecutar/venv/bin/activate`: Activación de ambiente

`pip3 install -r proyecto-a-ejecutar/requeriments.txt`: Instalacion de dependencias
