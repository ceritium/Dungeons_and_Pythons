import time # Módulo que nos permite darte tiempo de lectura al lector con método time.sleep(segundos)
import inquirer # pip install inquirer
import re
import argparse

"""

Los elementos razas y profesiones están predefinidos ya que con funciones en el código permitiremos que el jugador
pueda seleccionar los valores dentro para poder hacer uso de ellos a medida que avance el juego

"""

razas = ["humano", "humana", "elfo", "elfa", "enano", "enana"]
profesiones = ["guerrero", "hechicero", "pícaro", "guerrera", "hechicera", "pícara"]

"""

Estas funciones nos sirven para iniciar la presentación de la aventura y crear el personaje del jugador

"""

def wait():
    if fast == False:
        time.sleep(1)

def linebreaker(): #Se usa para separar visualmente episodios del juego
        wait()
        print(" ")
        x = " *** "
        print(x*15)
        print(x*15)
        print(" ")


def introduccion(): #Texto de narrativa: presentación de juego
    wait()
    print("Bienvenido a Dungeons&Pythons. Estás a punto de embarcarte en una emocionante aventura.")
    print(" ")
    wait()
    print("Como aventurero, podrás ponerte a prueba como héroe y ganar renombre en una tierra inhóspita")
    print(" ")
    wait()
    print("Pero primero, necesitarás decirme quien eres para poder dar tu primer paso...")
    print(" ")


"""
Estas funciones lanzan textos de narrativa personalizando el juego según opciones elegidas de personaje

"""

def inicio_raza(): #Texto de narrativa: origen del personaje según raza
    print(f"Saludos {nombre}, valiente {raza} que busca fortuna como {profesion}")

    if re.match(r'.*human.*', raza):
            wait()
            (" ")
            print("Vienes de la capital del Reino, con la idea de derrotar al dragón del lago")
    elif re.match(r'.*elf.*', raza):
            wait()
            (" ")
            print("Vienes desde lo más profundo del bosque, con la idea de derrotar al dragón del lago")
    elif re.match(r'.*enan.*', raza):
            print(" ")
            wait()
            print("Vienes desde las entrañas de la montaña, con la idea de derrotar al dragón del lago")

def inicio_profesion(): #Texto de narrativa: contexto según profesión
    if re.match(r'.*guerrer.*', raza):
            wait()
            print(" ")
            print("Piensas que con tu fuerza, podrás hacer frente a la amenaza que se cierne sobre tu pueblo")
    elif re.match(r'.*hechicer.*', raza):
            wait()
            print(" ")
            print("Piensas que con tu magia, te valdrás para contener este peligro que amenaza a los tuyos")
    elif re.match(r'.*picar.*', raza):
            wait()
            print(" ")
            print("Confías en que tus artimañas sean suficientes para cobrar la recompensa por el monstruo")

"""
Estas funciones permiten avanzar en la narrativa y crear el arma como primer objeto adquirido por el personaje

"""
def interludio(): #Texto de narrativa: trama continua
    wait()
    print("El camino hacia el lago te lleva varíos días, atravesando toda clase que parajes")
    print(" ")
    wait()
    print("El dragón ha causado muchos daños allá por donde pasas. Toda clase de parajes han sido reducidos a cenizas. Es una amenaza que ha de ser eliminada con premura")
    print(" ")
    wait()
    print("Antes de alcanzarlo, tienes que asegurarte y revisar tu inventario. Sin la adecuada preparación, seguramente morirás")
    print(" ")
    wait()

def weapon(profesion): #Crea una biblioteca con un elemento {profesión:arma}

    arma = {}
    if profesion == "guerrero" or profesion == "guerrera":
        arma[profesion] = "espada"
    elif profesion == "hechicero" or profesion == "hechicera":
        arma[profesion] = "pergamino"
    elif profesion == "pícaro" or profesion == "pícara":
        arma[profesion] = "arco y flechas"

    print(f"Recuerdas qué trajiste tu inseparable {arma[profesion]} contigo y crees que tu maestría en su manejo te será suficiente para derrotar a la bestia")
    wait()
    print(" ")
    return arma

"""

Estas funciones avanzan en la narrativa y presentan elecciones en la trama. Según el jugador elija repercutirá de una forma
u otra en el desenlace de la aventura

"""


def antes_del_lago(): #Texto de narrativa: avanza la trama
    wait()
    print(" ")
    print("Llegas al Bosque del Descanso, una arboleda cercana al lago del dragón. Un lugar anteriormente frondoso que ha sido reducido a cenizas casi en su totalidad")
    wait()
    print(" ")
    print("Solo la arboleda te separa de tu encuentro inevitable con tu monstruoso némesis. Quizás sea buena idea buscar aquí algún sitio para descansar; o puede que te sientas con energías para continuar tu viaje y acabar con todo esto cuanto antes")
    wait()

def descanso(): #Elección de camino. Permite actualizar el inventario
    print(" ")
    print("Pulsa 1 para buscar un lugar para descansar")
    print(" ")
    print("Pulsa 2 para seguir tu camino")
    print(" ")


    while True:
        try:
            opcion_1 = int(input("Qué harás? "))
            inventario = []
            if opcion_1 == 1:
                print("Encuentras una cueva que parece bastante segura. La exploras y estableces ahí tu campamento. No duermes mucho debido a los nervios, pero encuentras entre las piedras una pócima de salud que debió de pertenecer a otro aventurero... Algo es algo")
                inventario.append("pócima")
                break
            elif opcion_1 == 2:
                print("No crees que sea buena idea parar ahora, sobretodo tan cerca de la amenaza. Lo más probable es que el dragón te descubra aquí mientras descansas y te ataque por sorpresa. Así que lo más sensato es continuar tu camino")
                break
            else:
                print("Sé que el agotamiento te distrae, pero tienes que elegir: 1 o 2 ")
        except ValueError:
            print("Sé que el agotamiento te distrae, pero tienes que elegir: 1 o 2 ")

    return inventario


"""
Estas definiciones se usan para desencadenar el encuentro final en la aventura. Según los inputs usados previamente el
desenlace de la aventura tendrá un final u otro

"""


def encuentro_dragon(): #Texto de narrativa: introducción al encuentro final
    wait()
    print(" ")
    print("Sigues caminando toda la noche hacia el lago. Durante horas has olido el azufre que despide el dragón y a cada paso que das, se intensifica.")
    wait()
    print(" ")
    print("Pasan horas y horas, pero tu estado de alerta hacen que parezcan solo minutos.")
    wait()
    print(" ")
    print("Cuando te quieres dar cuenta, ya estás a los pies de la gigantesca charca en donde habita la bestia")
    wait()


def antes_del_combate(): #Permite acceder a la ficha de personaje si se desea o continuar tal cual
    print(" ")
    print("Pulsa 1 si quieres revisar tu ficha de personaje antes del combate para saber de lo que dispones")
    print(" ")
    print("Pulsa 2 si vas con todo. No te hace falta revisar nada")

    while True:
        try:
            opcion = int(input("¿Qué harás?: "))
            if opcion == 1:
                wait()
                print(" ")
                print(f"Nombre: {nombre}")
                print(f"Raza: {raza.capitalize()}")
                print(f"Profesión: {profesion.capitalize()}")
                print(f"Arma: {arma[profesion]}")
                print(f"Inventario: {inventario}")
                print(" ")
                break
            elif opcion == 2:
                wait()
                print(" ")
                print(f"Bueno {nombre}, si crees que no necesitas revisar vamos allá. ¡El mundo pertenece a los arrojados!")
                break
            else:
                wait()
                print(" ")
                print("Sé que el agotamiento te distrae, pero tienes que elegir: 1 o 2 ")
                wait()
                print(" ")
                opcion = int(input("¿Qué harás? "))
        except ValueError:
                    wait()
                    print(" ")
                    print("Sé que el agotamiento te distrae, pero tienes que elegir: 1 o 2 ")



def combate_final(): #Elección de acciones: suma de todas las elecciones hechas anteriores para dar dos finales: ganar o vencer
    wait()
    print(" ")
    print("Sientes que es el momento, así que gritas al cielo: ¡DRAGON! ¡HE VENIDO A POR TI")
    wait()
    print(" ")
    print("De las profundidades del lago, emerge la criatura. Roja como la sangre, grande como un castillo")
    wait()
    print(" ")
    print("Sin tiempo para vacilar, se avalanza hacia ti. ¡Es el momento de la verdad!")
    wait()
    (" ")
    print(f"Pulsa 1 si quieres usar tu {arma[profesion]} contra la criatura")
    print("Pulsa 2 si decides esquivar el ataque del dragón y luego contraatacar")

    wait()
    print(" ")
    x = " *** "
    print(x*15)
    print(x*15)
    print(" ")

    while True:
        try:
            opcion = int(input("¿Qué harás? "))
            if opcion == 1:
                wait()
                (" ")
                print(f"Te ensarzas en una batalla épica con la criatura. La lucha dura una eternidad. Tu {arma[profesion]} contra sus fauces y colmillos")
                wait()
                (" ")
                print(f"Tus energías se agotan y crees que la derrota es inminente")
                wait()
                (" ")
                print(f"Sin embargo, tu experiencia como {profesion} te permite al final del todo encontrar un punto débil")
                if profesion == "guerrero" or profesion == "guerrera":
                                                     wait()
                                                     (" ")
                                                     print(f"En un momento de debilidad del enemigo, clavas tu espada entre sus escamas alcanzado su corazón")
                                                     wait()
                                                     (" ")
                                                     print("¡Enhorabuena! ¡Has vencido al dragón!")
                                                     break
                elif profesion == "hechicero" or profesion == "hechicera":
                                                     wait()
                                                     (" ")
                                                     print(f"En un momento de debilidad del enemigo, lanzas una bola de fuego que derrite las escamas de su pecho, calcinando su corazón")
                                                     wait()
                                                     (" ")
                                                     print("¡Enhorabuena! ¡Has vencido al dragón!")
                                                     break
                elif profesion == "pícaro" or profesion == "pícara":
                                                     wait()
                                                     (" ")
                                                     print(f"En un momento de debilidad del enemigo, te escabulles entre sus garras para lanzar una flecha que se clava directamente en su corazón")
                                                     wait()
                                                     (" ")
                                                     print("¡Enhorabuena! ¡Has venido al dragón!")
                                                     break
            elif opcion == 2:
                    valor = "pócima"
                    if valor in inventario:
                                         wait()
                                         (" ")
                                         print("Esquivas el ataque pero las garras del dragón te rozan mortalmente")
                                         wait()
                                         (" ")
                                         print("Por suerte, puedes usar la poción que encontraste en la cueva y te repones")
                                         wait()
                                         (" ")
                                         print("Tomas aire... y lanzas tu contraataque")
                    else:
                         wait()
                         (" ")
                         print("Esquivas el ataque pero las garras del dragón te rozan mortalmente... que bien te habría venido una poción de salud ahora mismo")
                         wait()
                         (" ")
                         print("Caes al suelo, malherido... Lo último que ves son las fauces del monstruo acercandose, amenazante. Hoy serás su cena.")
                         wait()
                         (" ")
                         print("¡Lo siento! ¡Has sido devorado por la bestia y ahora tu pueblo está condenado")
                         break
            else:
                wait()
                print(" ")
                print("Sé que el agotamiento te distrae, pero tienes que elegir: 1 o 2 ")
                wait()
                print(" ")
                opcion = int(input("¿Qué harás? "))
        except ValueError:
                    wait()
                    print(" ")
                    print("Sé que el agotamiento te distrae, pero tienes que elegir: 1 o 2 ")


def createPlayer():
    questions = [
        inquirer.Text("nombre", message="¿Cuál es tu nombre?"),
        inquirer.List(
            "raza",
            message="Elige tu raza",
            choices=razas
        ),
        inquirer.List(
            "profesion",
            message="Elige tu profesión",
            choices=profesiones
        ),
    ]

    answers = inquirer.prompt(questions)
    nombre = answers["nombre"]
    raza = answers["raza"]
    profesion = answers["profesion"]
    return nombre, raza, profesion

"""
Jerarquía de funciones para hacer correr la aventura

"""

parser = argparse.ArgumentParser(
                    prog='Dugeons&Pythons',
                    description='Juego de aventuras en Python',
                    epilog='¡Que te diviertas!')
parser.add_argument('-f', '--fast', action='store_true', help='No espera entre escenas')
args = parser.parse_args()
fast = args.fast

introduccion()
linebreaker()
nombre, raza, profesion = createPlayer()
linebreaker()
inicio_raza()
inicio_profesion()
linebreaker()
interludio()
arma = weapon(profesion)
linebreaker()
antes_del_lago()
inventario = descanso()
linebreaker()
encuentro_dragon()
antes_del_combate()
linebreaker()
combate_final()
