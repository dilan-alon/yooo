class Pedido:
    def __init__(self, estado, tipo_pedido):
        self._estado = estado
        self._tipo_pedido = tipo_pedido
        self._total = 0.0

    def calcular_total(self):
        raise NotImplementedError("Falta implementar en la clase hija")

    def cambiar_estado(self, nuevo_estado):
        self._estado = nuevo_estado
        print(f"Estado actualizado: {self._estado}")

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, valor):
        self._total = valor


class Producto:
    def __init__(self, id, nombre, precio_base):
        self._id = id
        self._nombre = nombre
        self._precio_base = precio_base

    def calcular_precio(self):
        raise NotImplementedError("Falta implementar en la clase hija")

    @property
    def precio_base(self):
        return self._precio_base


class Pago:
    def __init__(self, id_pago, monto):
        self._id_pago = id_pago
        self._monto = monto

    def procesar_pago(self):
        raise NotImplementedError("Falta implementar en la clase hija")

    @property
    def monto(self):
        return self._monto


# Clases para los tipos de Pedido
class PedidoLocal(Pedido):
    def __init__(self, estado, tipo_pedido, numero_mesa):
        super().__init__(estado, tipo_pedido)
        self._numero_mesa = numero_mesa

    def calcular_total(self):
        self.total = 50.0
        print(f"Total Mesa {self._numero_mesa}: S/ {self.total}")


class PedidoMesero(Pedido):
    def __init__(self, estado, tipo_pedido, cargo_enlace):
        super().__init__(estado, tipo_pedido)
        self._cargo_enlace = cargo_enlace

    def calcular_total(self):
        self.total = 80.0
        print(f"Total pedido de {self._cargo_enlace}: S/ {self.total}")


class PedidoDelivery(Pedido):
    def __init__(self, estado, tipo_pedido, zona):
        super().__init__(estado, tipo_pedido)
        self._zona = zona

    def calcular_total(self):
        self.total = 120.0 
        print(f"Total Delivery ({self._zona}): S/ {self.total}")

class Plato(Producto):
    def __init__(self, id, nombre, precio_base, tipo_plato):
        super().__init__(id, nombre, precio_base)
        self._tipo_plato = tipo_plato

    def calcular_precio(self):
        return self.precio_base


class Bebida(Producto):
    def __init__(self, id, nombre, precio_base, tipo_bebida, es_frio):
        super().__init__(id, nombre, precio_base)
        self._tipo_bebida = tipo_bebida
        self._es_frio = es_frio

    def calcular_precio(self):
        return self.precio_base


class Combo(Producto):
    def __init__(self, id, nombre, precio_base, descuento):
        super().__init__(id, nombre, precio_base)
        self._descuento = descuento
        self._lista_productos = [] 

    def agregar_producto(self, producto):
        self._lista_productos.append(producto)

    def calcular_precio(self):
        suma = 0
        for p in self._lista_productos:
            suma += p.calcular_precio()
        return suma - self._descuento



class Efectivo(Pago):
    def __init__(self, id_pago, monto, monto_recibido):
        super().__init__(id_pago, monto)
        self._monto_recibido = monto_recibido

    def procesar_pago(self):
        vuelto = self._monto_recibido - self.monto
        print(f"Pago efectivo OK. Vuelto: S/ {vuelto}")


class Tarjeta(Pago):
    def __init__(self, id_pago, monto, numero_tarjeta):
        super().__init__(id_pago, monto)
        self._numero_tarjeta = numero_tarjeta

    def procesar_pago(self):
        digitos = self._numero_tarjeta[-4:]
        print(f"Pago tarjeta OK. Termina en {digitos}")


class PagoQR(Pago):
    def __init__(self, id_pago, monto, codigo_transaccion):
        super().__init__(id_pago, monto)
        self._codigo_transaccion = codigo_transaccion

    def procesar_pago(self):
        print(f"Pago QR OK. Código: {self._codigo_transaccion}")



class Producto_Pedido:
    def __init__(self, producto, pedido):
        self._producto = producto
        self._pedido = pedido


class Cliente:
    def __init__(self, id, nombre, telefono):
        self._id = id
        self._nombre = nombre
        self._telefono = telefono
        self._pedidos = [] 

    def validar_telefono(self):
        if len(self._telefono) >= 9:
            print(f"Teléfono de {self._nombre} válido.")
            return True
        else:
            print(f"Teléfono de {self._nombre} inválido.")
            return False


class Restaurante:
    def __init__(self, nombre_local):
        self._nombre_local = nombre_local
        self._lista_menu = []
        self._lista_pedido = []

    def registrar_pedido(self, pedido):
        self._lista_pedido.append(pedido)
        print(f"Pedido guardado en {self._nombre_local}")



if __name__ == "__main__":
    print("Iniciando prueba...\n")

    cliente1 = Cliente(1, "Juan Perez", "987654321")
    cliente1.validar_telefono()
    
    plato1 = Plato(101, "Lomo Saltado", 25.0, "Fondo")
    bebida1 = Bebida(102, "Chicha Morada", 8.0, "Jarra", True)
    
    combo1 = Combo(103, "Combo Almuerzo", 0, 3.0) 
    combo1.agregar_producto(plato1)
    combo1.agregar_producto(bebida1)
    
    print(f"Precio Plato: S/ {plato1.calcular_precio()}")
    print(f"Precio Combo: S/ {combo1.calcular_precio()}\n")

    restaurante = Restaurante("El Buen Sabor")
    pedido1 = PedidoDelivery("En preparacion", "Delivery", "Zona Norte")
    
    pedido1.calcular_total()
    restaurante.registrar_pedido(pedido1)
    
    asociacion1 = Producto_Pedido(combo1, pedido1)
    pedido1.cambiar_estado("En camino")
    print()

    pago1 = Tarjeta(500, pedido1.total, "1234567890123456")
    pago1.procesar_pago()
    
    pago2 = Efectivo(501, 50.0, 100.0)
    pago2.procesar_pago()