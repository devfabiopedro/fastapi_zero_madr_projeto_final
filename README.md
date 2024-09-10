<img src="https://i.imgur.com/3chUdCs.png" alt="MADR Logo">

## [FastAPI do zero](https://fastapidozero.dunossauro.com/)  
# 📚 MADR - Projeto final.

Projeto final do curso de FastAPI do [Eduardo Mendes @dunossauro](https://github.com/dunossauro/fastapi-do-zero) do canal [Live de Python](https://www.youtube.com/@Dunossauro).

 
## 📙Descrição deste Projeto:

Implementação de um sistema simples de gerenciamento de livros e romances.  

O MADR ( Meu Acervo de Romances ), deve seguir estas [orientações de projeto](https://fastapidozero.dunossauro.com/14/).

O principal objetivo é poder aplicar todos os conhecimentos adquiridos ao longo do treinamento, mostrando e executando os passos necessários para garantir o desenvolvimento correto uma API REST completa, funcional e escalável se utilizando do FastAPI.

## 🛠️ Os requisitos do projeto:

Para executar este projeto, você precisará ter instalado:

- Python 3.11 ou superior **(recomendação do autor, versão mínima)**
- [Poetry 1.8.3 ou superior](https://python-poetry.org/) (Gerenciador de pacotes do Python)

#### Dependências de projeto:
- Fastapi 0.111.1
- Alembic 1.13.2
- Sqlalchemy 2.0.31
- Pyjwt 2.9.0
- Psycopg-binary 3.2.1
- Python-dotenv 1.0.1
- Docker 7.1.0
#### Dependências de desenvolvimento:
- Factory-boy 3.3.0
- Freezegun 1.5.1
- Pytest 8.3.2
- Pytest-cov 5.0.0
- Ruff 0.5.5
- Taskipy 1.13.0
- Testcontainers 4.7.2

## 🖥️ Instalação:

1. Clone o repositório:

```bash
git clone https://github.com/devfabiopedro/fastapi_zero_madr_projeto_final.git
```
```bash
Vá para o diretório da aplicação:
cd fastapi_zero_madr_projeto_final
```

2. Crie um ambiente virtual com o Poetry:

```
poetry shell
```

3. Instale as dependências do projeto:

```
poetry install
```

## 🚀 Uso:
O Taskipy é uma biblioteca Python que facilita a criação e execução de tarefas de automação.
Neste projeto usei o [Taskipy](https://pypi.org/project/taskipy/)

```
No console da aplicação execute o comando:
task --list
```
Vai listar todos os comandos disponíveis para Executar, Formatar e Testar a aplicação:
```
lint - Faz um linter no código.
format - Formata o código corretamente.
run - Executa a aplicação.
test - Executas os testes unitários.
post-test - Exibe relatório de cobertura.
```

Executa o projeto:
```bash
task run
```

Abra o seu navegador, a aplicação estará disponível para ser executada no endereço local: `http://127.0.0.1:8000`.
