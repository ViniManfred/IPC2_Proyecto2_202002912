import os 
import sys
import subprocess
from E_transacciones import E_Transacciones
from empresas import Empresas
from puntos_atencion import Puntos_Atencion
from E_escritorios import Escritorios
from E_transacciones import E_Transacciones
from config_inicial import config_inicial
from CI_escritorios import CI_Escritorios
from clientes import Clientes
from CI_transacciones import CI_Transacciones
from LE_config_inicial import Lista_CI
from LE_empresas import Lista_E
import xml.etree.ElementTree as ET
from colorama import Fore
listaConfigDesdeXml = Lista_CI()
listaEmpresasDesdeXml = Lista_E()

def menu():
    opcion = ''
    #listaPacientes = Lista_P()
    #Ejecuta las opciones del menu
    while opcion != "Break":
        print(Fore.YELLOW+"\n----------------------------------")
        print(Fore.YELLOW+"  SOLUCIONES GUATEMALTECAS S.A.   ")
        print(Fore.YELLOW+"----------MENU DE INICIO----------")
        print(Fore.YELLOW+"  1. CONFIGURACION DE EMPRESAS")
        print(Fore.YELLOW+"  2. SELECT EMPRESA Y PUNTO DE A.")
        print(Fore.YELLOW+"  3. MANEJO DE PUNTOS DE ATENCION")
        print(Fore.YELLOW+"  8. MOSTRAR EMPRESAS")
        print(Fore.YELLOW+"  9. SALIR")
        print(Fore.YELLOW+"----------------------------------")

        opcion = input(Fore.YELLOW+"Seleccione una opcion del menu \n")
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            seleccionado=select()
        elif opcion == '3':
            seleccionado.E_escritorios.print()
        elif opcion== "8":
            listaEmpresasDesdeXml.printer()
        elif opcion== "9":
            print(Fore.GREEN+"Saliendo...\n")
            break
        else:
            print(Fore.RED+"Por favor seleccione una opcion valida.")


#Carga el archivo Xml lo lee y genera las listas correspondientes
def cargaArchivo_E(ruta):
    tree = ET.parse(ruta)
    archivo = tree.getroot()
    for EmpresasXml in archivo:    
            contador=int(listaEmpresasDesdeXml.ultimo.counter)+1
            nuevaE = Empresas(contador,EmpresasXml.attrib["id"],EmpresasXml.find('nombre').text,EmpresasXml.find('abreviatura').text)
            listaEmpresasDesdeXml.append(nuevaE)
            for lpaXml in EmpresasXml.iter('listaPuntosAtencion'):
                for paXml in lpaXml.iter('puntoAtencion'):
                    contador1=int(nuevaE.puntos_atencion.ultimo.counter)+1
                    nuevoPA = Puntos_Atencion(contador1,paXml.attrib["id"], paXml.find('nombre').text, paXml.find('direccion').text)
                    nuevaE.puntos_atencion.append(nuevoPA)
                    for leXml in paXml.iter('listaEscritorios'):
                        for escritorioXml in leXml.iter('escritorio'):
                            estado = "inactivo"
                            nuevoE = Escritorios(escritorioXml.attrib["id"], escritorioXml.find('identificacion').text, escritorioXml.find('encargado').text,estado)
                            nuevoPA.E_escritorios.append(nuevoE)
            for lTXml in EmpresasXml.iter('listaTransacciones'):
                for transaccionXml in lTXml.iter('transaccion'):
                    nuevaT = E_Transacciones(transaccionXml.attrib["id"], transaccionXml.find('nombre').text, transaccionXml.find('tiempoAtencion').text)
                    nuevaE.E_transacciones.append(nuevaT)

def cargaArchivo_CI(ruta):
    tree = ET.parse(ruta)
    archivo = tree.getroot()
    for configXml in archivo:
        nuevaCI = config_inicial(configXml.attrib["id"], configXml.attrib["idEmpresa"], configXml.attrib["idPunto"])
        listaConfigDesdeXml.append(nuevaCI)
        for escActivosXml in configXml.iter('escritoriosActivos'):
            for escXml in escActivosXml.iter('escritorio'):
                nuevoEA = CI_Escritorios(escXml.attrib["idEscritorio"])
                nuevaCI.CI_escritorios.append(nuevoEA)
        for listclientXml in configXml.iter('listadoClientes'):
            for clientXml in listclientXml.iter('cliente'):
                nuevoC = Clientes(clientXml.attrib["dpi"], clientXml.find('nombre').text)
                nuevaCI.clientes.append(nuevoC)
                for listTransXml in clientXml.iter('listadoTransacciones'):
                    for TransXml in listTransXml.iter('transaccion'):
                        nuevaTI = CI_Transacciones(TransXml.attrib["idTransaccion"], TransXml.attrib["cantidad"])
                        nuevoC.transacciones.append(nuevaTI)

def opcion1():
    opcion2 = ""
    while opcion2 != 'Break':
        print(Fore.BLUE+"\n----------------------------------")
        print(Fore.BLUE+"  SOLUCIONES GUATEMALTECAS S.A.   ")
        print(Fore.BLUE+"--------MENU CONFIGURACION--------")
        print(Fore.BLUE+"  1. LIMPIAR SISTEMA")
        print(Fore.BLUE+"  2. CARGAR LISTA DE EMPRESAS")
        print(Fore.BLUE+"  3. CARGAR CONFIGURACION INICIAL")
        print(Fore.BLUE+"  4. CREAR NUEVA EMPRESA")
        print(Fore.BLUE+"  5. VOLVER AL MENU DE INICIO")
        print(Fore.BLUE+"----------------------------------")

        opcion2 = input(Fore.BLUE+"Seleccione una opcion del menu \n")
        if opcion2 == '1':
            print(Fore.GREEN+"Inicializando...\n")
            subprocess.call([sys.executable, os.path.realpath("./inicio.py")]+sys.argv[1:])
        elif opcion2 == "2":
            try:
                #nombreArchivo1 = input(Fore.BLUE+"Ingrese el nombre del archivo XML\n")
                ruta1 = './plantillaSusEmpresa.xml'#+nombreArchivo1
                cargaArchivo_E(ruta1)
                print(Fore.GREEN+"Se cargo el archivo con exito!")
            except:
                print(Fore.RED+"Error: Inserte una ruta correcta\no archivo con formato de entrada Valido.")
        elif opcion2 == "3":
            try:
                #nombreArchivo2 = input(Fore.BLUE+"Ingrese el nombre del archivo XML\n")
                ruta2 = './plantillaSusCliente.xml'#+nombreArchivo2
                cargaArchivo_CI(ruta2)
                print(Fore.GREEN+"Se cargo el archivo con exito!")
            except:
                print(Fore.RED+"Error: Inserte una ruta correcta\no archivo con formato de entrada Valido.")
        elif opcion2=="4":
            print(Fore.MAGENTA+"----------------------------------")
            print(Fore.MAGENTA+"Ingrese la informacion que se le solicita para suscribir\nsu empresa al servicio de SOLUCIONES GUATEMALTECAS S.A.\n")
            contador=int(listaEmpresasDesdeXml.ultimo.counter)+1
            a = input(Fore.MAGENTA+"Ingrese el id de la empresa:\n")
            b=input(Fore.MAGENTA+"Ingrese el nombre de la empresa:\n")
            c=input(Fore.MAGENTA+"Ingrese la abreviatura de la empresa:\n")
            nuevaE= Empresas(contador,a,b,c)
            listaEmpresasDesdeXml.append(nuevaE)
            opcion3=""
            while opcion3 != "Break":
                print(Fore.YELLOW+"\n----------------------------------")
                print(Fore.YELLOW+"  SOLUCIONES GUATEMALTECAS S.A.   ")
                print(Fore.YELLOW+"--------MENU CREAR SUBLISTA-------")
                print(Fore.YELLOW+"  1. AGREGAR PUNTO ATENCION")
                print(Fore.YELLOW+"  2. AGREGAR TRANSACCION")
                print(Fore.YELLOW+"  3. TERMINAR DE CREAR")
                print(Fore.YELLOW+"----------------------------------")
                opcion3 = input(Fore.YELLOW+"Seleccione una opcion del menu \n")
                if opcion3 == '1':
                    print(Fore.CYAN+"\n----------------------------------")
                    print(Fore.CYAN+"Ingrese la informacion que se le solicita para\nagregar un punto de atencion a su empresa.")
                    d = input(Fore.CYAN+"Ingrese el id del punto de atencion:\n")
                    e=input(Fore.CYAN+"Ingrese el nombre del punto de atencion:\n")
                    f=input(Fore.CYAN+"Ingrese direccion del punto de atencion:\n")
                    contador1=int(nuevaE.puntos_atencion.ultimo.counter)+1
                    nuevoPA = Puntos_Atencion(contador1,d,e,f)
                    nuevaE.puntos_atencion.append(nuevoPA)
                    opcion4=""
                    while opcion4 != "Break":
                        print(Fore.YELLOW+"\n----------------------------------")
                        print(Fore.YELLOW+"  SOLUCIONES GUATEMALTECAS S.A.   ")
                        print(Fore.YELLOW+"----------------MENU--------------")
                        print(Fore.YELLOW+"  1. AGREGAR ESCRITORIO")
                        print(Fore.YELLOW+"  2. VOLVER")
                        print(Fore.YELLOW+"----------------------------------")
                        opcion4 = input(Fore.YELLOW+"Seleccione una opcion del menu \n")
                        if opcion4 == '1':
                            print(Fore.BLUE+"\n----------------------------------")
                            print(Fore.BLUE+"Ingrese la informacion que se le solicita para\nagregar un escritorio al punto de atención.")
                            g = input(Fore.BLUE+"Ingrese el id del escritorio:\n")
                            h=input(Fore.BLUE+"Ingrese la identificacion del escritorio:\n")
                            i=input(Fore.BLUE+"Ingrese el nombre del encargado del escritorio:\n")
                            nuevoE = Escritorios(g, h, i,"inactivo")
                            nuevoPA.E_escritorios.append(nuevoE)
                        elif opcion4 == '2':
                            break
                        else:
                            print(Fore.RED+"Por favor seleccione una opcion valida.")
                elif opcion3 =="2":
                    print(Fore.CYAN+"\n----------------------------------")
                    print(Fore.CYAN+"Ingrese la informacion que se le solicita\npara agregar una transaccion a su empresa.")
                    j = input(Fore.CYAN+"Ingrese el id de la transaccion:\n")
                    k=input(Fore.CYAN+"Ingrese el nombre de la transaccion:\n")
                    while True:
                        l = input(Fore.CYAN+"Ingrese el tiempo de atencion (minutos) de la transaccion:\n")
                        if l.isdigit():
                            break
                        else:
                            print(Fore.RED+"Error: Solo se permite ingresar digitos")
                    nuevaT = E_Transacciones(j, k, l)
                    nuevaE.E_transacciones.append(nuevaT)
                elif opcion3 =="3":
                    break
                else:
                    print(Fore.RED+"Error: Seleccione una opcion valida.")
        elif opcion2=="5":
            break
        else:
            print(Fore.RED+"Error: seleccione una opcion valida.")

def select():
    print(Fore.LIGHTBLUE_EX+"\n----------------------------------")
    print(Fore.LIGHTBLUE_EX+"  SOLUCIONES GUATEMALTECAS S.A.   ")
    print(Fore.LIGHTBLUE_EX+"--------MENU  DE EMPRESAS---------")
    listaEmpresasDesdeXml.print()
    print(Fore.LIGHTBLUE_EX+"----------------------------------")
    while True:
        a= input(Fore.LIGHTBLUE_EX+"Elija la empresa que desea gestionar:\n")
        empresa = listaEmpresasDesdeXml.busqueda(int(a))
        if empresa is None:
            print(Fore.RED + "Error: Seleccione una opcion correcta.")
        else:
            break
    print(Fore.MAGENTA+"\n----------------------------------")
    print(Fore.MAGENTA+"  SOLUCIONES GUATEMALTECAS S.A.   ")
    print(Fore.MAGENTA+"--------PUNTOS DE ATENCION--------")
    empresa.puntos_atencion.print()
    print(Fore.MAGENTA+"----------------------------------")
    while True:
        b= input(Fore.MAGENTA+"Elija el punto de atencion que desea gestionar:\n")
        punto = empresa.puntos_atencion.busqueda(int(b))
        if punto is None:
            print(Fore.RED + "Error: Seleccione una opcion correcta.")
        else:
            break
    print(Fore.GREEN+"Empresa y punto de atencion elegidos correctamente!")
    return punto
        
menu()
