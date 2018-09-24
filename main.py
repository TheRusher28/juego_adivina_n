__author__ = 'TheRusher28'
__mantainer__ = 'TheRusher28'
__email__ = 'therusher28@gmail.com'
__status__ = 'Beginner'

numero_elegido = input("¿Qué número escoges para que tu amigo lo adivine? (Del 0 al 100) ")
numero_adivinado = 0
time = 10
if float(numero_elegido) >= 0 and float(numero_elegido) <= 100:
    while time >= 0:
        time -= 1
        print("Numero a adivinar {} (Que tu compañero no lo vea)" .format(numero_elegido))
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
    while float(numero_adivinado) != float(numero_elegido):
        numero_adivinado = input("Adivina el numero : ")
    if numero_adivinado == numero_elegido:
        print("¡Has adivinado el numero!")
