class Autor:
    def __init__(self, nome: str, nacionalidade: str):
        self.nome = nome
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo: str, ano: int, autor: Autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor  # Agregação


class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.__livros = []  # Composição

    def cadastrar_livro(self, titulo: str, ano: int, autor: Autor):
        novo_livro = Livro(titulo, ano, autor)
        self.__livros.append(novo_livro)
        print(f"Livro '{titulo}' cadastrado na biblioteca {self.nome}.")

    def listar_livros(self):
        return self.__livros


class Usuario:
    def __init__(self, nome: str, biblioteca: Biblioteca):
        self.nome = nome
        self.biblioteca = biblioteca  # Associação

    def pegar_emprestado(self, titulo_livro: str):
        # Dependência
        livro_encontrado = None
        for livro in self.biblioteca.listar_livros():
            if livro.titulo == titulo_livro:
                livro_encontrado = livro
                break

        if livro_encontrado:
            print(f"Usuário {self.nome} pegou '{livro_encontrado.titulo}' de {livro_encontrado.autor.nome}.")
        else:
            print(f"O livro '{titulo_livro}' não está disponível.")


# --- Execução Correta ---
if __name__ == "__main__":
    autor1 = Autor("Machado de Assis", "Brasileira")
    minha_biblioteca = Biblioteca("Biblioteca Central")
    minha_biblioteca.cadastrar_livro("Dom Casmurro", 1899, autor1)
    
    usuario1 = Usuario("Carlos", minha_biblioteca)
    # Chamada corrigida para o nome correto do método:
    usuario1.pegar_emprestado("Dom Casmurro")


