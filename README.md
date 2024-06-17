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
cd fastapi_zero_madr_projeto_final
```

2. Crie um ambiente virtual com o Poetry:

```bash
poetry shell
```

3. Instale as dependências do projeto:

```bash
poetry install
```

## Uso
Iniciar o servidor ASGI local Uvicorn, execute:

```bash
uvicorn src.main:app --reload
```

Abra o seu navegador, a aplicação estará disponível para ser executada no endereço local: `http://127.0.0.1:8000`.
