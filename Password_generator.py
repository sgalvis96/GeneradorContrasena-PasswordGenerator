import random
class generator:
##################################################################
    def abcd():
        a = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0"
        ab = a.split()              #METODO PARA TENER TODAS LAS OPCIONES DE CARACTERES
        return ab
##################################################################
    def largo():
        caract = 12                     #METODO PARA DEFINIR LA LONGITUD DE LA CONTRASENA
        while caract > 11 or caract < 0:
            caract = int(input("Que longitud desea la contrasena?(1-10): "))
        return caract
###################################################################
    abcedario = abcd()    #METODO PARA ALMACENAR UNA LISTA DE TODAS LAS OPCIONES DE CARACTERES
    ###############
    longi = largo() #METODO PARA OBTENER LA LONGITUD DE LA CONTRASENA
    pwd  =  "".join(random.sample(abcedario,longi ))      #AQUI HAY VARIAS SENTENCIAS DE PYTHON (join = UNIR LA LISTA EN UNA SOLA PALABRA
    print("Contrasena: ",pwd)                                                            # (random = obtener un numero aleatorio )
                                                                                         # (sample = unir los caracteres de manera aleatoria)
                                                                                         # ( abcedario,longi = primero se pone el array y despues la longitud del mismo)