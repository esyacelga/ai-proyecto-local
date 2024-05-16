## Descripción del proyecto regresion logistica

La regresión logística es un modelo de aprendizaje supervisado utilizado para problemas de clasificación binaria, lo que significa que predice la probabilidad de que una muestra pertenezca a una de dos clases. Aunque se llama "regresión", se usa para clasificar, no para predecir valores continuos.

En términos simples:

* Toma un conjunto de características (por ejemplo, edad, género, ingresos) y calcula la probabilidad de que una muestra pertenezca a una de dos clases.
* Utiliza una función logística (también llamada sigmoide) para transformar la combinación lineal de las características en un valor entre 0 y 1, que representa la probabilidad de pertenecer a la clase positiva.
* Si la probabilidad es superior a un umbral (por defecto 0.5), la muestra se clasifica como perteneciente a la clase positiva; de lo contrario, se clasifica como perteneciente a la clase negativa.

En resumen, la regresión logística modela la relación entre las características de entrada y la probabilidad de pertenecer a una clase, y se utiliza para problemas de clasificación binaria. Es simple pero efectiva, y se utiliza ampliamente en aplicaciones donde se necesita predecir categorías.


![1715129767422](images/README/1715129767422.png)

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
