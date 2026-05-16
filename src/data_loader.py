# src/data_loader.py
"""
Módulo para carregamento e preprocessamento de dados de crédito.
"""
from pathlib import Path
from typing import Tuple, List
import pandas as pd


def load_credit_data(
    filepath: Path | None = None,
    use_cache: bool = True
) -> pd.DataFrame:
    """
    Carrega dados de crédito de arquivo CSV ou cache.
    
    Args:
        filepath: Caminho para arquivo CSV. Se None, usa padrão.
        use_cache: Se True, tenta carregar de cache parquet.
        
    Returns:
        DataFrame com dados de crédito.
        
    Raises:
        FileNotFoundError: Se arquivo não existe.
        ValueError: Se dados estão vazios.
    """
    if filepath is None:
        filepath = Path("data/raw/UCI_Credit_Card.csv")
    
    cache_path = Path("data/processed/credit_cache.parquet")
    
    if use_cache and cache_path.exists():
        return pd.read_parquet(cache_path)
    
    if not filepath.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    
    df = pd.read_csv(filepath)
    
    if df.empty:
        raise ValueError("Dataset está vazio")
    
    if use_cache:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(cache_path)
    
    return df


def preprocess_data(
    df: pd.DataFrame,
    target_column: str = "default payment next month",
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Preprocessa os dados para treinamento.
    
    Args:
        df: DataFrame com dados brutos.
        target_column: Nome da coluna alvo.
    
    Returns:
        Tupla com (X, y) onde X é DataFrame e y é Series.
    """
    # Remover coluna ID
    df = df.drop(columns=["ID"], errors="ignore")
    
    # Separar features e target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    return X, y

def get_feature_names(df: pd.DataFrame) -> list:
    """
    Retorna os nomes das features do dataset.
    
    Args:
        df: DataFrame com os dados.
    
    Returns:
        Lista com nomes das features (excluindo ID e target).
    """
    if df.empty:
        return []
    
    excluded_columns = {"ID", "default payment next month"}
    return [col for col in df.columns if col not in excluded_columns]