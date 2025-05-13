from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    "bolt://18.212.55.49:7687",
    auth=basic_auth("neo4j", "augmentation-lamp-ventilators")
)

class Crud:
    def __init__(self):
        self.driver = driver

    def criar(self):
        name = input("Digite o nome do livro: ")
        with self.driver.session() as session:
            session.run(
                "CREATE (l:Livro {name: $name})",
                name=name
            )
        print("Livro criado com sucesso!")

    def ler(self):
        with self.driver.session() as session:
            result = session.run("MATCH (l:Livro) RETURN l.name AS name")
            records = list(result)
            if not records:
                print("Nenhum dado para exibir.")
            else:
                for record in records:
                    print(f"Livro: {record['name']}")

    def atualizar(self):
        nome_antigo = input("Digite o nome do livro a ser atualizado: ")
        nome_novo = input(f"Digite o novo nome para o livro '{nome_antigo}': ")
        with self.driver.session() as session:
            session.run(
                "MATCH (l:Livro {name: $old_name}) SET l.name = $new_name",
                old_name=nome_antigo, new_name=nome_novo
            )
        print("Livro atualizado com sucesso!")

    def excluir(self):
        nome = input("Digite o nome do livro a ser excluído: ")
        with self.driver.session() as session:
            session.run(
                "MATCH (l:Livro {name: $name}) DELETE l",
                name=nome
            )
        print("Livro excluído com sucesso!")

def exibir_menu():
    crud = Crud()

    while True:
        print("\nMenu CRUD")
        print("1 - Criar")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            crud.criar()
        elif escolha == '2':
            crud.ler()
        elif escolha == '3':
            crud.atualizar()
        elif escolha == '4':
            crud.excluir()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o menu
exibir_menu()
