"""Módulo de validação de dados."""

def validate_age(age: int) -> bool:
    """
    Valida se a idade é válida.
    
    Args:
        age: Idade a ser validada.
    
    Returns:
        True se a idade é válida (>= 0), False caso contrário.
    """
    return age >= 0