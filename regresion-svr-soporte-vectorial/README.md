## Descripción del proyecto Support Vector Regression (SVR)

**¿Qué es SVR?**

Support Vector Regression (SVR) es un algoritmo de aprendizaje automático supervisado utilizado para tareas de regresión. A diferencia de otros algoritmos de regresión como la regresión lineal, SVR no busca encontrar una única línea recta que mejor se ajuste a los datos. En cambio, SVR busca **encontrar la función no lineal que mejor se ajusta a los datos**, incluso si esta función es **compleja y curvilínea**.

**¿Cómo funciona SVR?**

SVR funciona mapeando los datos de entrada a un espacio de dimensión superior y buscando un **hiperplano** en este espacio que **separe los datos en dos grupos**. Este hiperplano representa la función de regresión que SVR utiliza para predecir valores para nuevos datos.

Los puntos de datos que se encuentran más cerca del hiperplano se denominan **vectores de soporte**. Estos vectores de soporte son cruciales para definir el hiperplano y, por lo tanto, para el rendimiento del modelo SVR.

**¿Cuáles son las ventajas de SVR?**

* **Flexibilidad:** SVR puede adaptarse a funciones no lineales complejas, lo que lo hace adecuado para una amplia gama de problemas de regresión.
* **Robustez:** SVR es **menos sensible a valores atípicos** en los datos que otros algoritmos de regresión.
* **Alta precisión:** SVR puede lograr un alto nivel de precisión en muchos problemas de regresión.

**¿Cuáles son las desventajas de SVR?**

* **Complejidad computacional:** SVR puede ser **computacionalmente costoso** de entrenar, especialmente para conjuntos de datos grandes.
* **Selección de kernel:** La elección del kernel adecuado para SVR puede ser difícil y puede afectar significativamente el rendimiento del modelo.
* **Interpretación:** Puede ser difícil **interpretar** el modelo SVR, ya que la función de regresión es una función no lineal compleja.

**¿En qué casos se utiliza SVR?**

SVR se utiliza en una amplia variedad de aplicaciones, incluyendo:

* **Predicción de precios:** SVR se puede utilizar para predecir el precio de acciones, bienes raíces u otros activos.
* **Demanda de productos:** SVR se puede utilizar para predecir la demanda de un producto o servicio.
* **Calidad del producto:** SVR se puede utilizar para predecir la calidad de un producto en función de sus características.
* **Detección de anomalías:** SVR se puede utilizar para detectar anomalías en los datos, como fraudes o fallas en equipos.

**En resumen, SVR es un algoritmo de aprendizaje automático poderoso y versátil que se puede utilizar para resolver una amplia gama de problemas de regresión. Sin embargo, es importante tener en cuenta sus limitaciones, como la complejidad computacional y la dificultad de interpretación.**

**Si tienes alguna otra pregunta sobre SVR o sobre Data Science en general, no dudes en contactarme.**

### Descripción del Ejemplo

El conjunto de datos describe características de usuarios y si realizaron una compra o no. Aquí está la descripción de cada columna:

* **User ID**: Identificación única de cada usuario.
* **Gender**: Género del usuario (Masculino o Femenino).
* **Age**: Edad del usuario.
* **EstimatedSalary**: Salario estimado del usuario.
* **Purchased**: Indicador binario que muestra si el usuario realizó una compra (1) o no (0).

Por ejemplo, el primer usuario es un hombre de 19 años con un salario estimado de 19000, y no realizó una compra (Purchased=0). El segundo usuario es un hombre de 35 años con un salario estimado de 20000 y tampoco realizó una compra. Y así sucesivamente para cada fila en el conjunto de datos.

## Instación de ambiente

`virtualenv env` : Crecion de ambiente

`source proyecto-a-ejecutar/venv/bin/activate`: Activación de ambiente

`pip3 install -r proyecto-a-ejecutar/requeriments.txt`: Instalacion de dependencias
