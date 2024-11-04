# Pre Proyecto Final Integrador [PFI]
# 242C - Diego Schefer

"""
Requisitos de la Entrega
 
    1. Crear un menú interactivo

    Crear un menú interactivo utilizando bucles while y condicionales if-elif-else: 
    
        ● El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos. 
        ● Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados.
        
    2. Agregar productos al inventario
    
    Implementar la funcionalidad para agregar productos a una lista: 

        ● Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada.

    3. Mostrar el inventario
    
    Mostrar los productos ingresados:
    
        ● Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el  momento.

    
"""

# Inicio
producto = []
productos = []

CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
PURPLE = "\033[0;35m"
RED = "\033[0;31m"
BOLD = "\033[1m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
RESET = "\033[0m"


# Menu Principal

while True:

    print (("-") * 30)
    print(PURPLE + BOLD + "Menu de Opciones" + RESET)
    print (("-") * 30)    
    print(GREEN + "1. Alta")
    print("2. Modificacion")
    print("3. Eliminar")
    print("4. Listar")
    print("9. Precargar datos (Modo Debug)")
    print("0. Salir" + RESET)
    print (("-") * 30)

    opcion = int(input(CYAN + "Ingrese una opcion: " + RESET)) # input siembre retorna STR, lo trasnformo a INT
    # print(f"La Opcion Seleccionada fue {opcion}") # Si imprimo STR + INT se rompe el casteo al unirse
    print (("-") * 30)

    if opcion == 1:
        print (PURPLE + BOLD + "Alta de Producto" + RESET)
        print (("-") * 50)
      
        nombreProducto = input("Nombre de producto: ")

        precioProducto = float(input("Precio Actual: "))
        while precioProducto <= 0:
            print(RED + "El precio debe ser positivo" + RESET)
            precioProducto = float(input("Precio Actual: "))
    
        cantidadProducto = float(input("Cantidad Ingresada: "))       
        while cantidadProducto <= 0:
            print(RED + "El Stock debe ser positivo" + RESET)
            cantidadProducto = float(input("Cantidad Ingresada: "))
     
        productos.append([nombreProducto,precioProducto,cantidadProducto])
                

    elif opcion == 2:
        
        if len(productos) == 0:
            print(RED + BOLD + "Aun no tenemos productos cargados en el Sistema" + RESET)

        else:                      
            print ("Modificacion de Producto")
            print (("-") * 50)

            print("Selecciona el Indice del producto a Modificar")
            print (("-") * 50)
 
            for indice, listado in enumerate(productos):
                print(indice, listado)           
        
            modificarProducto =int(input(CYAN + "Indice de Producto: " + RESET))

            nombreProducto = input("Nombre de producto: ")

            precioProducto = float(input("Precio Actual: "))
        
            while precioProducto <= 0:
                print(RED + "El precio debe ser positivo" + RESET)
                precioProducto = float(input("Precio Actual: "))
        
            cantidadProducto = float(input("Cantidad Ingresada: "))       
            while cantidadProducto <= 0:
                print(RED + "El Stock debe ser positivo" + RESET)
                cantidadProducto = float(input("Cantidad Ingresada: "))
            
            productos[modificarProducto] = [nombreProducto,precioProducto,cantidadProducto] 

    elif opcion == 3:

        if len(productos) == 0:
            print(RED + BOLD + "Aun no tenemos productos cargados en el Sistema" + RESET)
        else:    

            print ("Eliminar Producto")
            print (("-") * 50)
 
            print(CYAN + "Selecciona el Indice del producto a Eliminar" + RESET)
            print (("-") * 50)
            
            for indice, listado in enumerate(productos):
                print(indice, listado)
        
            eliminarProducto =int(input(CYAN + "Indice de Producto: " + RESET))
            del productos[eliminarProducto]

    elif opcion == 4:

        if len(productos) == 0:
            print(RED + BOLD + "Aun no tenemos productos cargados en el Sistema" + RESET)
        else:
            print ("Listado de Productos")
            print (("-") * 50)

            print("Nombre".ljust(30) + "Precio".ljust(10) + "Cantidad")
            for producto in productos:
                print(f"{producto[0].ljust(30)}{str(producto[1]).ljust(10)}{str(producto[2])}")
       
    elif opcion == 9:

        productos = [
            ["Tortas de Chocolate", 4500, 5.0],
            ["Tortas de Vainilla", 2999.99 , 4.5],
            ["Tortas de Crema", 5100, 7.0],
            ["Tortas de Cereza", 2650, 6.25],
            ["Tortas de Ricota", 3400, 10.75],
        ]        

    elif opcion == 0:
        print(RED + "Saliendo... Muchas gracias por evaluar este Sistema!" + RESET)
        break
        
    else:
        print(RED + "Opcion Invalida, Selecciona nuevamente" + RESET)
    
