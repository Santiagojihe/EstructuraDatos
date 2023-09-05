
class Usuario:
    def __init__(
        self,
        identificacion,
        nombre,
        fecha_nacimiento,
        ciudad_nacimiento,
        direccion,
        telefono,
        correo,
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo


class RegistroUsuarios:
    def __init__(self, capacidad_maxima):
        self.usuarios = []
        self.capacidad_maxima = capacidad_maxima
    def agregar_usuario(self, usuario):
        if len(self.usuarios) < self.capacidad_maxima:
            if not self.buscar_usuario_por_identificacion(usuario.identificacion):
                self.usuarios.append(usuario)
                self.usuarios.sort(key=lambda u: u.identificacion)
                return True
        return False
    def buscar_usuario_por_identificacion(self, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None
    def eliminar_usuario_por_identificacion(self, identificacion):
        usuario = self.buscar_usuario_por_identificacion(identificacion)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False
    def guardar_en_archivo(self, archivo):
        with open(archivo,'w') as file:
            file.write("Identificacion\tNombre\tFecha de Nacimiento\tCiudad de Nacimiento\tDireccion\tTelefono\tCorreo\n")
            for usuario in self.usuarios:
                file.write(f"{usuario.identificacion}\t{usuario.nombre}\t{usuario.fecha_nacimiento}\t{usuario.ciudad_nacimiento}\t{usuario.direccion}\t{usuario.telefono}\t{usuario.correo}\n")
    def cargar_desde_archivo(self, archivo):
        self.usuarios = []
        try:
            with open(archivo, 'r') as file:
                lines = file.readlines()
                if not lines:
                    print("El archivo está vacío.")
                    return
                header = lines[0].strip()
                if header != "Identificacion\tNombre\tFecha de Nacimiento\tCiudad de Nacimiento\tDireccion\tTelefono\tCorreo":
                    print("El archivo no tiene el formato esperado.")
                    return
                for line in lines[1:]:
                    row = line.strip().split('\t')
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    self.agregar_usuario(usuario)
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no fue encontrado.")
if __name__ == "__main__":
    capacidad_maxima = 100
    registro = RegistroUsuarios(capacidad_maxima)
    archivo = r'C:\Users\santi\Desktop\Estructuras tarea\usuarios.txt'
    registro.cargar_desde_archivo(archivo)
    while True:
        print("\nMenú:")
        print("1. Agregar un nuevo usuario")
        print("2. Eliminar un usuario por identificación")
        print("3. Mostrar todos los usuarios")
        print("4. Guardar en un archivo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            fecha_nacimiento = input("Fecha de Nacimiento (AAAA-MM-DD): ")
            ciudad_nacimiento = input("Ciudad de Nacimiento: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            nuevo_usuario = Usuario(identificacion, nombre, fecha_nacimiento, ciudad_nacimiento, direccion, telefono, correo)
            if registro.agregar_usuario(nuevo_usuario):
                print("Usuario agregado con éxito.")
            else:
                print("No se pudo agregar el usuario (capacidad máxima alcanzada).")
        elif opcion == "2":
            identificacion = input("Identificación del usuario a eliminar: ")
            if registro.eliminar_usuario_por_identificacion(identificacion):
                print("Usuario eliminado con éxito.")
            else:
                print("Usuario no encontrado.")
        elif opcion == "3":
            print("\nLista de Usuarios:")
            for usuario in registro.usuarios:
                print(f"Identificación: {usuario.identificacion}, Nombre: {usuario.nombre}")
        elif opcion == "4":
            registro.guardar_en_archivo(archivo)
            print("Datos guardados en el archivo 'usuarios.txt'.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
        
    

