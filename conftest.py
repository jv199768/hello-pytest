import hello
import pytest

@pytest.fixture(scope='module')
def hello_result():
	return hello.full_output()