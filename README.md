## Setup do Ambiente

### Pré-requisitos
- Python 3.12+
- UV (instalador de pacotes)

### Instalação

```bash
# Instalar UV (se ainda não tem)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clonar o projeto
git clone <repo>
cd swe4ds-credit-api

# Criar ambiente e instalar dependências
uv sync --dev