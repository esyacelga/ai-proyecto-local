import unittest

from elasticsearch import Elasticsearch

from app.adapters.persistence.elastic_search_repository import \
    document_exists_match, search_documents_by_text  # Asegúrate de que la importación sea correcta


class TestDocumentExistsReal(unittest.TestCase):

    def setUp(self):
        # Configura la conexión a tu instancia de Elasticsearch
        self.servidor_elastic = "http://192.168.2.232:9200"
        self.index = "documentacion_isspol"  # Usar un índice de prueba
        self.es = Elasticsearch([self.servidor_elastic])

    def test_document_exists_found(self):
        # Variables de prueba
        content = "en un pequeno pueblo al borde de un gran bosque vivia un perro llamado max conocido por su inusual par de botas rojas max no era un perro comun su amor por las aventuras y la exploracion era tan grande que sus botas hechas a medida para sus patas eran su acompanante fiel en cada travesia max habia recibido sus botas de un amable zapatero local que se las hizo para que pudiera explorar sin danarse las patas en los caminos de tierra y piedras del bosque con sus botas puestas max se sentia invencible cada manana al amanecer se preparaba para sus aventuras ajustando sus botas y preparandose para explorar un dia mientras paseaba por el bosque max descubrio un sendero que nunca habia visto antes la curiosidad lo llevo a seguirlo y pronto se encontro frente a una cueva oculta entre las rocas con su valentia habitual max entro en la cueva usando sus botas para navegar por el suelo irregular y las rocas resbaladizas dentro de la cueva max encontro una vieja caja de madera cubierta de polvo usando su hocico y sus patas logro abrir la caja y para su sorpresa encontro un mapa antiguo y una brujula dorada el mapa parecia mostrar la ubicacion de un tesoro escondido en el bosque decidido a descubrir el tesoro max siguio el mapa atravesando rios subiendo colinas y cruzando campos sus botas le daban un firme agarre en cada terreno permitiendole superar todos los obstaculos despues de una larga jornada de exploracion max llego a un claro donde encontro un cofre lleno de piedras preciosas y monedas de oro el tesoro no solo era valioso sino que tambien era un simbolo de la valentia y la perseverancia de max regreso al pueblo con el tesoro y compartio la alegria con los habitantes quienes lo recibieron como un heroe las botas rojas de max se convirtieron en un simbolo de sus aventuras y de la promesa de que con valentia y determinacion siempre hay nuevos horizontes por descubrir cada noche max se acurrucaba en su cama mirando sus botas con gratitud sabia que mientras tuviera esas botas siempre podria seguir sus suenos y explorar lo desconocido y asi en el pequeno pueblo y en el bosque que lo rodeaba las historias de max y sus botas rojas se convirtieron en leyendas de valentia y aventura"
        # Llamar a la función a probar
        result = document_exists_match(content, self.index, self.servidor_elastic)
        # Verificar los resultados
        self.assertTrue(result)

    def test_document_exists_found(self):
        # Variables de prueba
        content = "hay una historia sobre un perro con botas"
        # Llamar a la función a probar
        result = search_documents_by_text(content, self.index, self.servidor_elastic)
        # Verificar los resultados
        self.assertTrue(len(result) > 0)
        for doc in result:
            print(doc)


if __name__ == '__main__':
    unittest.main()
