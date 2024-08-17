import hello
import pytest

def test_hello():
    result = hello.full_output()
    assert result == "Hello, World!"

def test_comma():
    result = hello.full_output()
    assert ',' in result

def test_exclamation():
    result = hello.full_output()
    assert result.endswith('!')

@pytest.mark.parametrize('arg_str, expected', [
    ("-g Hey", "Hey, World!"),
    ("--greeting Hey", "Hey, World!"),
    ("-n Brian", "Hello, Brian!"),
    ("--name Brian", "Hello, Brian!"),
    pytest.param("-g Hey -n Brian", "Hey, Brian!", marks=pytest.mark.smoke),
    ], ids=(lambda x : f"'{x}'"))
def test_output(arg_str, expected):
    result = hello.full_output(arg_str)
    assert result == expected

'''def test_greeting(arg_str):
    result = hello.full_output(arg_str)
    assert result == "Hey, World!"


def test_greeting_long():
    result = hello.full_output("--greeting Hey")
    assert result == "Hey, World!"

def test_name(arg_str):
    result = hello.full_output(arg_str)
    assert result == "Hello, Brian!"

def test_name_long():
    result = hello.full_output("--name Brian")
    assert result == "Hello, Brian!"'''

