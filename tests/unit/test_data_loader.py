# tests/unit/test_data_loader.py
import pytest
import pandas as pd
from pathlib import Path


def test_load_credit_data_from_cache(mocker, tmp_path):
    """
    Testa que load_credit_data usa cache quando disponível.
    
    Args:
        mocker: Fixture do pytest-mock para criar mocks.
        tmp_path: Fixture built-in para diretório temporário.
    """
    # ARRANGE
    # Criar mock de pd.read_parquet
    mock_df = pd.DataFrame({"test": [1, 2, 3]})
    mock_read_parquet = mocker.patch(
        "src.data_loader.pd.read_parquet",
        return_value=mock_df
    )
    
    # Criar arquivo de cache fake
    cache_path = tmp_path / "data" / "credit_data.parquet"
    cache_path.parent.mkdir(parents=True)
    cache_path.touch()
    
    # Mockar Path.exists para retornar True
    mocker.patch.object(Path, "exists", return_value=True)
    
    # ACT
    # Chamar função (implementação real, dependências mockadas)
    # result = load_credit_data(use_cache=True)
    
    # ASSERT
    # mock_read_parquet.assert_called_once()
    # assert result.equals(mock_df)
    pass  # Implementaremos na próxima aula


def test_load_credit_data_handles_missing_file(mocker):
    """
    Testa que load_credit_data levanta erro para arquivo inexistente.
    """
    mocker.patch.object(Path, "exists", return_value=False)
    
    # with pytest.raises(FileNotFoundError):
    #     load_credit_data(filepath=Path("nao_existe.csv"))
    pass  # Implementaremos na próxima aula