# SWE4DS Credit API

API REST para predição de inadimplência de cartão de crédito, desenvolvida como projeto prático do curso de Engenharia de Machine Learning.

## Sobre o Projeto

Este projeto demonstra boas práticas de Engenharia de Software aplicadas a Data Science:

- Controle de versão com Git
- Ambientes reprodutíveis
- Testes automatizados
- Deploy em produção

## Tecnologias

- Python 3.12+
- FastAPI
- scikit-learn
- MLflow

## Setup

```bash
# Clonar repositório
git clone https://github.com/SEU_USUARIO/swe4ds-credit-api.git
cd swe4ds-credit-api

# Criar ambiente virtual
uv venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/macOS

# Instalar dependências
uv pip install -r requirements.txt