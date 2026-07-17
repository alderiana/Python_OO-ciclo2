class Documento:
    def __init__(self, titulo: str, conteudo: str):
        self.titulo = titulo
        self.conteudo = conteudo
        
class Impressora:
    # Relação de dependência: o documento é usado apenas dentro deste método
    def imprimir(self, d: Documento):
        print("\n--- [IMPRIMINDO DOCUMENTO] ---")
        print(f"Título:   {d.titulo}")
        print(f"Conteúdo: {d.conteudo}")
        print("-----------------------------\n")
def main():  # Alterado de menu para main
    lista_documentos = []
    impressora = Impressora()
    
    while True:
        print("==== MENU IMPRESSORA ====")
        print("1. Criar Novo Documento")
        print("2. Listar e Imprimir Documentos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Digite o título do documento: ")
            conteudo = input("Digite o conteúdo do documento: ")
            
            novo_doc = Documento(titulo, conteudo)
            lista_documentos.append(novo_doc)
            print("Documento criado com sucesso!\n")

        elif opcao == "2":
            if not lista_documentos:
                print("Nenhum documento cadastrado ainda.\n")
            else:
                print("\n--- Documentos Disponíveis ---")
                for indice, doc in enumerate(lista_documentos, start=1):
                    print(f"{indice}. {doc.titulo}")
                
                escolha_str = input("Escolha o número do documento para imprimir: ").strip()
                
                if escolha_str.isdigit():
                    escolha = int(escolha_str) - 1
                    if 0 <= escolha < len(lista_documentos):
                        # A impressora recebe o documento por dependência aqui
                        impressora.imprimir(lista_documentos[escolha])
                    else:
                        print("Opção inválida!\n")
                else:
                    print("Entrada inválida! Digite um número.\n")

        elif opcao == "3":
            print("Encerrando o programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


# Executa o programa chamando a função main
if __name__ == "__main__":
    main()