class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
class Cliente(Persona):
    def __init__(self,nombre,apellido, numero_cuenta,balance=0.0):
        super().__init__(nombre,apellido)
        self.balance = balance
        self.numero_cuenta = numero_cuenta
    def __str__(self):
        return f'Cliente:{self.nombre} {self.apellido}\nNumero de Cuenta: {self.numero_cuenta}\nBalance: ${self.balance}'

    #---- Metodos de Operacion Bancaria ---
    def consultar_saldo(self):
        """ Retorna el saldo actual del cliente"""
        return float(self.balance)

    def depositar(self, cantidad):

        """añade la cantidad al balance del cliente.
           Válida que la cantidad sea Positiva."""

        if cantidad > 0:
            self.balance += cantidad
            return True, f"Deposito de {cantidad:.2f} Realizado con exito.\nNuevo Balance = ${self.balance:.2f}"
        else:
            return False, "Error la cantidad depositada debe ser positiva."

    def retirar(self, cantidad):

        """
         Retira una cantidad del balance del cliente.
         Válida que la cantidad sea positiva y que haya fondos suficientes.
        """

        if cantidad <=0:

           return False, "La Cantidad a retirar debe ser positiva."
        elif cantidad > self.balance:
            return False, f"Error: Fondos insuficiente. Su saldo actual es: ${self.balance:.2f}"

        else:
            self.balance -= cantidad

            return True, (
                  f"✅ Retiro realizado con éxito.\n\n"
                  f"💵 Monto retirado: ${cantidad:,.2f}\n\n"
                  f"💰 Nuevo  saldo: ${self.balance:,.2f}"
)