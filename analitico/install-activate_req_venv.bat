@echo off

if not exist venv\Scripts\activate.bat (
    echo Criando novo ambiente virtual venv...
    python -m venv venv
)

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Instalando dependencias...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Concluido!

powershell -NoExit -Command "& '.\venv\Scripts\Activate.ps1'"