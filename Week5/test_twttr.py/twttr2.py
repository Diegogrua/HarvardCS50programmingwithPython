
text = input("Input: ")
vowels = "aeiouAEIOU"
result = ""
print("Ouput: ", end="")

for letter in text:
    if letter not in vowels:

      print(letter + result, end="")

    else:
         continue
print()
