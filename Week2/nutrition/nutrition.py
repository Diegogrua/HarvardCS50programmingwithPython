fruits = {
     "apple": 130,
     "avocado": 50,
     "banana": 110,
     "c0antaloupe": 50,
     "grapefruit" : 60,
     "grapes" : 90,
     "honeydew": 50,
     "sweet cherries": 100,
     "kiwifruit" : 90,
     "pear": 100,
}



fruit = input("Fruit: ").lower()

if fruit in fruits:
    print("Calories: ", fruits[fruit])

