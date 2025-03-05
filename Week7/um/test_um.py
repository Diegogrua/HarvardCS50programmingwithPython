from um import count

def main():
    test_count()
    test_count1()
    test_count2()

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um hello, um, world") == 2

def test_count1():
    assert count("um, um. yummy") == 2


def test_count2():
    assert count("Um, thanks for the album.") == 1
    assert count("yumm yum, um, hello um") == 2


if __name__== "__main__":
    main()



