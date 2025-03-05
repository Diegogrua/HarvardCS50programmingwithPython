def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
# en esta funcion diremos todas las condiciones que nos piden para validar o invalidar el input
def is_valid(s):
    if 6 >= len(s) >=2 and s[0:2].isalpha() and s.isalnum(): # aca definimos la cantidad de caracteres, y que los s primeros sean letras desde el index cero hasta la 2da letra, el isalnum para los caracteres especiales
        for char in s: #en las tres siguientes lines definimos que despues de las letras, hayan numeros sin estar entre letras
            if char.isdigit(): #para los caracteres que son numeros
                index = s.index(char) # le ponemos un index a los caracteres numeros


                if s[index:].isdigit() and int(char) != 0: # desde el primer caracter numero "index" y el con ":" hasta el final sean numeros y no hayan numeros entre letras. [index:]  dice que hasta el final por dejar los : y espacio
                    return True
                else:
                    return False
        return True



     # si pasa todos los test, retornar True

main()
