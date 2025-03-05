import json
import sys
from datetime import datetime

DATA_FILE = 'data.json'

class Vehicle:
    def __init__(self, plate):
        self.plate = plate
        self.entry_time = None
        self.exit_time = None

    def __str__(self):
        return f"Plate {self.plate}, Entry Time: {self.entry_time}, Exit Time: {self.exit_time}"

class ValetParking:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(DATA_FILE, 'w') as file:
            json.dump(self.data, file, indent=4)

    def enter_time(self, plate):
        # registra la hora de entrada del vehiculo.
        now = datetime.now().isoformat() # isoformat el formato en que se muestra la hora
        if plate not in self.data:
            self.data[plate] = {'name': plate, 'entry_time': now, 'exit_time': None} # si la placa no esta crea una entrada nueva
        else:
            self.data[plate]['entry_time'] = now # si ya esta en los datos solo actualiza la hora de entrada
        self.save_data() #  guarda los datos actualizados
        print(f"hora de entrada para el vehiculo {plate}, hour {now}.")

    def exit_time(self, plate):
        #registra la hora de salida de el vehiculo y el tiempo estacionado
        now = datetime.now().isoformat()
        if plate in self.data and self.data[plate]['entry_time']:
           entry_time = datetime.fromisoformat(self.data[plate]['entry_time']) # calculo de tiempo
           exit_time = datetime.now() # aca calcula el tiempo con el actual
           duration = exit_time - entry_time
        # costo de tiempo
           rate_per_hour = 10
           payment_due = (duration.total_seconds() / 3600) * rate_per_hour
           self.data[plate]['exit_time'] = now
           self.save_data()
           print(f"Hora de salida del vehiculo {plate} ({self.data[plate]}).")
           print(f"Tiempo estacionado: {duration}.")
           print(f"pago a realizar: ${payment_due:.2f}.")

          # eliminar la entrada del vehiculo al calcular el pago
           del self.data[plate]
           self.save_data()
           print(f"Datos del vehículo {plate} eliminados.")
        else:
            print(f"No se encontro la hora de entrada {plate}.")

def main():
    # manejo de los comandos
    if len(sys.argv) < 2:
        print("uso: python project.py [entra/sale]")
        sys.exit(1)

    command = sys.argv[1]

    manager = ValetParking()

    if command == 'entra':
        plate = input("Ingrese el numero de la placa: ")
        manager.enter_time(plate)
    elif command == 'sale':
        plate = input("Ingrese el numero de la placa: ")
        manager.exit_time(plate)
    else:
        print("comando no reconocido. Usa: 'entra' o 'sale'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
