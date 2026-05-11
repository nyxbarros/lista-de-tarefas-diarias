#!/bin/bash

# caminho absoluto do script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# entrar no projeto
cd "$SCRIPT_DIR"

# criar venv apenas se não existir
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# ativar venv
source .venv/bin/activate

# atualizar pip
pip install --upgrade pip

# instalar dependências
pip install python-dateutil textual

# rodar programa
python3 main.py

echo "programa finalizado"