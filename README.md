# Projeto de Recenseamento

Este projeto consiste em um sistema de recenseamento com camadas de dados, API e frontend.

## Estrutura do Projeto

- dados: Camada de dados com modelos e repositórios para acesso ao banco de dados
- api: Camada da API REST que expõe os recursos do sistema
- frontend: Camada de interface do usuário (não implementada neste exemplo)

## Clonando e Executando o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/user/repo.git
```
2. Entre na pasta do projeto:
```bash
cd repo
```
3. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate
```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```
5. Copie o arquivo .env.example para .env e configure as informações do banco de dados:
```bash
cp .env.example .env
```
6. Execute o script para criar as tabelas e popular o banco de dados:
```bash
python init_db.py
```
7. Inicie a aplicação:
```bash
python api/app.py
```
8. Acesse a aplicação no navegador ou utilize um cliente REST como Postman para testar as APIs.

