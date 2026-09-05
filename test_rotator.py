import pytest

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

def test_rotate_123456_direct():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotate(numbers)
    assert numbers == [2, 3, 4, 5, 6, 1]

def test_rotate_returns_nothing():
    numbers = [1, 2, 3]
    assert rotator.rotate(numbers) is None

def test_rotate_mutates_caller_list():
    numbers = [1, 2, 3]
    aliasHeldByCaller = numbers
    rotator.rotate(numbers)
    assert aliasHeldByCaller == [2, 3, 1]

def test_rotate_single_item():
    numbers = [7]
    rotator.rotate(numbers)
    assert numbers == [7]

def test_rotate_two_items():
    numbers = [1, 2]
    rotator.rotate(numbers)
    assert numbers == [2, 1]

def test_rotate_empty_raises():
    numbers = []
    with pytest.raises(IndexError):
        rotator.rotate(numbers)

def test_123456_0r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, 0)
    assert numbers == [1, 2, 3, 4, 5, 6]

def test_123456_negative_3r():
    numbers = [1, 2, 3, 4, 5, 6]
    rotator.rotateRepeat(numbers, -3)
    assert numbers == [1, 2, 3, 4, 5, 6]

def test_empty_0r():
    numbers = []
    rotator.rotateRepeat(numbers, 0)
    assert numbers == []

def test_empty_1r_raises():
    numbers = []
    with pytest.raises(IndexError):
        rotator.rotateRepeat(numbers, 1)

def test_single_item_5r():
    numbers = [7]
    rotator.rotateRepeat(numbers, 5)
    assert numbers == [7]

def test_rotateRepeat_returns_nothing():
    numbers = [1, 2, 3]
    assert rotator.rotateRepeat(numbers, 2) is None

def test_rotateRepeat_mutates_caller_list():
    numbers = [1, 2, 3]
    aliasHeldByCaller = numbers
    rotator.rotateRepeat(numbers, 2)
    assert aliasHeldByCaller == [3, 1, 2]

def test_rotateRepeat_float_rotations_raises():
    numbers = [1, 2, 3]
    with pytest.raises(TypeError):
        rotator.rotateRepeat(numbers, 1.5)

def test_rotateRepeat_string_rotations_raises():
    numbers = [1, 2, 3]
    with pytest.raises(TypeError):
        rotator.rotateRepeat(numbers, "2")

def test_rotate_instances_are_independent():
    firstRotator = Rotator()
    secondRotator = Rotator()
    firstNumbers = [1, 2, 3]
    secondLetters = ['a', 'b', 'c']
    firstRotator.rotate(firstNumbers)
    secondRotator.rotate(secondLetters)
    firstRotator.rotate(firstNumbers)
    assert firstNumbers == [3, 1, 2]
    assert secondLetters == ['b', 'c', 'a']
