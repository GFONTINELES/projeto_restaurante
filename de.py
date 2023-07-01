class ItemMenu:
    def __init__(self, id, nome, descricao, categoria, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.preco = preco

class Pedido:
    def __init__(self, id, item, id_mesa, id_cliente, data_hora):
        self.id = id
        self.item = item
        self.id_mesa = id_mesa
        self.id_cliente = id_cliente
        self.data_hora = data_hora

class Mesa:
    def __init__(self, id, capacidade):
        self.id = id
        self.capacidade = capacidade

class Cliente:
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Restaurante:
    def __init__(self):
        self.cardapio = []
        self.pedidos = []
        self.mesas = []
        self.clientes = []

    def adicionar_item(self, nome, descricao, categoria, preco):
        item_id = len(self.cardapio) + 1
        item = ItemMenu(item_id, nome, descricao, categoria, preco)
        self.cardapio.append(item)
        return item

    def adicionar_pedido(self, item_menu, id_mesa, id_cliente, data_hora):
        pedido_id = len(self.pedidos) + 1
        pedido = Pedido(pedido_id, item_menu, id_mesa, id_cliente, data_hora)
        self.pedidos.append(pedido)
        return pedido

    def adicionar_mesa(self, capacidade):
        mesa_id = len(self.mesas) + 1
        mesa = Mesa(mesa_id, capacidade)
        self.mesas.append(mesa)
        return mesa

    def adicionar_cliente(self, nome, telefone, email):
        cliente_id = len(self.clientes) + 1
        cliente = Cliente(cliente_id, nome, telefone, email)
        self.clientes.append(cliente)
        return cliente

    def obter_item_por_id(self, item_id):
        for item in self.cardapio:
            if item.id == item_id:
                return item
        return None

    def obter_mesa_por_id(self, mesa_id):
        for mesa in self.mesas:
            if mesa.id == mesa_id:
                return mesa
        return None

    def obter_cliente_por_id(self, cliente_id):
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                return cliente
        return None

    def obter_cardapio(self):
        return self.cardapio

    def obter_pedidos_por_mesa(self, mesa_id):
        pedidos_mesa = []
        for pedido in self.pedidos:
            if pedido.id_mesa == mesa_id:
                pedidos_mesa.append(pedido)
        return pedidos_mesa

    def obter_pedidos_por_cliente(self, cliente_id):
        pedidos_cliente = []
        for pedido in self.pedidos:
            if pedido.id_cliente == cliente_id:
                pedidos_cliente.append(pedido)
        return pedidos_cliente

    def obter_mesas_disponiveis(self):
        mesas_disponiveis = []
        for mesa in self.mesas:
            if self.verificar_mesa_disponivel(mesa.id):
                mesas_disponiveis.append(mesa)
        return mesas_disponiveis

    def verificar_mesa_disponivel(self, mesa_id):
        for pedido in self.pedidos:
            if pedido.id_mesa == mesa_id:
                return False
        return True

    def exibir_menu(self):
        opcao = 0
        while opcao != 5:
            print("----- MENU -----")
            print("1. Pedidos por cliente")
            print("2. Cardápio")
            print("3. Mesas disponíveis")
            print("4. Clientes cadastrados")
            print("5. Sair")
            opcao = int(input("Selecione uma opção: "))

            if opcao == 1:
                cliente_id = int(input("Digite o ID do cliente: "))
                pedidos_cliente = self.obter_pedidos_por_cliente(cliente_id)
                if pedidos_cliente:
                    print(f"Pedidos do cliente {self.obter_cliente_por_id(cliente_id).nome}:")
                    for pedido in pedidos_cliente:
                        item = self.obter_item_por_id(pedido.item.id)
                        print(f"Pedido: {item.nome} - Data/Hora: {pedido.data_hora}")
                else:
                    print("Nenhum pedido encontrado para o cliente.")

            elif opcao == 2:
                cardapio = self.obter_cardapio()
                print("Cardápio:")
                for item in cardapio:
                    print(f"Item: {item.nome} - Categoria: {item.categoria} - Preço: R${item.preco}")

            elif opcao == 3:
                mesas_disponiveis = self.obter_mesas_disponiveis()
                if mesas_disponiveis:
                    print("Mesas disponíveis:")
                    for mesa in mesas_disponiveis:
                        print(f"Mesa disponível: {mesa.id} - Capacidade: {mesa.capacidade}")
                else:
                    print("Todas as mesas estão ocupadas.")

            elif opcao == 4:
                clientes = self.clientes
                if clientes:
                    print("Clientes cadastrados:")
                    for cliente in clientes:
                        print(f"Cliente: {cliente.nome} - Telefone: {cliente.telefone} - Email: {cliente.email}")
                else:
                    print("Nenhum cliente cadastrado.")

            elif opcao == 5:
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida. Digite novamente.")

restaurante = Restaurante()

# Adicionar itens ao menu
item_salada = restaurante.adicionar_item("Salada", "Salada com alface, croutons e molho Caesar", "Entrada", 15.0)
item_spaghetti = restaurante.adicionar_item("Spaghetti à Bolonhesa", "Massa de spaghetti com molho à bolonhesa", "Prato Principal", 25.0)
item_sorvete = restaurante.adicionar_item("Sorvete de Morango", "Sorvete de Morango com cobertura", "Sobremesa", 12.0)
item_picanha = restaurante.adicionar_item("Picanha Argentina", "Refeição de Picanha Argentina", "Prato Principal", 80.0)
item_frango = restaurante.adicionar_item("Frango assado", "Refeição de Frango Assado", "Prato Principal", 80.0)
item_saladadefruta = restaurante.adicionar_item("Salada de frutas", "Salada de frutas vermelhas", "Sobremesa", 9.0)
item_espetinho = restaurante.adicionar_item("espetinho", "Espetinho de carne, de frango ou porco", "Entrada", 7.0)
item_lasanha = restaurante.adicionar_item("Lasanha", "Lasanha de carne", "Prato Principal", 28.0)
item_frangodeso = restaurante.adicionar_item("Frango desossado", "Frango desossado", "Prato Principal", 35.0)
item_pizza = restaurante.adicionar_item("Pizza", "Pizza Pequena(pedaço)", "Entrada", 10.0)
item_hamburguer = restaurante.adicionar_item("Hamburguer", "Hamburguer duas carnes, ovo e salada", "Entrada", 15.0)
item_pastel = restaurante.adicionar_item("Pastel", "Pastel de carne, de frango ou queijo", "Entrada", 12.0)

# Adicionar mesas ao restaurante
mesa_1 = restaurante.adicionar_mesa(4)
mesa_2 = restaurante.adicionar_mesa(4)
mesa_3 = restaurante.adicionar_mesa(6)
mesa_4 = restaurante.adicionar_mesa(4)
mesa_5 = restaurante.adicionar_mesa(2)
mesa_6 = restaurante.adicionar_mesa(8)
mesa_7 = restaurante.adicionar_mesa(6)
mesa_8 = restaurante.adicionar_mesa(4)

# Adicionar clientes ao restaurante
cliente_1 = restaurante.adicionar_cliente("João Pedro", "9925-1111", "jjj23@hotmail.com")
cliente_2 = restaurante.adicionar_cliente("Mariana", "9899-2222", "mariana@example.com")
cliente_3 = restaurante.adicionar_cliente("Pedro Avelar", "8899-3873", "peduy12@gmail.com")
cliente_4 = restaurante.adicionar_cliente("Nunes", "8779-0023", "pnunes012@hotmail.com")
cliente_5 = restaurante.adicionar_cliente("Pedro Luiz", "8979-3323", "pedr@hotmail.com")
cliente_6 = restaurante.adicionar_cliente("Antonieta", "8991-3323", "ped872@hotmail.com")
cliente_7 = restaurante.adicionar_cliente("Maria Luiza", "8999-3323", "luizah012@hotmail.com")
cliente_8 = restaurante.adicionar_cliente("Pedro Fontineles", "8099-9393", "pedrin1298@hotmail.com")
cliente_9 = restaurante.adicionar_cliente("Lucas Fontineles", "8909-3320", "lkfontineles29@hotmail.com")

# Fazer pedidos
restaurante.adicionar_pedido(item_salada, mesa_1.id, cliente_1.id, "2023-06-28 11:00:00")
restaurante.adicionar_pedido(item_espetinho, mesa_1.id, cliente_1.id, "2023-06-28 11:10:00")
restaurante.adicionar_pedido(item_spaghetti, mesa_2.id, cliente_2.id, "2023-06-28 11:30:00")
restaurante.adicionar_pedido(item_sorvete, mesa_1.id, cliente_3.id, "2023-06-28 13:00:00")
restaurante.adicionar_pedido(item_sorvete, mesa_2.id, cliente_2.id, "2023-06-28 13:30:00")
restaurante.adicionar_pedido(item_picanha, mesa_3.id, cliente_4.id, "2023-06-28 13:20:00")
restaurante.adicionar_pedido(item_frango, mesa_2.id, cliente_5.id, "2023-06-28 12:30:00")
restaurante.adicionar_pedido(item_spaghetti, mesa_5.id, cliente_9.id, "2023-06-28 12:10:50")
restaurante.adicionar_pedido(item_salada, mesa_5.id, cliente_8.id, "2023-06-28 12:00:00")
restaurante.adicionar_pedido(item_hamburguer, mesa_6.id, cliente_7.id, "2023-06-28 18:30:00")
restaurante.adicionar_pedido(item_saladadefruta, mesa_6.id, cliente_7.id, "2023-06-28 18:30:55")
restaurante.adicionar_pedido(item_pizza, mesa_6.id, cliente_7.id, "2023-06-28 18:31:00")

# Exibir menu interativo
restaurante.exibir_menu()
