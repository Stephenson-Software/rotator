from rotator import Rotator

rotator = Rotator()

def test_123456_1r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, 1)
    assert numbers == [2, 3, 4, 5, 6, 1]

def test_123456_2r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, 2)
    assert numbers == [3, 4, 5, 6, 1, 2]

def test_123456_3r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, 3)
    assert numbers == [4, 5, 6, 1, 2, 3]

def test_123456_4r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, 4)
    assert numbers == [5, 6, 1, 2, 3, 4]

def test_123456_5r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, 5)
    assert numbers == [6, 1, 2, 3, 4, 5]

def test_123456_6r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, 6)
    assert numbers == [1, 2, 3, 4, 5, 6]

def test_123456_87r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, 87)
    assert numbers == [4, 5, 6, 1, 2, 3]

def test_3827382717_1r():
    numbers = [3, 8, 2, 7, 3, 8, 2, 7, 1, 7]
    rotator.rotateRepeat(numbers, 1)
    assert numbers == [8, 2, 7, 3, 8, 2, 7, 1, 7, 3]

def test_ones_23r():
    numbers = [1, 1, 1, 1, 1, 1]
    rotator.rotateRepeat(numbers, 23)
    assert numbers == [1, 1, 1, 1, 1, 1]

def test_negatives_1r():
    numbers = [3, -4, 5, -6, 7]
    rotator.rotateRepeat(numbers, 1)
    assert numbers == [-4, 5, -6, 7, 3]

def test_big_list_1r():
    numbers = [3, 8, 2, 7, 3, 8, 2, 7, 1, 7, 6, 7, 5, 3, 2, 5, 7, 6, 3, 2, 1, 23, 5, 7, 4536, 123, 1]
    rotator.rotateRepeat(numbers, 1)
    assert numbers == [8, 2, 7, 3, 8, 2, 7, 1, 7, 6, 7, 5, 3, 2, 5, 7, 6, 3, 2, 1, 23, 5, 7, 4536, 123, 1, 3]

def test_decimals_1r():
    numbers = [1.2, 2.3, 3.3, 4.87, 5.0, 6.1]
    rotator.rotateRepeat(numbers, 1)
    assert numbers == [2.3, 3.3, 4.87, 5.0, 6.1, 1.2]

def test_letters_1r():
    letters = ['a', 'b', 'c']
    rotator.rotateRepeat(letters, 1)
    assert letters == ['b', 'c', 'a']