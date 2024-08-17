import hello as hello
import pytest

@pytest.mark.smoke
def test_main(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert result == "Hello, World!"
