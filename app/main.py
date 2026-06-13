from tests.test_light_sensor import run as test_light_sensor


def main():

    print("\nO que deseja fazer?\n")

    print("[1] - Testar sensores")

    option = input("\nSelecione uma opção: ")

    if option == "1":

        print("\nQual sensor deseja testar?\n")

        print("[1] - Sensor de luminosidade")

        sensor_option = input("\nSelecione um sensor: ")

        if sensor_option == "1":
            test_light_sensor()

        else:
            print("\nOpção de sensor inválida")

    else:
        print("\nOpção inválida")


if __name__ == "__main__":
    main()