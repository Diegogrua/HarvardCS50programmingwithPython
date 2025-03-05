def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    result = ""
    vowels = ["a", "e", "i", "o", "u"]

    for i in range(len(word)):
        if word[i].lower() not in vowels:
           result += word[i]
    return result


if __name__ == "__main__":
    main()


