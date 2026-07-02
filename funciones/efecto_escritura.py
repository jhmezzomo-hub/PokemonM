import sys
from time import sleep

def print_animado(texto, velocidad=0.02, salto=True):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        sleep(velocidad)
    
    if salto:
        print()