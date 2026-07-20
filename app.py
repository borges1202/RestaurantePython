from modelos.restaurante import Restaurante

rest_japones = Restaurante()
rest_japones.name = 'japa'
rest_japones.category = 'Japonesa'

rest_mexicano = Restaurante()
rest_mexicano.name = 'Mexican food'
rest_mexicano.category = 'Mexicana'
rest_mexicano.switch_state()

rest_praca = Restaurante()
rest_praca.name = ''
rest_praca.category = ''
 

def main():
    Restaurante.list_restaurantes()


if __name__ == '__main__':
    main()
