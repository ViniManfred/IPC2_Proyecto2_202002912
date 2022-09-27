from Pacientes import Pacientes
from LE_Pacientes import Lista_P
from Datos_Personales import Datos_Personales
from Contagiados import Contagiados
from sanos import sanos
import xml.etree.ElementTree as ET

def menu():
    opcion = ''
    listaPacientes = Lista_P()
    #Ejecuta las opciones del menu
    while opcion != '3':
        print("---------------MENU---------------")
        print("  1. CARGAR ARCHIVO XML")
        print("  2. MOSTRAR PACIENTES")
        print("  3. SALIR")

        opcion = input("Seleccione una opcion del menu \n")
        if opcion == '1':
            try:
                ruta = './Prueba1.xml'
                listaPacientes = cargaArchivo(ruta)
                print("Se cargo el archivo con exito!!\n")
            except:
                print("Inserte una ruta correcta")
        elif opcion == '2':
            listaPacientes.print()  
#Carga el archivo Xml lo lee y genera las listas correspondientes
def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    pacientes = tree.getroot()
    listaPacientesDesdeXml = Lista_P()
    for pacienteXml in pacientes:    
        for periodosXml in pacienteXml.iter('periodos'):
            periodo= periodosXml.text
        for mXml in pacienteXml.iter('m'):
            m=mXml.text
        nuevoPaciente = Pacientes(periodo, m)
        listaPacientesDesdeXml.append(nuevoPaciente)
                
        for rejillasXml in pacienteXml.iter('rejilla'):
            for celdaXml in rejillasXml.iter("celda"):    
                f=celdaXml.attrib['f']
                c=celdaXml.attrib['c']
                nuevoContagiado = Contagiados(f,c)
                nuevoPaciente.contagiados.append(nuevoContagiado)
        if nuevoPaciente.contagiados.raiz.f is not None:
            for fila in range(int(m)):
                for columna in range(int(m)):
                    if fila == int(nuevoPaciente.contagiados.raiz.f) and columna == int(nuevoPaciente.contagiados.raiz.c):
                        estado_1="contagiado"
                        nuevoSano = sanos(fila, columna,estado_1)
                        nuevoPaciente.sanos.append(nuevoSano)
                        if nuevoPaciente.contagiados.raiz.siguiente is not None:
                            nuevoPaciente.contagiados.raiz = nuevoPaciente.contagiados.raiz.siguiente    
                    else:
                        estado_2="sano"
                        nuevoSano = sanos(fila, columna,estado_2)
                        nuevoPaciente.sanos.append(nuevoSano)
        else:
            for fila in range(int(m)):
                for columna in range(int(m)):
                        estado_2="sano"
                        nuevoSano = sanos(fila, columna,estado_2)
                        nuevoPaciente.sanos.append(nuevoSano)   

        for dpXml in pacienteXml.iter('datospersonales'):
            for nombreXml in dpXml.iter('nombre'):
                nombre1 = nombreXml.text
            for edadXml in dpXml.iter('edad'):
                edad1 = edadXml.text
            nuevoDP = Datos_Personales(nombre1,edad1)
            nuevoPaciente.datos_personales.append(nuevoDP)
    return listaPacientesDesdeXml

menu()
