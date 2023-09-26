import random

""" este modulo juega cachipun"""
opciones = ["piedra", "papel", "tijera"]
#lista de las opciones 
def juego_cachipun(humano,computador): 
    #inicia el juego
    while  humano not in opciones:
        print("valor invalido: escriba un valor entre piedra, papel o tijera")
        humano = input("Ingrese la jugada: ")
        humano = humano.lower()
    print("El jugador eligio: ",humano)
    print("La computadora eligio:  " ,computador)
    if (humano=="papel" and computador=="piedra" ) or (humano=="tijera" and computador=="papel") or (humano=="piedra" and computador=="tijera"):
        print("TU ERES EL GANADOR")
    elif humano==computador:
        print("ES UN EMPATE VUELVE A JUGAR PARA GANAR")
    else: 
        print("GANO LA COMPUTADORA")
    print("el juego termino")



if __name__=="__main__":
    print("empezamos a jugar cachipun")
    print("Ingrese la jugada: piedra ,  papel , tijeras")
    humano= input("ingrese su jugada: ")
    humano=humano.lower()
    computador =["piedra" , "papel" , "tijeras"]
    computador=random.choice(opciones)
    resultado=juego_cachipun(humano,computador)
    print("el humano jugo: ",humano)
    print("el computador jugo: ", computador)
    print(resultado)

