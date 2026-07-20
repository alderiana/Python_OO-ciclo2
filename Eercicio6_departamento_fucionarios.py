class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome} | Salário: R$ {self.salario:.2f}"


class Departamento:
    def __init__(self, nome: str):
        self.nome = nome
        self.funcionarios = []  # Vetor/Lista que receberá os objetos Funcionário

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
        print(f"Funcionário '{funcionario.nome}' adicionado ao departamento '{self.nome}' com sucesso!")

    def calcular_media_salarial(self) -> float:
        if not self.funcionarios:
            return 0.0
        total_salarios = sum(f.salario for f in self.funcionarios)
        return total_salarios / len(self.funcionarios)

    def listar_funcionarios(self):
        print(f"\n--- Funcionários do Departamento: {self.nome} ---")
        if not self.funcionarios:
            print("Nenhum funcionário alocado neste departamento.")
            return
        for f in self.funcionarios:
            print(f"- {f}")


def exibir_menu():
    print("\n" + "="*30)
    print("      SISTEMA DE GESTÃO")
    print("="*30)
    print("1. Criar Departamento")
    print("2. Criar Funcionário")
    print("3. Adicionar Funcionário a um Departamento")
    print("4. Listar Funcionários de um Departamento")
    print("5. Ver Média Salarial de um Departamento")
    print("6. Sair")
    print("="*30)


def main():
    # Repositórios temporários na memória (listas)
    departamentos = []
    funcionarios_globais = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            nome_dep = input("Digite o nome do departamento: ").strip()
            if nome_dep:
                novo_dep = Departamento(nome_dep)
                departamentos.append(novo_dep)
                print(f"Departamento '{nome_dep}' criado com sucesso!")
            else:
                print("O nome do departamento não pode ser vazio.")

        elif opcao == "2":
            nome_func = input("Digite o nome do funcionário: ").strip()
            try:
                salario_func = float(input("Digite o salário do funcionário: R$ "))
                if nome_func and salario_func >= 0:
                    novo_func = Funcionario(nome_func, salario_func)
                    funcionarios_globais.append(novo_func)
                    print(f"Funcionário '{nome_func}' criado com sucesso e disponível para alocação!")
                else:
                    print("Dados inválidos. Nome não pode ser vazio e salário deve ser positivo.")
            except ValueError:
                print("Erro: Digite um valor numérico válido para o salário.")

        elif opcao == "3":
            if not departamentos:
                print("Nenhum departamento cadastrado. Crie um primeiro.")
                continue
            if not funcionarios_globais:
                print("Nenhum funcionário cadastrado. Crie um primeiro.")
                continue

            # Escolha do Departamento
            print("\nDepartamentos Disponíveis:")
            for i, dep in enumerate(departamentos):
                print(f"[{i}] {dep.nome}")
            try:
                idx_dep = int(input("Escolha o número do departamento: "))
                
                # Escolha do Funcionário
                print("\nFuncionários Disponíveis:")
                for i, func in enumerate(funcionarios_globais):
                    print(f"[{i}] {func.nome}")
                idx_func = int(input("Escolha o número do funcionário: "))

                # Associa via Agregação
                departamentos[idx_dep].adicionar_funcionario(funcionarios_globais[idx_func])
            except (ValueError, IndexError):
                print("Erro: Opção inválida de departamento ou funcionário.")

        elif opcao == "4":
            if not departamentos:
                print("Nenhum departamento cadastrado.")
                continue
            
            print("\nDepartamentos Disponíveis:")
            for i, dep in enumerate(departamentos):
                print(f"[{i}] {dep.nome}")
            try:
                idx_dep = int(input("Escolha o número do departamento para listar: "))
                departamentos[idx_dep].listar_funcionarios()
            except (ValueError, IndexError):
                print("Erro: Departamento inválido.")

        elif opcao == "5":
            if not departamentos:
                print("Nenhum departamento cadastrado.")
                continue

            print("\nDepartamentos Disponíveis:")
            for i, dep in enumerate(departamentos):
                print(f"[{i}] {dep.nome}")
            try:
                idx_dep = int(input("Escolha o número do departamento para ver a média: "))
                media = departamentos[idx_dep].calcular_media_salarial()
                print(f"A média salarial do departamento '{departamentos[idx_dep].nome}' é: R$ {media:.2f}")
            except (ValueError, IndexError):
                print("Erro: Departamento inválido.")

        elif opcao == "6":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
