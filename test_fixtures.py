import pytest

@pytest.fixture
def any_name(scope='module'):
    print('\n setup')
    yield 5
    print('teardown')

def test_a(any_name):
    print('do something')
    print('assert something')
    assert any_name == 5


def test_b(any_name):
    print('do something')
    print('assert something')
    assert any_name == 5