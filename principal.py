import cachipun
import seleccion
from login import *
def main():
    usario = login()
    print("bienvenido al inicio de sesion para el juego cachipun ")
    if usario== True:
        print("bienvenido al juego cachipun contra el computador")
        print("opciones: piedra, papel, tijera")
        opciones = ["opciones: piedra, papel, tijera"]
        humano = input("ingrese su jugada:  ")
        humano=humano.lower()
        #entrada del jugador 
        computador=seleccion.seleccionar()
        #Se invoca la modulo cachipun y su funcion 
        cachipun.juego_cachipun(humano, computador)
    else:
        print("vuelve a intetar")

if __name__ == "__main__": 
    main()