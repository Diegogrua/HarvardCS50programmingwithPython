from datetime import date
import inflect
import sys

p = inflect.engine() # asigno la variable que me convierte numeros a letras

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-") # obtenemos la fecha y aplicamos el split
    except ValueError:
        sys.exit("Invalid Date") # tratar el error como nos lo pidieron
    print(minutes_lived(year, month, day))


def minutes_lived(year, month, day):
    try:
        dt = date(int(year), int(month), int(day)) # ponemos los valores como enteros para poder hacer la operación
    except ValueError:
        return "Invalid Date"
    tday = date.today() # nos da la feca de hoy
    diff = tday - dt
    minutes = int(diff.total_seconds() / 60) # usamos el metodo para segundos y los dividimos en 60 para que de minutos e int para que lo redondee
    msg = p.number_to_words(minutes, andword="") + " minutes"# metodo que convierte a palabras el andword para quitar el and en la salida
    return msg.capitalize()




if __name__ == "__main__":
    main()
