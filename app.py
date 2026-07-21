from modelos.restaurante import Restaurante


rest_japones = Restaurante("Japa", "Japonesa")
rest_japones.assessment("João", 5)
rest_japones.assessment("Maria", 4)
rest_japones.switch_state()

rest_mexicano = Restaurante("Mexican Food", "Mexicana")
rest_mexicano.assessment("Arthur", 3)
rest_mexicano.assessment("Giovanna", 2)


def main():
    Restaurante.list_restaurantes()


if __name__ == "__main__":
    main()