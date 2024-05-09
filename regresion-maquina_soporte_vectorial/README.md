## Descripción del proyecto soporte vectorial


Las Máquinas de Vectores de Soporte (SVM) son un algoritmo de aprendizaje automático utilizado para problemas de clasificación y regresión. Su objetivo principal es encontrar el mejor "margen" posible que separe las diferentes clases en el espacio de características.

**¿Cómo funciona?**

* **Encontrar el mejor margen**: SVM busca la línea (o plano/híper-plano en dimensiones más altas) que mejor separa las diferentes clases en el espacio de características. Este margen es la distancia entre la línea y los puntos más cercanos de cada clase, que se llaman vectores de soporte.
* **Clasificar nuevos puntos**: Una vez que se encuentra el mejor margen, SVM puede clasificar nuevos puntos al determinar en qué lado de la línea caen. Si un punto está en el lado positivo, se clasifica como una clase, y si está en el lado negativo, se clasifica como la otra clase.

**Características clave:**

* **Margen grande**: SVM busca el margen más grande posible para separar las clases, lo que lo hace robusto y menos propenso al sobreajuste.
* **Kernel trick**: SVM puede manejar problemas no lineales utilizando un truco llamado "kernel trick", que mapea los datos de entrada a un espacio dimensionalmente más alto donde es más fácil encontrar un híper-plano separador.
* **Vectores de soporte**: Los puntos de datos más cercanos a la línea de separación son los vectores de soporte, y determinan la posición y orientación de la línea.

**Ventajas:**

* Eficaz en espacios de alta dimensión.
* Buen rendimiento en conjuntos de datos pequeños a medianos.
* Versátil: puede utilizar diferentes funciones kernel para manejar diferentes tipos de datos.

**Desventajas:**

* No es adecuado para conjuntos de datos muy grandes debido a su tiempo de entrenamiento.
* Sensible a la elección del parámetro de regularización C y la elección del kernel.

**Ejemplo de uso:** Supongamos que tenemos un conjunto de datos de flores con diferentes características (longitud del pétalo, ancho del pétalo, etc.) y queremos clasificarlas en diferentes especies (rosa, tulipán, etc.). Podemos utilizar SVM para encontrar la mejor línea que separe estas especies basadas en sus características, y luego clasificar nuevas flores en función de qué lado de la línea caigan.

En resumen, SVM es un algoritmo poderoso y versátil que se utiliza para clasificar datos al encontrar la mejor línea (o híper-plano) que separa diferentes clases en el espacio de características. Su capacidad para encontrar el mejor margen y manejar problemas no lineales lo convierte en una herramienta valiosa en el aprendizaje automático.


### Descripción del Ejemplo

El archivo CSV Ice Cream Selling es un conjunto de datos que suelen utilizar los principiantes en el aprendizaje automático, especialmente para practicar la regresión polinómica. Es un conjunto de datos sencillo y adecuado para personas que están comenzando su viaje en el aprendizaje automático y desean adquirir experiencia práctica con algoritmos de regresión.

* **fixed\_acidity**: Representa la acidez fija del vino, que es la cantidad de ácidos no volátiles en el vino. Los ácidos fijos son aquellos que no se evaporan fácilmente.
* **volatile\_acidity**: Es la cantidad de ácidos volátiles en el vino, que contribuyen al olor y sabor agrio.
* **citric\_acid**: Indica la cantidad de ácido cítrico presente en el vino, que puede agregar frescura y sabor cítrico.
* **residual\_sugar**: Es la cantidad de azúcar que queda en el vino después de la fermentación. Contribuye al sabor y al cuerpo del vino.
* **chlorides**: Representa la cantidad de cloruros presentes en el vino, que pueden afectar su sabor y aroma.
* **free\_sulfur\_dioxide**: Es la cantidad de dióxido de azufre libre en el vino, que actúa como conservante y antioxidante.
* **total\_sulfur\_dioxide**: Indica la cantidad total de dióxido de azufre presente en el vino, incluyendo tanto el libre como el combinado.
* **density**: Representa la densidad del vino, que está relacionada con su contenido de azúcar y alcohol.
* **pH**: Indica el nivel de acidez o alcalinidad del vino.
* **sulphates**: Es la cantidad de sulfatos presentes en el vino, que pueden contribuir a su estabilidad y sabor.
* **alcohol**: Representa el porcentaje de alcohol en el vino.
* **quality**: Es la calidad del vino, que se clasifica en una escala del 1 al 10, donde 1 indica la calidad más baja y 10 la calidad más alta.

Este conjunto de datos contiene múltiples características químicas y físicas del vino, así como su calidad. Estas características pueden utilizarse para predecir la calidad del vino, lo que hace que este conjunto de datos sea adecuado para problemas de clasificación o regresión, dependiendo de cómo se formule el problema y del tipo de algoritmo que se elija. En este caso, hemos decidido tratar el problema como un problema de clasificación, donde el objetivo es predecir si un vino es de baja, media o alta calidad.

El conjunto de datos está organizado en formato tabular y contiene dos columnas. La primera columna representa los valores de temperatura, que sirven como variable independiente en el análisis de regresión. Los valores de temperatura normalmente se miden en grados Celsius o Fahrenheit. La segunda columna corresponde al número de unidades de helado vendidas, que es la variable dependiente en el análisis de regresión.

Al utilizar este conjunto de datos, los principiantes pueden explorar la relación entre la temperatura y las ventas de helado y aplicar técnicas de regresión polinómica para predecir la cantidad de unidades de helado vendidas en función de la temperatura. Este conjunto de datos ofrece un ejemplo práctico y identificable para comprender e implementar algoritmos de regresión en el aprendizaje automático.

## Instalación de ambiente

`virtualenv env` : Creacion de ambiente virtual

`source proyecto-a-ejecutar/venv/bin/activate`: Activación de ambiente

`pip3 install -r proyecto-a-ejecutar/requeriments.txt`: Instalacion de dependencias
