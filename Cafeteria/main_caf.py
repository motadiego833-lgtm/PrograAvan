from Cafeteria import (Cliente, Empleado, Bebida, Postre, Pedido, Inventario, Rol, Temperatura, EstadoPedido)
#PD: Cuando inserto el * me sale error, por eso tuve que espesificar cada clase     

stock = Inventario()

clie1 = Cliente(1, "Ana", "ana.mtz@email.com", 200)
clie2 = Cliente(2, "Carlos", "carlos.r@email.com", 50)
clie3 = Cliente(3, "Sofía", "sofia@email.com", 850)

emple1 = Empleado(5, "Pedro", "pedro@cafeteria.com", "E-102", Rol.BARISTA)
emple2 = Empleado(6, "Lucía Mesa", "lucia@cafeteria.com", "E-103", Rol.MESERO)
emple3 = Empleado(7, "Marta Gómez", "marta@cafeteria.com", "E-104", Rol.GERENTE)

capuchino = Bebida(10, "Capuchino", 45.0, "Grande", Temperatura.CALIENTE)
capuchino.agregar_extra("Canela") 
capuchino.agregar_extra("Leche de Almendra") 

frappe_v = Bebida(11, "Frappé Vainilla", 60.0, "Mediano", Temperatura.FRIA)
frappe_v.agregar_extra("Crema Batida") 
frappe_v.agregar_extra("Sirope de Caramelo") 

te = Bebida(12, "Té", 50.0, "Grande", Temperatura.CALIENTE)
te.agregar_extra("Miel") 

galleta = Postre(20, "Galleta", 15.0, True, True)
brownie = Postre(21, "Brownie Chocolate", 25.0, False, False)
muffin = Postre(22, "Muffin de Arándano", 30.0, False, True)

pedi1 = Pedido(777, [capuchino, galleta])
clie1.login()
clie1.realizar_pedido(pedi1)

pedi2 = Pedido(778, [frappe_v, brownie])
clie2.login()
clie2.realizar_pedido(pedi2)

pedi3 = Pedido(779, [te, muffin])
clie3.login()
clie3.realizar_pedido(pedi3)

emple1.cambiar_estado_pedido(pedi1, EstadoPedido.PREPARANDO) 
emple2.cambiar_estado_pedido(pedi2, EstadoPedido.ENTREGADO) 
emple3.cambiar_estado_pedido(pedi3, EstadoPedido.ENTREGADO)  


print(f"\nCuentas:")
print(f"Total Ana: ${pedi1.total:.2f}")
print(f"Total Carlos: ${pedi2.total:.2f}")
print(f"Total Sofía: ${pedi3.total:.2f}")

clie1.consultar_historial()
clie2.consultar_historial()
clie3.consultar_historial()