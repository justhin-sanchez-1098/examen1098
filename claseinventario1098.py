print("examen1098")
print("justhin sanchez medina-22308051281098")
class Tacos1098:
    def __init__(self):
        # Atributos inicializados
        self.id_inventario = ""
        self.tipo_carne = ""
        self.kg_carne = ""
        self.tipo_salsa = ""
        self.tortillas = ""
        self.verduras = ""
        self.desechables = ""

    def mostrar_datos(self):
        print("Datos del inventario:")
        print(f"ID de inventario: {self.id_inventario}")
        print(f"Tipo de carne: {self.tipo_carne}")
        print(f"Cantidad de carne: {self.kg_carne}")
        print(f"Tipo de salsa: {self.tipo_salsa}")
        print(f"Tipo de tortillas: {self.tortillas}")
        print(f"Verduras: {self.verduras}")
        print(f"Desechables: {self.desechables}")

    def listar_salsas(self):
        salsas = ["estilo guacamole", "de arbol", "casera", "roja", "verde"]
        print("Lista de salsas:")
        for salsa in salsas:
            print(salsa)

    def tupla_tipos_de_carne(self):
        carnes = ("sirloin", "buche", "tripas", "Pastor", "bistec")
        return carnes

    def diccionario_productosyprecio(self):
        productosyprecio = {
            "kilo de carne  ": 100,
            "kilo de cebolla  ": 30,
            "platos desechables  ": 65,
            "kilo de tortilla  ": 20,
            "tipos de carne  ": "pastor y bistec"
        }
        print("Productos y precios:")
        for x, y in productosyprecio.items():
            print(f"{x}: {y}")

    def altas(self):
        print("La cantidad de carne vendida es alta.")

    def bajas(self):
        print("La cantidad de carne echada a perder es baja.")

# Crear el objeto
inventario = Tacos1098()

# Asignar datos a los atributos
inventario.tortillas = "amarilla"
inventario.kg_carne = "100 kg"
inventario.id_inventario = "260618"
inventario.tipo_carne = "molida de puerco"
inventario.tipo_salsa = "adobada"
inventario.verduras = "limón, cebolla, cilantro"
inventario.desechables = "platos y cucharas"

# Utilizar los métodos
inventario.mostrar_datos()
inventario.listar_salsas()
# Mostrar la tupla de tipos de carne
tipos_de_carne = inventario.tupla_tipos_de_carne()
print("Tipos de carne disponibles:", tipos_de_carne)
inventario.diccionario_productosyprecio()
inventario.altas()
inventario.bajas()

