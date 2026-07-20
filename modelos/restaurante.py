class Restaurante:
    restaurante_list = []

    def __init__(self, name='', category=''):
        self._name = name.title()
        self._category = category.title()
        self._status = False
        Restaurante.restaurante_list.append(self)

    def __str__(self):
        self._name = self._name or 'Sem informação'
        self._category = self._category or 'Sem informação'

        return f'{self.name} | {self.category} | {self.status}'

    @classmethod
    def list_restaurantes(cls):
        for i in cls.restaurante_list:
            i._name = i._name or 'Sem informação'
            i._category = i._category or 'Sem informação'

            print(
                f"Restaurante: {i.name} | "
                f"Categoria: {i.category} | "
                f"Ativo: {i.status}"
            )

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def status(self):
        return '☑' if self._status else '☐'

    @name.setter
    def name(self, name=''):
        if not isinstance(name, str):
            raise ValueError('Coloque apenas texto')
        else:
            self._name = name.title()

    @category.setter
    def category(self, category=''):
        if not isinstance(category, str):
            raise ValueError('Coloque apenas texto')
        else:
            self._category = category.title()

    def switch_state(self):
        self._status = not self._status
