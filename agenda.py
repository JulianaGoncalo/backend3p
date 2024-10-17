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


agenda = AgendaContatos()
agenda.adicionar_contato("Didi", "12345678","didi@gmail.com")
agenda.adicionar_contato("Juju", "87654321", "juju@email.com")
agenda.listar_contatos()
agenda.buscar_contato("Didi")
agenda.alterar_contato("Didi", "1234")
agenda.remover_contato("Juju")
agenda.salvar_contatos("contatos.txt")
