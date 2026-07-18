class Restaurante:
    restaurante_list = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.title()
        self._status = False
        Restaurante.restaurante_list.append(self)

    def __str__(self):
        return f'{self._name} | {self._category}'

    @classmethod
    def list_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for estabelecimentos in cls.restaurante_list:
            print(f'{estabelecimentos._name.ljust(25)} | {estabelecimentos._category.ljust(25)} | {estabelecimentos.status}')
            
    @property
    def status(self):
        return '☑' if self._status else '☐'
    
    def switch_state(self):
        self._status = not self._status


rest = Restaurante('Praça', 'Gourmet')
rest1 = Restaurante('Pizza', 'fast food')
rest2 = Restaurante('habbis', 'Fast food')

Restaurante.list_restaurantes()

