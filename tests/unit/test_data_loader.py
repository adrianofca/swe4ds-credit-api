# tests/unit/test_data_loader.py
"""
Testes unitários para o módulo data_loader.

Este módulo contém testes para:
- load_credit_data: Carregamento de dados
- preprocess_data: Preprocessamento
- get_feature_names: Extração de features
"""
import pytest
import pandas as pd
from pathlib import Path
from src.data_loader import (
    load_credit_data,
    preprocess_data,
    get_feature_names,
)


class TestGetFeatureNames:
    """Testes para a função get_feature_names."""
    
    def test_returns_list(self, sample_credit_data):
        """Verifica que o retorno é uma lista."""
        result = get_feature_names(sample_credit_data)
        assert isinstance(result, list)
    
    def test_excludes_id_column(self, sample_credit_data):
        """Verifica que coluna ID é excluída."""
        result = get_feature_names(sample_credit_data)
        assert "ID" not in result
    
    def test_excludes_target_column(self, sample_credit_data):
        """Verifica que coluna target é excluída."""
        result = get_feature_names(sample_credit_data)
        assert "default payment next month" not in result
    
    def test_returns_correct_count(self, sample_credit_data):
        """Verifica quantidade de features (23)."""
        result = get_feature_names(sample_credit_data)
        assert len(result) == 23
    
    def test_with_empty_dataframe(self, empty_dataframe):
        """Verifica comportamento com DataFrame vazio."""
        result = get_feature_names(empty_dataframe)
        assert result == []


class TestGetFeatureNamesParametrized:
    """Testes parametrizados para get_feature_names."""
    
    @pytest.mark.parametrize("column,should_include", [
        ("LIMIT_BAL", True),
        ("AGE", True),
        ("SEX", True),
        ("ID", False),
        ("default payment next month", False),
    ])
    def test_column_inclusion(
        self,
        sample_credit_data,
        column,
        should_include
    ):
        """Testa inclusão/exclusão de colunas específicas."""
        result = get_feature_names(sample_credit_data)
        
        if should_include:
            assert column in result
        else:
            assert column not in result


class TestPreprocessData:
    """Testes para a função preprocess_data."""
    
    def test_returns_tuple(self, sample_credit_data):
        """Verifica que retorna tupla (X, y)."""
        result = preprocess_data(sample_credit_data)
        assert isinstance(result, tuple)
        assert len(result) == 2
    
    def test_features_is_dataframe(self, sample_credit_data):
        """Verifica que features é DataFrame."""
        X, _ = preprocess_data(sample_credit_data)
        assert isinstance(X, pd.DataFrame)
    
    def test_target_is_series(self, sample_credit_data):
        """Verifica que target é Series."""
        _, y = preprocess_data(sample_credit_data)
        assert isinstance(y, pd.Series)
    
    def test_features_excludes_id(self, sample_credit_data):
        """Verifica que features não contém ID."""
        X, _ = preprocess_data(sample_credit_data)
        assert "ID" not in X.columns
    
    def test_features_excludes_target(self, sample_credit_data):
        """Verifica que features não contém target."""
        X, _ = preprocess_data(sample_credit_data)
        assert "default payment next month" not in X.columns
    
    def test_target_has_binary_values(self, sample_credit_data):
        """Verifica que target contém apenas 0 e 1."""
        _, y = preprocess_data(sample_credit_data)
        assert set(y.unique()).issubset({0, 1})
    
    def test_same_number_of_rows(self, sample_credit_data):
        """Verifica que X e y têm mesmo número de linhas."""
        X, y = preprocess_data(sample_credit_data)
        assert len(X) == len(y) == len(sample_credit_data)
    
    def test_raises_keyerror_without_target(self):
        """Verifica KeyError quando target não existe."""
        df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        
        with pytest.raises(KeyError) as exc_info:
            preprocess_data(df)
        
        assert "default payment next month" in str(exc_info.value)


class TestLoadCreditData:
    """Testes para a função load_credit_data."""
    
    def test_loads_from_cache(self, mocker, sample_credit_data):
        """Verifica uso do cache quando disponível."""
        mocker.patch(
            "src.data_loader.pd.read_parquet",
            return_value=sample_credit_data
        )
        mocker.patch("src.data_loader.Path.exists", return_value=True)
        
        result = load_credit_data(use_cache=True)
        
        assert result.equals(sample_credit_data)
    
    def test_raises_filenotfound(self, mocker):
        """Verifica FileNotFoundError para arquivo inexistente."""
        mocker.patch.object(Path, "exists", return_value=False)
        
        with pytest.raises(FileNotFoundError):
            load_credit_data(
                filepath=Path("nao_existe.csv"),
                use_cache=False
            )
    
    def test_raises_valueerror_for_empty(self, mocker, tmp_path):
        """Verifica ValueError para dados vazios."""
        empty_csv = tmp_path / "empty.csv"
        pd.DataFrame(columns=["col"]).to_csv(empty_csv, index=False)
        
        mocker.patch.object(
            Path, "exists",
            lambda self: str(self) == str(empty_csv)
        )
        
        with pytest.raises(ValueError) as exc_info:
            load_credit_data(filepath=empty_csv, use_cache=False)
        
        assert "vazio" in str(exc_info.value)