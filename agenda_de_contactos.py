print("Agenda de Contactos".center(50,"+"))
contactos={} #diccionario vacio
for x in range (3):#ingreso de datos
    nombre=input("Ingrese un Nombre:\t")
    telefono=input("Ingrese el Numero del contacto:\t ")
    contactos[nombre]=telefono#guardar informacion en el diccionario

print("Busqueda".center(20,"."))
busqueda=input("Ingrese el nombre que quiere buscar:\t")
if busqueda in contactos:
    print(f"{busqueda}: {contactos[busqueda]}")
else:
    print("Contacto no encontrado")