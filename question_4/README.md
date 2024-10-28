# Projeto Ola Mundo

Este projeto é um exemplo simples de como estruturar um projeto Python com múltiplos arquivos e diretórios, e como fazer uma chamada de função entre módulos diferentes. Ele usa uma função `ola_mundo` localizada em `src/ola_mundo.py` que retorna uma mensagem ao ser chamada a partir do arquivo principal `main.py`.

## Estrutura do Projeto

## Arquivos Principais

- **`main.py`**: Executa o projeto, importando e chamando a função `ola_mundo` de `src/ola_mundo.py`.
- **`src/ola_mundo.py`**: Contém a função `ola_mundo` que retorna uma mensagem de saudação.
- **`logs/logs.log`**: Arquivo destinado a armazenar logs de execução.

## Pré-requisitos

- Python 3.11.9
- `pip` para instalar as dependências

## Instalação

1. Clonar repositório:
   ```bash
   git clone https://github.com/GabrielZacchi/teste_autoglass.git
   cd question_4

2. Criar ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate

2. Instalar repositórios:
   ```bash
   pip install -r requirements.txt

## Executar

```bash
python main.py