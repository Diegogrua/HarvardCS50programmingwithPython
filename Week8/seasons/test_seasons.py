from seasons import minutes_lived

def main():
    test_1()
    test_2()
   


def test_1():
    assert minutes_lived(25, 2, 1993) == "Invalid Date"

def test_2():
    assert minutes_lived(23, 1, 2000) == "Invalid Date"

if __name__ == "__main__":
    main()



