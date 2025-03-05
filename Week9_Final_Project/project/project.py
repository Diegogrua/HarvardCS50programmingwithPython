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
        now = datetime.now().isoformat()
        if plate not in self.data:
            self.data[plate] = {'name': plate, 'entry_time': now, 'exit_time': None}
        else:
            self.data[plate]['entry_time'] = now
        self.save_data()

    def exit_time(self, plate):

        if plate in self.data and self.data[plate]['entry_time']:
            entry_time = datetime.fromisoformat(self.data[plate]['entry_time'])
            exit_time = datetime.now()

            payment_due, duration = self.calculate_payment(entry_time, exit_time)
            print(f"Hora de salida del vehiculo {plate}, {exit_time}")
            print(f"Tiempo estacionado: {duration}.")
            print(f"Pago a realizar: ${payment_due:.2f}.")

            while True:
                try:
                    payment = int(input("Ingrese el monto a pagar (solo se permiten 5, 10 o 20): "))
                    if payment not in [5, 10, 20]:
                        print("Solo se permiten pagos de 5, 10 o 20.")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un número válido.")

            status, difference = self.validate_payment(payment, payment_due)
            if status == "Falta":
                print(f"Falta dinero. Faltan: ${difference:.2f}.")
            elif status == "Sobra":
                print(f"Pago completado. Su cambio es: ${difference:.2f}.")
            else:
                print("Pago exacto recibido.")

            del self.data[plate]
            self.save_data()
            print(f"Datos del vehículo {plate} eliminados.")
        else:
            print(f"No se encontró la hora de entrada para el vehículo con placa {plate}.")

    def calculate_payment(self, entry_time, exit_time):
        # Calcula la duración
        duration = exit_time - entry_time
        # Costo por hora
        rate_per_hour = 10
        # Cálculo del pago debido
        payment_due = (duration.total_seconds() / 3600) * rate_per_hour
        # Redondear el pago a dos decimales
        payment_due = round(payment_due, 2)
        return payment_due, duration

    def validate_payment(self, payment, payment_due):
        if payment < payment_due:
            return "Falta", payment_due - payment
        elif payment > payment_due:
            return "Sobra", payment - payment_due
        else:
            return "Exacto", 0

def main():
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
