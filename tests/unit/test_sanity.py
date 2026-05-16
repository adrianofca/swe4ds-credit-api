# tests/unit/test_sanity.py
def test_sanity_check():
    """Teste mínimo para verificar que pytest funciona."""
    assert 1 + 1 == 2


def test_python_version():
    """Verifica versão do Python."""
    import sys
    assert sys.version_info >= (3, 12)