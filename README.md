# 📚 Projeto CRUD com Neo4j em Python

Este projeto é um exemplo simples de aplicação **CRUD (Create, Read, Update, Delete)** usando o banco de dados **Neo4j** com Python e a biblioteca oficial `neo4j`.

## 🚀 Funcionalidades

- Criar um livro
- Listar todos os livros
- Atualizar o nome de um livro
- Excluir um livro

## 🧰 Tecnologias utilizadas

- Python 3.x
- Neo4j
- Biblioteca `neo4j`

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. Instale as dependências:

```bash
pip install neo4j
```

3. Configure a conexão com o Neo4j:

No arquivo `main.py`, altere o trecho abaixo com seu IP, usuário e senha:

```python
driver = GraphDatabase.driver(
    "bolt://<SEU_IP>:7687",
    auth=basic_auth("<USUARIO>", "<SENHA>")
)
```

> ⚠️ Verifique se o banco Neo4j está em execução e aceita conexões Bolt.

## ▶️ Como usar

Execute o programa com:

```bash
python main.py
```

E utilize o menu interativo:

```
Menu CRUD
1 - Criar
2 - Ler
3 - Atualizar
4 - Excluir
5 - Sair
```

## 🛠️ Estrutura

```
📁 projeto-crud-neo4j/
├── main.py          # Código principal com a classe Crud e o menu
├── README.md        # Documentação do projeto
├── requirements.txt # Dependencias do projeto
├── .gitignore       # Pastas e arquivos excluidos repositorio
└── setup.ps1        # Codigo powershell que cria o venv e instala as dependencias
```

## ✅ Exemplo de uso

- Criar: Adiciona um nó `Livro` com atributo `name`.
- Ler: Mostra todos os livros existentes.
- Atualizar: Modifica o nome de um livro.
- Excluir: Remove um livro pelo nome.

## 📌 Observações

- O label do nó utilizado no grafo é `Livro`.
- O projeto não possui persistência de sessão (nova sessão deve ser aberta a cada operação).
- Certifique-se de usar credenciais válidas e que o banco está online.

## 👤 Autor

Desenvolvido por Vitor Barbosa Marins.
