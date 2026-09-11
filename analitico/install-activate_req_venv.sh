#!/usr/bin/env bash

if [ ! -f "venv/bin/activate" ]; then
    echo "Criando novo ambiente virtual venv..."
    python3 -m venv venv
fi

echo "Ativando ambiente virtual..."
source venv/bin/activate

echo "Instalando dependencias..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Concluido!"

exec bash --rcfile <(echo "source ~/.bashrc; source venv/bin/activate")
