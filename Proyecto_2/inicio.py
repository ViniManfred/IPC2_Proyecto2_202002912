import os 
import sys
import subprocess
from E_transacciones import E_Transacciones
from empresas import Empresas
from puntos_atencion import Puntos_Atencion
from E_escritorios import Escritorios
from E_transacciones import E_Transacciones
from pila import Pila
from clientes import Clientes
from clientes_escritorio import Clientes_escritorio
from cola import Cola
from LE_empresas import Lista_E
import xml.etree.ElementTree as ET
from colorama import Fore
class inicio:
    listaEmpresasDesdeXml = Lista_E()

    def menu(self):
        opcion = ''
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
                self.opcion1()
            elif opcion == '2':
                seleccionado=self.select()
            elif opcion == '3':
                opcion1=""
                while opcion1 != "Break":
                    print(Fore.BLUE+"\n----------------------------------")
                    print(Fore.BLUE+"  SOLUCIONES GUATEMALTECAS S.A.   ")
                    print(Fore.BLUE+"-----MANEJO PUNTO DE ANTENCION----")
                    print(Fore.BLUE+"  1. ESTADO DEL PUNTO DE ATENCION")
                    print(Fore.BLUE+"  2. ACTIVAR ESCRITORIO")
                    print(Fore.BLUE+"  3. DESACTIVAR ESCRITORIO")
                    print(Fore.BLUE+"  4. ATENDER CLIENTE")
                    print(Fore.BLUE+"  5. SOLICITUD DE ATENCION")
                    print(Fore.BLUE+"  6. SIMULAR ACTIVIDAD DEL P.A.")
                    print(Fore.BLUE+"  7. VOLVER AL MENU DE INICIO")
                    print(Fore.BLUE+"----------------------------------")
                    opcion1 = input(Fore.BLUE+"Seleccione una opcion del menu \n")
                    if opcion1 == '1':
                        self.estado_PA(seleccionado)
                    elif opcion1 == '2':
                        print(Fore.CYAN+"\n----------------------------------")
                        print(Fore.CYAN+"  SOLUCIONES GUATEMALTECAS S.A.   ")
                        print(Fore.CYAN+"--------ACTIVAR ESCRITORIOS-------")
                        seleccionado.E_escritorios.print_inactivos()
                        print(Fore.CYAN+"----------------------------------")
                        track = input(Fore.CYAN+"Seleccione el escritorio que desea activar\n")
                        encontrado = seleccionado.E_escritorios.busqueda_desactivos(int(track))
                        while True:
                            if encontrado is None:
                                print(Fore.RED + "Error: Seleccione el escritorio correctamente.")
                            else:
                                nuevaPila = Pila(encontrado.counter,encontrado.id,encontrado.identificacion,encontrado.encargado,"activo")
                                seleccionado.pila.append(nuevaPila)
                                nuevoCE = Clientes_escritorio(seleccionado.cola.raiz.counter,seleccionado.cola.raiz.dpi,seleccionado.cola.raiz.nombre,seleccionado.cola.raiz.tiempo_atencion,seleccionado.cola.raiz.tiempo_espera)
                                encontrado.clientes_escritorio.append(nuevoCE)
                                seleccionado.cola.desencolar()
                                print(Fore.GREEN+"Se ha activado el escritorio correctamente!")
                                break
                    elif opcion1=="3":
                        try:
                            seleccionado.pila.desapilar()
                            print(Fore.GREEN+"Se ha desactivado el escritorio correctamente!")
                        except:
                            print(Fore.RED+"No hay escritorios por desactivar.")
                    elif opcion1=="4":
                        seleccionado.pila.printer()
                        encontrado.clientes_escritorio.print()

                    elif opcion1 == "7":
                        break
            elif opcion== "8":
                self.listaEmpresasDesdeXml.printer()
            elif opcion== "9":
                print(Fore.GREEN+"Saliendo...\n")
                break
            else:
                print(Fore.RED+"Por favor seleccione una opcion valida.")


    #Carga el archivo Xml lo lee y genera las listas correspondientes
    def cargaArchivo_E(self,ruta):
        tree = ET.parse(ruta)
        archivo = tree.getroot()
        for EmpresasXml in archivo:    
                contador=int(self.listaEmpresasDesdeXml.ultimo.counter)+1
                nuevaE = Empresas(contador,EmpresasXml.attrib["id"],EmpresasXml.find('nombre').text,EmpresasXml.find('abreviatura').text)
                self.listaEmpresasDesdeXml.append(nuevaE)
                for lpaXml in EmpresasXml.iter('listaPuntosAtencion'):
                    for paXml in lpaXml.iter('puntoAtencion'):
                        contador1=int(nuevaE.puntos_atencion.ultimo.counter)+1
                        nuevoPA = Puntos_Atencion(contador1,paXml.attrib["id"], paXml.find('nombre').text, paXml.find('direccion').text)
                        nuevaE.puntos_atencion.append(nuevoPA)
                        for leXml in paXml.iter('listaEscritorios'):
                            for escritorioXml in leXml.iter('escritorio'):
                                contador2=int(nuevoPA.E_escritorios.ultimo.counter)+1
                                estado = "inactivo"
                                nuevoE = Escritorios(contador2,escritorioXml.attrib["id"], escritorioXml.find('identificacion').text, escritorioXml.find('encargado').text,estado)
                                nuevoPA.E_escritorios.append(nuevoE)
                for lTXml in EmpresasXml.iter('listaTransacciones'):
                    for transaccionXml in lTXml.iter('transaccion'):
                        nuevaT = E_Transacciones(transaccionXml.attrib["id"], transaccionXml.find('nombre').text, transaccionXml.find('tiempoAtencion').text)
                        nuevaE.E_transacciones.append(nuevaT)

    def cargaArchivo_CI(self,ruta):
        tree = ET.parse(ruta)
        archivo = tree.getroot()
        for configXml in archivo:
            empresa = self.listaEmpresasDesdeXml.busquedaID(configXml.attrib["idEmpresa"])
            if empresa is None:
                print(Fore.RED + "Error: No se encontro la empresa.")
            else:
                punto = empresa.puntos_atencion.busquedaID(configXml.attrib["idPunto"])
                if punto is None:
                    print(Fore.RED + "Error: No se encontro el Punto de Atencion.")
                else:
                    tiempo = 0
                    for listclientXml in configXml.iter('listadoClientes'):
                        for clientXml in listclientXml.iter('cliente'):
                            contador3=int(punto.clientes.ultimo.counter)+1
                            time=0
                            for listTransXml in clientXml.iter('listadoTransacciones'):
                                for TransXml in listTransXml.iter('transaccion'):
                                    transaccion = empresa.E_transacciones.busquedaID(TransXml.attrib["idTransaccion"])
                                    if transaccion is None:
                                        print(Fore.RED + "Error: No se encontro la transaccion.")
                                    else:
                                        tiempo_atencion=float(transaccion)*float(TransXml.attrib["cantidad"])
                                        time+=tiempo_atencion
                                        myRoundNumber = round(time, 2)
                            tiempo+=myRoundNumber
                            espera=tiempo-myRoundNumber
                            myRoundNumber2 = round(espera, 2)
                            nuevoC = Clientes(contador3,clientXml.attrib["dpi"], clientXml.find('nombre').text,myRoundNumber, myRoundNumber2)
                            nuevaCola = Cola(contador3,clientXml.attrib["dpi"], clientXml.find('nombre').text,myRoundNumber, myRoundNumber2)
                            punto.clientes.append(nuevoC)
                            punto.cola.append(nuevaCola)
                    for escActivosXml in configXml.iter('escritoriosActivos'):
                        for escXml in escActivosXml.iter('escritorio'):
                            escrit = punto.E_escritorios.busquedaID(escXml.attrib["idEscritorio"])
                            if escrit is None:
                                print(Fore.RED + "Error: No se encontro el Escritorio.")
                            else:
                                escrit.estado="activo"
                                nuevaPila = Pila(escrit.counter, escrit.id,escrit.identificacion,escrit.encargado,"activo")
                                punto.pila.append(nuevaPila)
                                
                                nuevoCE = Clientes_escritorio(punto.cola.raiz.counter,punto.cola.raiz.dpi,punto.cola.raiz.nombre,punto.cola.raiz.tiempo_atencion,punto.cola.raiz.tiempo_espera)
                                escrit.clientes_escritorio.append(nuevoCE)
                                punto.cola.desencolar()

    def opcion1(self):
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
                    self.cargaArchivo_E(ruta1)
                    print(Fore.GREEN+"Se cargo el archivo con exito!")
                except:
                    print(Fore.RED+"Error: Inserte una ruta correcta\no archivo con formato de entrada Valido.")
            elif opcion2 == "3":
                try:
                    #nombreArchivo2 = input(Fore.BLUE+"Ingrese el nombre del archivo XML\n")
                    ruta2 = './plantillaSusCliente.xml'#+nombreArchivo2
                    self.cargaArchivo_CI(ruta2)
                    print(Fore.GREEN+"Se cargo el archivo con exito!")
                except:
                    print(Fore.RED+"Error: Inserte una ruta correcta\no archivo con formato de entrada Valido.")
            elif opcion2=="4":
                print(Fore.MAGENTA+"----------------------------------")
                print(Fore.MAGENTA+"Ingrese la informacion que se le solicita para suscribir\nsu empresa al servicio de SOLUCIONES GUATEMALTECAS S.A.\n")
                contador=int(self.listaEmpresasDesdeXml.ultimo.counter)+1
                a = input(Fore.MAGENTA+"Ingrese el id de la empresa:\n")
                b=input(Fore.MAGENTA+"Ingrese el nombre de la empresa:\n")
                c=input(Fore.MAGENTA+"Ingrese la abreviatura de la empresa:\n")
                nuevaE= Empresas(contador,a,b,c)
                self.listaEmpresasDesdeXml.append(nuevaE)
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
                                contador2=int(nuevoPA.E_escritorios.ultimo.counter)+1
                                nuevoE = Escritorios(contador2,g, h, i,"inactivo")
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

    def select(self):
        print(Fore.LIGHTBLUE_EX+"\n----------------------------------")
        print(Fore.LIGHTBLUE_EX+"  SOLUCIONES GUATEMALTECAS S.A.   ")
        print(Fore.LIGHTBLUE_EX+"--------MENU  DE EMPRESAS---------")
        self.listaEmpresasDesdeXml.print()
        print(Fore.LIGHTBLUE_EX+"----------------------------------")
        while True:
            a= input(Fore.LIGHTBLUE_EX+"Elija la empresa que desea gestionar:\n")
            empresa = self.listaEmpresasDesdeXml.busqueda(int(a))
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
    
    def estado_PA(self, seleccionado):
        opcion2=""
        while opcion2 != "Break":
            print(Fore.MAGENTA+"\n----------------------------------")
            print(Fore.MAGENTA+"  SOLUCIONES GUATEMALTECAS S.A.   ")
            print(Fore.MAGENTA+"-------PUNTO DE ANTENCION------")
            print(Fore.MAGENTA+"  1. ESCRITORIOS")
            print(Fore.MAGENTA+"  2. CLIENTES EN ESPERA")
            print(Fore.MAGENTA+"  3. GESTION DE TIEMPOS")
            print(Fore.MAGENTA+"  4. VOLVER")
            print(Fore.BLUE+"----------------------------------")
            opcion2 = input(Fore.MAGENTA+"Seleccione una opcion del menu \n")
            if opcion2 == '1':
                activos=seleccionado.E_escritorios.busqueda_estado("activo")
                inactivos=seleccionado.E_escritorios.busqueda_estado("inactivo")
                print(Fore.CYAN+"\n----------------------------------")
                print(Fore.CYAN+"            ESCRITORIOS           ")
                print(Fore.CYAN+"----------------------------------")
                print(Fore.CYAN+" Escritorios activos: ",activos)
                print(Fore.CYAN+" Escritorios inactivos: ",inactivos)
                print(Fore.CYAN+"----------------------------------")
            elif opcion2=="2":
                try:
                    print(Fore.CYAN+"\n----------------------------------")
                    print(Fore.CYAN+"       CLIENTES EN ESPERA         ")
                    print(Fore.CYAN+"----------------------------------")
                    seleccionado.cola.print()
                    print(Fore.CYAN+"----------------------------------")
                except:
                    print(Fore.RED+"No hay clientes por atender.")
            elif opcion2=="3":
                try:
                    espera_promedio = seleccionado.clientes.espera_promedio()
                    atencion_promedio = seleccionado.clientes.atencion_promedio()
                    maximo = seleccionado.clientes.atencion_maxima()
                    minimo = seleccionado.clientes.atencion_minima()
                    maximo1 = seleccionado.clientes.espera_maxima()
                    minimo1 = seleccionado.clientes.espera_minima()
                    print(Fore.CYAN+"\n----------------------------------")
                    print(Fore.CYAN+"              TIEMPOS             ")
                    print(Fore.CYAN+"----------------------------------")
                    print(Fore.CYAN+" Tiempo promedio de espera:",espera_promedio)
                    print(Fore.CYAN+" Tiempo maximo de espera:",maximo1)
                    print(Fore.CYAN+" Tiempo minimo de espera:",minimo1)
                    print(Fore.CYAN+" Tiempo promedio de atencion:",atencion_promedio)
                    print(Fore.CYAN+" Tiempo maximo de atencion:",maximo)
                    print(Fore.CYAN+" Tiempo minimo de atencion:",minimo)
                    print(Fore.CYAN+"----------------------------------")
                except:
                    print(Fore.RED+"No hay clientes por atender.")
            elif opcion2=="4":
                break
            else:
                print(Fore.RED+"Por favor seleccione una opcion valida.")

p1=inicio()        
p1.menu()
