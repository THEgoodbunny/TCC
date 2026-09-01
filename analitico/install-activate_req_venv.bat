@echo off

:: Se a venv nao existir ou estiver quebrada, cria uma nova
if not exist venv\Scripts\activate (
    echo Criando novo ambiente virtual venv...
    python -m venv venv
)

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando dependencias...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Concluido!
@echo off
title Terminal Python (VENV Ativada)
cmd /k "call venv\Scripts\activate"

pause
