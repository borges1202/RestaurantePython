class Restaurante:
    restaurante_list = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurante.restaurante_list.append(self)

    def __str__(self):
        return f'{self.name} / {self.category} / {self.active}'

    def list_restaurantes():
        for estabelecimentos in Restaurante.restaurante_list:
            print(estabelecimentos)


rest = Restaurante('Praça', 'Gourmet')
rest1 = Restaurante('Pizza', 'Fast Food')
rest2 = Restaurante('habbis', 'Fast food')

Restaurante.list_restaurantes()
