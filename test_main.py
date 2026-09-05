# @author Daniel McCoy Stephenson
# @since 8/21/2026
import importlib.util

import pytest

import main
from main import printNumbers

def loadMainFresh():
    spec = importlib.util.spec_from_file_location("mainFresh", main.__file__)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_printNumbers_single_item(capsys):
    printNumbers([5])
    assert capsys.readouterr().out == "[5]\n"

def test_printNumbers_multiple_items(capsys):
    printNumbers([1, 2, 3])
    assert capsys.readouterr().out == "[1, 2, 3]\n"

def test_printNumbers_letters(capsys):
    printNumbers(['a', 'b'])
    assert capsys.readouterr().out == "[a, b]\n"

def test_printNumbers_decimals(capsys):
    printNumbers([1.2, 5.0])
    assert capsys.readouterr().out == "[1.2, 5.0]\n"

def test_printNumbers_does_not_mutate(capsys):
    numbers = [1, 2, 3]
    printNumbers(numbers)
    capsys.readouterr()
    assert numbers == [1, 2, 3]

def test_printNumbers_mixed_types(capsys):
    printNumbers([None, True, 'a', 2.5])
    assert capsys.readouterr().out == "[None, True, a, 2.5]\n"

def test_printNumbers_returns_nothing(capsys):
    assert printNumbers([1, 2]) is None
    capsys.readouterr()

def test_printNumbers_empty_raises():
    with pytest.raises(IndexError):
        printNumbers([])

def test_run_prints_before_and_after(capsys):
    loadMainFresh()
    assert capsys.readouterr().out == (
        "Num rotations: 1\n"
        "\n"
        "Before:\n"
        "[1, 2, 3, 4, 5, 6]\n"
        "\n"
        "After:\n"
        "[2, 3, 4, 5, 6, 1]\n"
        "\n"
    )
