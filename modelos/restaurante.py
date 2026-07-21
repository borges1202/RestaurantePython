from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurante_list = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._status = False
        self._assessment_list = []
        Restaurante.restaurante_list.append(self)

    def __str__(self):
        str_name = self._name or 'Sem informação'
        str_category = self._category or 'Sem informação'

        return f'{str_name} | {str_category} | {self.status}'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name=''):
        if not isinstance(name, str):
            raise ValueError('Coloque apenas texto')
        else:
            self._name = name.title()

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category=''):
        if not isinstance(category, str):
            raise ValueError('Coloque apenas texto')
        else:
            self._category = category.title()

    @property
    def status(self):
        return '☑' if self._status else '☐'

    @classmethod
    def list_restaurantes(cls):
        for i in cls.restaurante_list:
            iname = i._name or 'Sem informação'
            icategory = i._category or 'Sem informação'

            print(
                f"Restaurante: {iname} | "
                f"Categoria: {icategory} | "
                f"Ativo: {i.status} | "
                f"Avaliação: {i.average()}"
            )

    def switch_state(self):
        self._status = not self._status
        
    def assessment(self, client, notation):
        if notation < 0 or notation > 5:
            raise ValueError('Coloque um valor válido')
        else:
            assessment = Avaliacao(client, notation)
            self._assessment_list.append(assessment)

    
    def average(self):
        return Avaliacao.average_rating(self)

