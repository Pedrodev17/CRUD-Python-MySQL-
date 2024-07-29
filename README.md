
# CRUD com Python e MySQL

Este projeto é um sistema CRUD (Create, Read, Update, Delete) desenvolvido com Python e MySQL. Ele permite realizar operações básicas de gerenciamento de dados, como criação, leitura, atualização e deleção de registros.

## Funcionalidades

- **Criação de Registros**: Permite adicionar novos registros ao banco de dados.
- **Leitura de Registros**: Exibe uma lista de todos os registros cadastrados.
- **Atualização de Registros**: Permite editar as informações dos registros existentes.
- **Deleção de Registros**: Permite remover registros do banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **MySQL**: Banco de dados utilizado para armazenar os dados.
- **mysql-connector-python**: Conector Python para MySQL.

## Requisitos

- Python 3.6 ou superior
- MySQL 5.7 ou superior
- Biblioteca `mysql-connector-python`

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/crud-python-mysql.git
   cd crud-python-mysql
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados MySQL:**
   - Crie um banco de dados MySQL.
   - Atualize as configurações de conexão com o banco de dados no arquivo `config.py`.

5. **Crie as tabelas no banco de dados:**
   ```bash
   python create_tables.py
   ```

6. **Execute a aplicação:**
   ```bash
   python app.py
   ```

## Configuração

Edite o arquivo `config.py` para configurar a conexão com o banco de dados MySQL:

```python
DB_HOST = 'localhost'
DB_USER = 'seu_usuario'
DB_PASSWORD = 'sua_senha'
DB_NAME = 'nome_do_banco_de_dados'
```

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação.
- `config.py`: Configurações do banco de dados.
- `create_tables.py`: Script para criar tabelas no banco de dados.
- `crud_operations.py`: Operações CRUD implementadas.
- `requirements.txt`: Arquivo de dependências do projeto.

## Contribuição

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório (`git push origin feature/nova-feature`).
5. Abra um Pull Request.



---

Se precisar de mais alguma informação ou modificação, sinta-se à vontade para me avisar!
