#!/bin/bash

# Se a venv nao existir ou estiver quebrada, cria uma nova
if [ ! -f "venv/bin/activate" ]; then
    echo "Criando novo ambiente virtual venv..."
    python3 -m venv venv
fi

echo "Ativando ambiente virtual..."
source venv/bin/activate

echo "Instalando dependencias..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt

echo "Concluido!"


#!/bin/bash
# Abre um novo terminal carregando a venv e mantendo a sessão do Bash viva
bash --rcfile <(echo "source ~/.bashrc; source venv/bin/activate")
