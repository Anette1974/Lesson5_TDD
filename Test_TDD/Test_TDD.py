def add(x, y):
    return x + y

def test_add():
    expected = 3
    actual = add(1, 2)
    assert actual == expected