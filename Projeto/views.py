from models import Cliente, NCliente

def cliente_inserir(nome, email, fone):
  cliente = Cliente(0, nome, email, fone)
  NCliente.inserir(cliente)

