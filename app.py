from modelos.restaurante import Restaurante

rest_japones = Restaurante("", "japones")
rest_japones.assessment('joao', 10)
rest_japones.assessment('joao', 5)
rest_japones.assessment('joao', 3)
rest_japones.assessment('jao', 2)
rest_japones.average()


def main():
    Restaurante.list_restaurantes()


if __name__ == "__main__":
    main()
