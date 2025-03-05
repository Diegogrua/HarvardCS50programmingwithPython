question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?: ")


if question.lower().strip() == "42" or question.lower().strip() == "forty two" or question.lower().strip() == "forty-two":
    print("Yes")
else:
    print("No")

