from ArbolBinario import ArbolBinarioBusqueda

abb = ArbolBinarioBusqueda()


class Usuario:
    def __init__(self, nombre, numero_identificacion):
        self.nombre = nombre
        self.numero_identificacion = numero_identificacion

    def calcular_clave(self):
        # Suma de los dígitos del número de identificación
        return sum(int(digit) for digit in str(self.numero_identificacion))


def mostrar_menu():
    print("1. Agregar usuario")
    print("2. Eliminar usuario por clave")
    print("3. Mostrar el árbol")
    print("4. InOrder")
    print("5. Valor Maximo")
    print("6. Valor Minimo")
    print("7. buscar")
    print("8. Salir")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        numero_identificacion = int(input("Ingrese el número de identificación: "))
        usuario = Usuario(nombre, numero_identificacion)
        clave = usuario.calcular_clave()
        abb.insertar(
            clave, numero_identificacion
        )  # esta parte se puede modificar para que al imprimir imprima lo que son identificacion o nombre junto a la clave
        print(f"Usuario '{nombre}' agregado con clave {clave}.")
    elif opcion == "2":
        clave_a_eliminar = int(input("Ingrese la clave del usuario a eliminar: "))
        usuario_eliminado = abb.buscar(clave_a_eliminar)
        if usuario_eliminado:
            print(
                f"Usuario '{usuario_eliminado}' eliminado."
            )  # aqui nos muestra el usuario que se elimino con su identificacion
            abb.eliminar(clave_a_eliminar)
        else:
            print("Usuario no encontrado.")
    elif opcion == "3":
        abb.mostrar_arbol()
    elif opcion == "4":
        # Recorrido inorder para mostrar las claves de los nodos
        recorrido = abb.recorrido_inorder()
        print("Recorrido inorder de claves:", recorrido)
    elif opcion == "5":
        # Valor máximo
        valor_maximo = abb.valor_maximo()
        if valor_maximo:
            print(f"Valor máximo Clave: {valor_maximo}")
        else:
            print("Árbol vacío, no hay valor máximo.")
    elif opcion == "6":
        # Valor mínimo
        valor_minimo = abb.valor_minimo()
        if valor_minimo:
            print(f"Valor mínimo Clave: {valor_minimo}")
        else:
            print("Árbol vacío, no hay valor mínimo.")
    elif opcion == "7":
        clave_busqueda = int(input("escriba la clave a buscar:"))
        encontrado = abb.buscar(clave_busqueda)
        print(f"la identificacion de esa clave es:{encontrado}")
    elif opcion == "8":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

# abb.insertar(10101013, "Juan")
# abb.insertar(10001011, "Pablo")
# abb.insertar(10101015, "Maria")
# abb.insertar(1010000, "Ana")
# abb.insertar(10111105, "Diana")
# abb.insertar(10110005, "Mateo")
# abb.mostrar_arbol()
