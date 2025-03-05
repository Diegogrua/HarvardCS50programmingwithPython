def values():
    operation = input("type an operation: ")
    x, y, z = operation.split(" ")
    new_x = float(x)
    new_z = float(z)
    return new_x, y, new_z

def calculator():
    new_x, y, new_z = values()
    if y == "+":
       print(new_x + new_z)
    elif y == "-":
       print(new_x - new_z)
    elif y == "*":
       print(new_x * new_z)
    elif y == "/":
       result = new_x / new_z
       print(round(result,1))
    else:
        print("try again")

calculator()

