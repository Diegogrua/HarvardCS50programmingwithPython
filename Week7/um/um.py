import re

def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r'\bum\b', s, re.IGNORECASE)
    contador = len(match)
    return contador

if __name__ == "__main__":
    main()




