class Restaurante:
    restaurante_list = []

    def __init__(self):
        self._name = ''
        self._category = ''
        self._status = False
        Restaurante.restaurante_list.append(self)

    def __str__(self):
        return 'Sem informações' if self.name == '' and self._category == '' else  f'{self._name if self.name != '' else 'Sem informação'} | {self._category if self.category != '' else 'Sem informação'} | {self.status}'

    @classmethod
    def list_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for estabelecimento in cls.restaurante_list:
            print(f'{estabelecimento._name.ljust(25)} | {estabelecimento._category.ljust(25)} | {estabelecimento.status}')
            
    
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