from tabulate import tabulate
import sys
import csv

if len(sys.argv) == 2:
    if sys.argv[1][-3:] == "csv": # los primeros [1] me dice la posicion del comando y los segundos [csv] para los caracteres dentro
       try:
           with open(sys.argv[1]) as file:
              reader = csv.DictReader(file)
              print(tabulate(reader, headers="keys", tablefmt="grid")) # con el parametro headers="keys" agregamos el encabezado de la tabla
       except FileNotFoundError:
           sys.exit("File noot found")
    else:
            sys.exit("Not a csv file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


