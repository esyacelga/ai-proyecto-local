## Descripción del proyecto árbol K-NEAREST NEIGHBORS

El algoritmo **K-Nearest Neighbors (K-NN)** es un método sencillo pero poderoso utilizado en machine learning para clasificación y regresión. Imagina que tienes un conjunto de puntos en un gráfico, cada uno representando diferentes categorías. Cuando tienes un nuevo punto y quieres saber a qué categoría pertenece, simplemente buscas los **k** puntos más cercanos y ves cuál categoría es la más común entre ellos.

Aquí hay una explicación paso a paso:

1. **Determinar el número ‘k’**: Este es el número de vecinos más cercanos que considerarás. Por ejemplo, si k=3, mirarás los tres vecinos más cercanos.
2. **Medir la distancia**: Calculas la distancia entre tu punto nuevo y todos los otros puntos. La distancia euclidiana es la más común para medir esto.
3. **Identificar los vecinos**: Encuentras los **k** puntos más cercanos a tu punto nuevo.
4. **Clasificación por mayoría de votos**: Para clasificación, el nuevo punto se asigna a la categoría que más se repite entre sus vecinos. Para regresión, se toma un promedio de los valores de los vecinos.

[Es como preguntarle a un grupo de personas cuál es su fruta favorita para adivinar cuál será la fruta favorita de una nueva persona basándote en las respuestas de las personas más cercanas a ella.

Este algoritmo es especialmente útil cuando tus datos son intuitivos y puedes definir una medida de distancia clara. [Sin embargo, puede ser menos efectivo si tienes muchas dimensiones o si tus datos están muy dispersos](https://www.ibm.com/es-es/topics/knn)

Imagina que tienes un montón de amigos viviendo en una vecindad. Cada uno de ellos tiene una etiqueta que indica si les gusta o no el helado.

Ahora, un nuevo vecino se muda y quieres saber si le gustará el helado. ¿Cómo lo averiguarías usando el algoritmo KNN?

1. **Encuentra a los vecinos más cercanos**: Primero, miras a tus vecinos más cercanos. No necesitas ir muy lejos. Digamos que solo miras a tus cinco vecinos más cercanos (por eso se llama K-Nearest Neighbors, donde K es el número de vecinos que miras).
2. **Vota por la mayoría**: Miras si a tus vecinos les gusta o no el helado. Si a la mayoría de ellos les gusta, entonces tú supones que al nuevo vecino también le gustará. Si a la mayoría no le gusta, asumes lo contrario.
3. **Decide si le gustará el helado**: Finalmente, tomas una decisión basada en lo que encontraste con tus vecinos. Si la mayoría de tus vecinos cercanos les gusta el helado, tú asumes que al nuevo vecino también le gustará.

Eso es básicamente lo que hace KNN. Toma una decisión basada en lo que piensan tus vecinos más cercanos. Es simple y efectivo, pero debes elegir un buen número de vecinos (K) y una buena manera de medir la "cercanía" de los vecinos, que se llama función de distancia.


![1715195319067](images/README/1715195319067.png)

### Descripción del Ejemplo

El conjunto de datos describe el nivel jerárquico de empleados en una empresa, junto con sus salarios asociados. Aquí está la descripción de cada columna:

- **Position**: El título o posición del empleado en la empresa.
- **Level**: El nivel jerárquico del empleado, donde 1 es el nivel más bajo y 10 es el nivel más alto.
- **Salary**: El salario asociado con la posición del empleado.

Por ejemplo, la primera fila indica que un "Business Analyst" tiene un nivel de 1 y un salario de 45000. La última fila indica que un "CEO" tiene un nivel de 10 y un salario de 1000000.

Este conjunto de datos proporciona una relación entre el nivel jerárquico y el salario en la empresa, lo que puede ser útil para comprender la estructura salarial y la progresión en la carrera dentro de la empresa.



## Instalación de ambiente

`virtualenv env` : Creacion de ambiente virtual

`source proyecto-a-ejecutar/venv/bin/activate`: Activación de ambiente

`pip3 install -r proyecto-a-ejecutar/requeriments.txt`: Instalacion de dependencias
