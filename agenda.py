class AgendaContatos:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        novo_contato = {'nome': nome, 'telefone': telefone, 'email': email}
        self.contatos.append(novo_contato)
        return "Contato adicionado com sucesso"    
    
    def pesquisar_contato(self, nome):
        for contato in self.contatos:
            if contato['nome'] == nome:
                return contato
        return "Contato não encontrado"
    
    def listar_contatos(self):
        if not self.contatos:
            return "Nenhum contato cadastrado"
        for contato in self.contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato['nome']==nome:
                print(f"Nome: {contato ['nome']}")
                print(f"Telefone: {contato['telefone']}")        
                print(f"Email: {contato['email']}")
                return
        print(f"Contato {nome} não encontrado.")    

    def alterar_contato(self, nome, telefone, email):
        for contato in self.contatos:
            if contato['nome'] == nome:
                contato['telefone'] = telefone
                contato['email'] = email
                return "Contato alterado com sucesso"
        return "Contato não encontrado"

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato['nome'] == nome:
                self.contatos.remove(contato)
                return "Contato removido com sucesso"
        return "Contato não encontrado"

    def salvar_contatos(self, arquivo):
        with open(arquivo, 'w') as file:
            for contato in self.contatos:
                file.write(f"{contato['nome']},{contato['telefone']},{contato['email']}\n")
        
        print(f"Contatos salvos no arquivo {arquivo} com sucesso")      



def adic_interativo(agenda):
        while True:
            nome = input("Digite o nome do contato (ou 'sair' para finalizar):")
            if nome.lower() == 'sair':
                break
            telefone = input("Digite o numero de telefone:")
            email = input("Digite o email:")
            agenda.adicionar_contato(nome, telefone, email)



agenda = AgendaContatos()
agenda.adicionar_contato("Didi", "12345678","didi@gmail.com")
agenda.adicionar_contato("Juju", "87654321", "juju@email.com")
agenda.listar_contatos()
agenda.buscar_contato("Didi")
agenda.alterar_contato("Didi", "1234","oi@oi")
agenda.remover_contato("Juju")
agenda.salvar_contatos("contatos.txt")

agenda2 = AgendaContatos()
agenda2.adicionar_contato("Marilia", "123", "marilia@email")
agenda2.salvar_contatos("contatos.txt")

agenda3 = AgendaContatos()
agenda3.adicionar_contato("Paulo", "890","email@email")
agenda3.salvar_contatos("contatos.txt")

agenda4 = AgendaContatos()
agenda4.adicionar_contato("abublublé", "839", "email")
agenda4.salvar_contatos("contatos.txt")

agenda5 = AgendaContatos()
agenda5.adicionar_contato("Milena", "48299", "emaildec@gmail.com")
agenda5.salvar_contatos("contatos.txt")

agenda6 = AgendaContatos()
agenda6.adicionar_contato("Lucas", "081995020546", "lucas@gmail.com")
agenda6.salvar_contatos("contatos.txt")

agenda7 = AgendaContatos()
agenda7.adicionar_contato("Juliana", "081995020547", "juliana@gmail.com")
agenda7.salvar_contatos("contatos.txt")

agenda8 = AgendaContatos()
agenda8.adicionar_contato("Roberto", "081995020548", "roberto@gmail.com")
agenda8.salvar_contatos("contatos.txt")

agenda9 = AgendaContatos()
agenda9.adicionar_contato("Fernanda", "081995020549", "fernanda@gmail.com")
agenda9.salvar_contatos("contatos.txt")

agenda10 = AgendaContatos()
agenda10.adicionar_contato("Carlos", "081995020550", "carlos@gmail.com")
agenda10.salvar_contatos("contatos.txt")

agenda11 = AgendaContatos()
agenda11.adicionar_contato("Ana", "081995020551", "ana@gmail.com")
agenda11.salvar_contatos("contatos.txt")

agenda12 = AgendaContatos()
agenda12.adicionar_contato("Pedro", "081995020552", "pedro@gmail.com")
agenda12.salvar_contatos("contatos.txt")

agenda13 = AgendaContatos()
agenda13.adicionar_contato("Sofia", "081995020553", "sofia@gmail.com")
agenda13.salvar_contatos("contatos.txt")

agenda13.listar_contatos()



agenda = AgendaContatos()        
adic_interativo(agenda)
agenda.listar_contatos()
agenda.salvar_contatos("contatos.txt")


