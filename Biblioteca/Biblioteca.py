class Material:
    def __init__(self,idMaterial, titulo, anoPublicacion, disponible):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.anoPublicacion = anoPublicacion
        self.disponible = disponible

class Libro(Material):
    def __init__(self, idMaterial, titulo, autor, genero, anoPublicacion, isbn, disponible):
        super().__init__(idMaterial, titulo, anoPublicacion, disponible)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

        print(f"\nLibros disponibles:")
        print(f"ID: {self.idMaterial}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Año de publicación: {self.anoPublicacion}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")

class Revista(Material):
    def __init__(self, idMaterial, titulo, edicion, periodicidad, anoPublicacion, disponible):
        super().__init__(idMaterial, titulo, anoPublicacion, disponible)
        self.edicion = edicion
        self.periodicidad = periodicidad

        print(f"\nRevistas disponibles:")
        print(f"ID: {self.idMaterial}")
        print(f"Título: {self.titulo}")
        print(f"Edición: {self.edicion}")
        print(f"Periodicidad: {self.periodicidad}")
        print(f"Año de publicación: {self.anoPublicacion}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")

class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, anoPublicacion,  urlDescarga, tipoArchivo, tamanoMB, disponible):
        super().__init__(idMaterial, titulo, anoPublicacion, disponible)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamanoMB = tamanoMB

        print(f"\nMateriales digitales disponibles:")
        print(f"ID: {self.idMaterial}")
        print(f"Título: {self.titulo}")
        print(f"Año de publicación: {self.anoPublicacion}")
        print(f"URL de descarga: {self.urlDescarga}")
        print(f"Tipo de archivo: {self.tipoArchivo}")
        print(f"Tamaño: {self.tamanoMB} MB")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")

class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, limitePrestamos):
        super().__init__(idPersona, nombre, email)
        self.limitePrestamos = limitePrestamos
        self.listaActiva = []

        print(f"\nUsuario:")
        print(f"ID: {self.idPersona}")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Límite de préstamos: {self.limitePrestamos}")

class Bibliotecario(Persona):
    def __init__(self, idPersona, nombre, email):
        super().__init__(idPersona, nombre, email)

    def gestionarPrestamo(self, usuario, prestamo):
        if len(usuario.listaActiva) < usuario.limitePrestamos:   
            usuario.listaActiva.append(prestamo)
            prestamo.material.disponible = False
            print(f"\n{self.nombre} hizo el préstamo para {usuario.nombre}")
        else:
            print(f"\n{usuario.nombre} alcanzo el limite permitido de préstamos.")
    
    def transferirMaterial(self, sucursalDestino):
        print(f"El bibliotecario {self.nombre} transfiere material a {sucursalDestino.nombre}")

class Sucursal:
    def __init__(self, idSucursal, nombre, catalogoLocal=None):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = catalogoLocal if catalogoLocal else []
        
        print(f"\nSucursales:")
        print(f"ID: {self.idSucursal}")
        print(f"Nombre: {self.nombre}")
        print(f"Materiales en catálogo local: {len(self.catalogoLocal)}")

class Prestamo:
    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, usuario: Usuario, material: Material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material
        print(f"\nNuevo préstamo:")
        print(f"ID: {self.idPrestamo}")
        print(f"Usuario: {self.usuario.nombre}")
        print(f"Material: {self.material.titulo}")
        print(f"Fecha de inicio: {self.fechaInicio}")
        print(f"Fecha de devolución: {self.fechaDevolucion}")

class Penalizacion:
    def __init__(self, monto=0, motivo="", pagada=False):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada

    def calcularMulta(self, diasRetraso):
        if diasRetraso > 0:
            self.monto = diasRetraso * 5
            self.motivo = f"Retraso de {diasRetraso} días"
            self.pagada = False
            print(f"\nMotivo: {self.motivo}")
            print(f"Multa a pagar: ${self.monto}")
        else:
            print("\nNo hay retraso")

    def bloquearUsuario(self, usuario):
        if not self.pagada and self.monto > 0:
            print(f"\n{usuario.nombre} ha sido bloqueado por: {self.motivo}")
        else:
            print(f"\n{usuario.nombre} no tiene penalización")

class Catalogo:

    def __init__(self, sucursales):
        self.sucursales = sucursales

    def buscarPorAutor(self, autor):    
        resultados = []
        for sucursal in self.sucursales:
            for material in sucursal.catalogoLocal:
                if isinstance(material, Libro) and material.autor == autor:
                    resultados.append(material)
        if not resultados:
            print(f"\nNo se encontraron los libros del autor: {autor}")
        return resultados
    
    def buscarEnTodasSucursales(self, titulo):
        resultados = []
        for sucursal in self.sucursales:
            for material in sucursal.catalogoLocal:
                if material.titulo == titulo:
                    resultados.append(material)
        
        if not resultados:
            print(f"\nNo se encontró el material: {titulo}") 
        return resultados