class Usuario:
    def __init__(self, nome, senha, id):
        self.nome = nome
        self.senha = senha
        self.id = id
        self.experiencia = 0
        self.level = 1
        self.tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append({"tarefa": tarefa, "progresso": 0})
    
    def atualizar_progresso(self, indice, progresso):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["progresso"] = progresso
    
    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"ID: {self.id}")
        print(f"Experiência: {self.experiencia}")
        print(f"Level: {self.level}")
        print("Tarefas:")
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i+1}. {tarefa['tarefa']} - Progresso: {tarefa['progresso']}%")


# Criação de usuários de exemplo
usuarios = [
    Usuario("Joao", "senha123", 1),
    Usuario("Maria", "senha456", 2),
]

# Exemplo de uso
usuario_atual = None

while True:
    print("1. Login")
    print("2. Criar conta")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome de usuário: ")
        senha = input("Senha: ")
        
        for usuario in usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                usuario_atual = usuario
                print(f"Bem-vindo, {usuario.nome}!")
                break
        else:
            print("Usuário ou senha incorretos.")
    
    elif opcao == "2":
        nome = input("Nome de usuário: ")
        senha = input("Senha: ")
        novo_id = len(usuarios) + 1
        usuarios.append(Usuario(nome, senha, novo_id))
        print("Conta criada com sucesso!")
    
    elif opcao == "3":
        break

    # Se o usuário estiver logado, permite realizar ações
    if usuario_atual:
        print("1. Adicionar tarefa")
        print("2. Atualizar progresso de uma tarefa")
        print("3. Mostrar informações do usuário")
        print("4. Logout")
        
        acao = input("Escolha uma ação: ")
        
        if acao == "1":
            tarefa = input("Digite o nome da tarefa: ")
            usuario_atual.adicionar_tarefa(tarefa)
            print("Tarefa adicionada com sucesso!")
        elif acao == "2":
            usuario_atual.mostrar_info()
            indice = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
            progresso = int(input("Digite o novo progresso (em %): "))
            usuario_atual.atualizar_progresso(indice, progresso)
            print("Progresso atualizado com sucesso!")
        elif acao == "3":
            usuario_atual.mostrar_info()
        elif acao == "4":
            usuario_atual = None
            print("Logout realizado com sucesso!")
