def main():
    greating = input("type your great: ")
    value = value(greating)
    print("$" + value)

def value(greating):
    greating = greating.lower().strip()
    if "hello" in greating:
        return 0
    elif "h" == greating[0]:
        return 20
    else:
         return 100


if __name__ == "__main__":
    main()




