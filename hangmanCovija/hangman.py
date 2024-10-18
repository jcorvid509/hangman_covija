# Juego del ahorcado
# PEdimos una palabra al primer jugador
# Entramos en un bucle donde pedimos al segundo jugador una letra
# y si existe en la palabra, mostramos su posición
# el bucle termina cuando la palabra esté completa 
# o cuando se llegue 10 fallos


def hangman():
    
    import os                           # importamos os para borrar la pantalla
    import pygame                       # importamos pygame para reproducir sonidos
    import re                           # importadmos re

    """Al tener la funcion moneco dentro del archivo no es necesario"""
    #import sys                          #importamos sys para cambiar la ruta de importación de archivos py
    #sys.path.append(r'Python\pruebas')  #cambiamos la ruta
    #import moneco                       #importamos moneco de la ruta anterior

    os.system("cls")    # limpiamos la pantalla


    cw = "n"    # la variable cw no indica si se ha escrito bien la palabra
    while cw != ("y" or "Y"):                                           # Preguntamos por la palabra, si se ha equivocado vuelve a empezar
        os.system("cls")
        word = input("Introduce la palabra del ahorcado: ")             # pedimos la palabra y la guardamos en word
        if len(word) == 0 or " " in word:                               # si la palabra tiene espacios o vacios, volvemos al bucle
            cw = "n"
        else:                                                           # si no, continuamos con el programa
            cw = input("Tu palabra es " + word + " es correcta? (y/n)") # preguntamos si la palabra es correcta
                                                                        # si lo es salimos del bucle, si no volvemos al bucle   

    word = word.lower() # hacemos cualquier letra que se escriba sea en minuscula
    os.system("cls")    # limpiamos la pantalla para que el segundo jugador no vea la palabra
    #print(word)        #zona de testeo

    word2 = len(word) * "_" # word2 será la variable intermedia, guardará el resultado
                            # empezará como el largo de la palabra con guiones "_"
    fails = 0               # fails será la variable que guardará el número de fallos 0/10
    state = 0               # state será el estado de la pregunta, acierto = 1, fallo = 0
    err = []                # guardará las letras ya utilizadas y erradas

    while fails < 10:       # hasta que no se alcancen los 10 fallos no se sale del juego
        
        word3 = ""                  # en cada ciclo, word3 se borrará, esta variable será la que mostraremos por pantalla con espacios
        for i in range(len(word)):  # recorremos la palabra escrita
            word3 += word2[i] + " " # añadimos las letras de la palabra (word2) segidas de un espacio
                                    # recordemos que word2 es la palabra con guiones "_"
                                    # (word = "hola", word2 =  "_____", word3 =  " _ _ _ _ ")
            #print(word3)            #zona de testeo

        print("La palabra es: " + word3)        # mostramos la palabra con espacios
        print("")
        print("Has errado en las letras", err)  # mostramos las letras erradas
        print("")
        l = input("Introduce una letra: ")      #  pedimos una letra
        os.system("cls")                        # al introducir la letra limpiamos la pantalla

        if len(l) > 1:                              # si introduce mas de una letra
            print("Pon solo una letra no varias")
            state = 0
        elif l == " " or l == "":                   # si se intruce un espacio o se deja vacio
            print("No pongas espacios,o dejes vacia la casilla, eso no vale")
            state = 0
        elif l in err:                              # si la letra ya ha sido introducida y errada
            print("Ya has intentado esa letra, prueba con otra")
            state = 0
        elif l in word2:                            # si la letra ha sido acertada
            print("Si, ya sabemos que esa letra está en la palabra, no hace falta que la vuelvas a probar")
            state = 1
        elif l in word:                             # si la letra está en la palabra
            print("Has acertado, la letra "+ l + " esta en la palabra")
            state = 1
            for i in re.finditer(l, word):          # recorremos la palabra para encontrar las letras
                s = int(i.start())                  # guardamos la posición de la letra
                e = int(i.end())
                word2 = word2[:s]+ l+ word2[e:]     # cambiamos "_" por la letra acertada en word2
                #print(word2)                       #zona de testeo
        else:                                       #  si la letra no está en la palabra
            fails += 1                              # aumentamos el numero de fallos
            state = 0
            err.append(l)                           # añadimos la letra a la lista de letras erradas
            print("")
        
        #word3 = word2.replace(" ","")               # zona de testeo 
        #print(word3)
            
        moneco(fails, state)                        # llamamos a la funcion moneco, la cual nos muestra el muñeco del ahorcado
                                                    # y reproduce el sonido correspondiente
        print("")
        print("Tienes", fails,"fallos")             # mostramos el numero de fallos
        print("")

        if fails == 10:                                                                 # si se ha superdaro el limite de fallos
            print("Has fallado, el juego se ha terminado, la palabra era: " + word)     # mostramos el mensaje de fallos 

        if word2 == word:   # si la palabra que obtengamos es igual a la escrita, abremos acertado la palabra
            
            print("Enhorabuena, la palabra era", word2, "ganaste")
            if fails <= 3:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\0.mp3')    # sonido de victoria con menos de 4 fallos
            elif fails <= 7:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\4.mp3')    # sonido de victoria con 4 a 7 fallos
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\8.mp3')    # sonido de victoria EPICARDO con mas de 7 fallos
            
            pygame.mixer.music.play()   # reproducimos el sonido de victoria
            fails = 10
        
        if fails == 10:                                                                 # si se ha superado el limite de fallos
            print("")
            l = input("Pulsa y para seguir jugando o cualquier otra tecla para cerrar: ") # preguntamos si quiere seguir jugando
            if l.lower() == "y":
                hangman()                                                               # volvemos a empezar el juego
            else:
                os.system("cls")                                                        # limpiamos la pantalla





def moneco(fail, state):    # función que imprime el muñeco y hace sonar los fallos y aciertos
    
    import pygame       # importamos la libreria de pygame, la cual nos ayuda a emitir sonidos
    pygame.mixer.init() # iniciamos el mixer de pygame, el cual nos permite reproducir sonidos
   
    match fail: # fail representa el numero de fallos
        case 1:
            
            if state == 0:  # dependiendo de si ha fallado o no la pregunta cargamos un sonido u otro
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\1.mp3')      # sonido si falla teniendo "fail" fallos
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')    # sonido si acierta teniendo "fail" fallos
           
            pygame.mixer.music.play()   #reproducimos el sonido
            # imprime el ahorcado
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("_______")
        case 2:
            if state == 0:
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\2.mp3')
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print(" ")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_____")
        case 3:
            if state == 0:
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\3.mp3')
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print(" _____ ")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_____")
        case 4:
            if state == 0:
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\4.mp3')
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print(" _____ ")
            print(" |   | ")
            print(" |")
            print(" |")
            print(" |")
            print("_|_____")
        case 5:
            if state == 0:
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\5.mp3')
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |")
            print(" |")
            print("_|_____")
        case 6:
            if state == 0:
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\6.mp3')
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |   |")
            print(" |")
            print("_|_____")
        case 7:
            if state == 0:
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\7.mp3')
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /|")
            print(" |")
            print("_|_____")
        case 8:
            if state == 0:
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\8.mp3')
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /|\\")
            print(" |")
            print("_|_____")
        case 9:
            if state == 0:
                pygame.mixer.music.load(r'hangmanCovija\mp3\error\9.mp3')
            else:
                pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /|\\")
            print(" |  /")
            print("_|_____")
        case 10:
            # ahorcado si perdemos
            pygame.mixer.music.load(r'hangmanCovija\mp3\error\10.mp3')
            pygame.mixer.music.play()
            print(" _____ ")
            print(" |   | ")
            print(" |   O ")
            print(" |  /|\\")
            print(" |  / \\")
            print("_|_____")
            print("")
            print("HAS MUELTO")
        case _:
            #ahorcado si no tenemos fallos
            pygame.mixer.music.load(r'hangmanCovija\mp3\success\_.mp3')
            pygame.mixer.music.play()
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")






hangman()
