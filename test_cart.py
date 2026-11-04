from cart import Cart

def test_add_updates_total():
    c = Cart()
    c.add("apple", 2.0, 3)
    assert c.total() == 6.0

def test_remove_updates_total():
    c = Cart()
    c.add("apple", 2, 3)
    c.add("pear", 1.5, 2)
    assert c.total() == 9.0
    c.remove("apple")
    assert c.total() == 3.0
