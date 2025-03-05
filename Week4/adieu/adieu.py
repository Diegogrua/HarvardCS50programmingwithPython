import inflect

p = inflect.engine()
text = ["Adieu", "adieu"]
while True:
    try:
       names = input("name: ")
    except EOFError:
        print()
        break
    text.append(names)
text[2] = "to " + text[2]

if len(text) == 3:
    new_text = p.join(text, conj='')
elif len(text) == 4:
    new_text = p.join(text, final_sep='')
else:
    new_text = p.join(text)

print(new_text)


