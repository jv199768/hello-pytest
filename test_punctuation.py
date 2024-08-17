
def test_comma(hello_result):
    assert ',' in hello_result

def test_exclamation(hello_result):
    assert hello_result.endswith('!')