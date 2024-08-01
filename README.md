<img src="https://i.imgur.com/3chUdCs.png" alt="MADR Logo">

# [FastAPI do zero](https://fastapidozero.dunossauro.com/) - MADR projeto final do curso.

Projeto de implementação do projeto final do curso de FastAPI do [Eduardo Mendes @dunossauro](https://github.com/dunossauro/fastapi-do-zero) do canal [Live de Python](https://www.youtube.com/@Dunossauro).

 
## Descrição do Projeto

Implementação e publicação do projeto final.
O objetivo é aplicar todos os conceitos aprendidos ao longo do curso para desenvolver uma API completa e funcional utilizando FastAPI.

## Requisitos do projeto

Para executar este projeto, você precisará ter instalado:

- Python 3.11 ou superior **(recomendação do autor)**
- [Poetry](https://python-poetry.org/) (Gerenciador de pacotes do Python)

## Instalação

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

## Uso
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

Exemplo:
```bash
task run
```

Abra o seu navegador, a aplicação estará disponível para ser executada no endereço local: `http://127.0.0.1:8000`.