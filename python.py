class Motocicleta():
    # atributos de clase
    estado = "nueva"
    motor = False
    # métodos

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_max, peso, combustible_maximo):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_max = velocidad_max
        self.peso = peso
        self.combustible_maximo = combustible_maximo

    def arrancar(self):
        if self.motor:
            print("Se giró la llave, el motor está encendido")
        else:
            print("El motor está encendido y ruge como león")

    def detener(self):
        if self.motor:
            print("Se empieza a detener el motor")
        else:
            print("El motor ya está detenido por completo")

    def verificar_precio(self):
        print(
            f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} $.")

    def comprobar_deposito(self):
        print(f"--->REPORTE DE DEPÓSITO DE {self.marca} {self.modelo}<---")
        print(f"El depósito tiene {self.combustible_litros} litros.")
        print(
            f"La capacidad máxima del tanque de combustible es de {self.combustible_maximo}.")
        print(
            f"Faltan {self.combustible_maximo - self.combustible_litros} litros para llenar el depósito.")
        print(f"--->FIN DEL REPORTE<---\n")

    def repostar(self):
        while True:
            self.repostar_litros = float(
                input("Por favor, introduzca la cantidad de litros que desea repostar:\n"))
            if self.combustible_litros + self.repostar_litros <= self.combustible_maximo:
                print("Repostaje exitoso.")
                print(f"Se han repostado {self.repostar_litros} litros.")
                self.combustible_litros += self.repostar_litros
                print(
                    f"El depósito tiene {self.combustible_litros} litros de combustible.")
                break
            else:
                print("No cabe tanto combustible. ¿Quieres encharcar el concesionario?")


Yamaha = Motocicleta("Verde", "45663-FHDY", 10, 2, "Yamaha",
                     "YZF-R1", "20/02/2020", 288, 199, 14)

Aprilia = Motocicleta(
    velocidad_max=300,
    matricula="74874-VSF",
    numero_ruedas=2,
    combustible_litros=0,
    marca="aprilia",
    color="rojo",
    fecha_fabricacion="12/07/2019",
    modelo="RSV4 RR 1000",
    peso=202,
    combustible_maximo=20
)

Yamaha.precio = 20000
