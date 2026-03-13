from enum import Enum
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, id_persona: int, nombre: str, email: str):
        self.idper = id_persona
        self.nom = nombre
        self.email = email

    def login(self):
        print(f"\n{self.nom} ha iniciado sesión.")

    def actualizar_perfil(self, nuevo_nom: str, nuevo_email: str):
        self.nom = nuevo_nom
        self.email = nuevo_email
        print(f"Datos actualizados: {self.nom}, {self.email}")

class Cliente(Persona):
    def __init__(self, id_persona: int, nombre: str, email: str, puntos: int = 0):
        super().__init__(id_persona, nombre, email)
        self.puntos_fidelidad = puntos
        self.historial_pedidos = []

    def realizar_pedido(self, pedido_obj):
        self.historial_pedidos.append(pedido_obj)
        print(f"Pedido #{pedido_obj.id_ped} registrado para {self.nom}.")

    def consultar_historial(self):
        print(f"\nHistorial de {self.nom}")
        for p in self.historial_pedidos:
            print(f"Pedido ID: {p.id_ped}")
            print(f"Total: ${p.total:.2f}")
            print(f"Estado: {p.est.name}")

    def canjear_puntos(self, cantidad: int):
        if cantidad <= self.puntos_fidelidad:
            self.puntos_fidelidad -= cantidad
            print(f"Canjeo exitoso. Saldo actual: {self.puntos_fidelidad}")
        else:
            print("Error: Saldo insuficiente.")

class Rol(Enum):
    BARISTA = 1
    MESERO = 2
    GERENTE = 3

class Empleado(Persona):
    def __init__(self, id_persona: int, nombre: str, email: str, id_empleado: str, rol: Rol):
        super().__init__(id_persona, nombre, email)
        self.id_empl = id_empleado
        self.rol = rol

    def actualizar_inventario(self, inventario_obj, ingrediente, cantidad):
        inventario_obj.reducir_stock(ingrediente, cantidad)

    def cambiar_estado_pedido(self, pedido_obj, nuevo_estado):
        pedido_obj.est = nuevo_estado
        print(f"\nPedido #{pedido_obj.id_ped} está en: {nuevo_estado.name}")

class ProductoBase:
    def __init__(self, id_producto: int, nombre: str, precio_base: float):
        self.idpro = id_producto
        self.nom = nombre
        self.prebase = precio_base

class Temperatura(Enum):
    FRIA = 1
    CALIENTE = 2

class Bebida(ProductoBase):
    def __init__(self, id_p: int, nom: str, precio: float, tamano: str, temperatura: Temperatura):
        super().__init__(id_p, nom, precio)
        self.tam = tamano
        self.temp = temperatura
        self.modi = []

    def agregar_extra(self, extra: str):
        self.modi.append(extra)
        print(f"Se añadió {extra} a {self.nom}.")

    def calcular_precio_final(self):
        return self.prebase + (len(self.modi) * 0.50)

class Postre(ProductoBase):
    def __init__(self, id_p: int, nom: str, precio: float, vegano: bool, sin_gluten: bool):
        super().__init__(id_p, nom, precio)
        self.es_veg = vegano
        self.sin_glu = sin_gluten

class EstadoPedido(Enum):
    PENDIENTE = 1
    PREPARANDO = 2
    ENTREGADO = 3

class Pedido:
    def __init__(self, id_pedido: int, productos: list):
        self.id_ped = id_pedido
        self.prod = productos
        self.est = EstadoPedido.PENDIENTE
        self.total = self.calcular_total()

    def calcular_total(self):
        suma = 0
        for prod in self.prod:
            if isinstance(prod, Bebida):
                suma += prod.calcular_precio_final()
            else:
                suma += prod.prebase  
        return suma

class Inventario:
    def __init__(self):
        self.ingredientes = {"Granos Cafe": 50, "Leche": 20, "Azucar": 30}

    def reducir_stock(self, ingrediente: str, cantidad: int):
        actual = self.ingredientes.get(ingrediente, 0)
        if actual >= cantidad:
            self.ingredientes[ingrediente] -= cantidad
            print(f"{ingrediente}: {actual} -> {self.ingredientes[ingrediente]}")
        else:
            self.notificar_faltante(ingrediente)

    def notificar_faltante(self, ingrediente: str):
        print(f"Stock bajo de: {ingrediente}.")