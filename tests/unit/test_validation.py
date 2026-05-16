# tests/unit/test_validation.py
def test_validate_age_rejects_negative():
    """Idade negativa dever ser rejeitada."""
    from src.validation import validate_age

    result = validate_age(-5)
    assert result is False


def test_validate_age_acceps_valid():
    """Idade válida deve ser aceita."""
    from src.validation import validate_age

    result= validate_age(25)
    assert result is True