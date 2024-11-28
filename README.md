# Brain Agriculture

Este projeto é uma aplicação Flask para cadastro de produtores rurais. A aplicação permite cadastrar, editar e excluir produtores, além de gerar relatórios e dashboards sobre as fazendas cadastradas. A aplicação utiliza PostgreSQL como banco de dados e pode ser executada utilizando Docker.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.11.1 ou superior
- Docker (se você for usar Docker)
- Bibliotecas python listadas no arquivo: requirements.txt


## Instalação

1. Instalar Dependências Python:
    Antes de executar o projeto, é necessário instalar as dependências. No terminal, execute o seguinte comando:

   ```bash
    pip install -r requirements.txt
   ```


   Se você não for usar Docker, crie um ambiente virtual:

   ```bash
      python -m venv .venv
      source .venv/bin/activate  # No Windows: .venv\Scripts\activate
      pip install -r requirements.txt
   ```



## Execução via Docker

2. Construir a Imagem Docker

    Na raiz do projeto, execute o comando para construir a imagem do Docker:


    ```bash
        docker build -t agriculture .
        docker run -p 5000:5000 brain-agriculture
    ```
    A aplicação estará disponível em http://localhost:5000.



## Testes Unitários

Para executar os testes unitários, utilize o seguinte comando:

```bash
python -m pytest tests/
```


## Endpoints da API

POST /produtores: Cadastrar um novo produtor.
```bash
   {
      "cpf_cnpj": "05427781064",
      "nome_produtor": "teste",
      "nome_fazenda": "fazenda teste",
      "cidade": "salvador",
      "estado": "ba",
      "area_total": 100,
      "area_agricultavel": 50,
      "area_vegetacao": 50,
      "culturas": ["Soja"]
   }
```

