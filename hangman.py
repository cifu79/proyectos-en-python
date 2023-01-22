import random
import os


def run():
    IMAGENES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    
    DB = ['python','java','pearl','javascript','go','rust','ruby']
    
    palabra = random.choice(DB)
    espacios = ['_'] * len(palabra)
    intentos = 6
    
    while True:
        os.system('clear')
        for caracter in espacios:
            print(caracter, end='')
        print(IMAGENES[intentos])
        letra = input('Escribe una letra para completar la palabra ').lower()
        
        encontrar = False
        
        for indice,caracter in enumerate(palabra):
            if caracter == letra:
                espacios[indice] = letra
                found = True
        

        if not encontrar:
            intentos -= 1
            
        if '_' not in espacios:
            os.system('clear')
            print('Ganaste')
            break
        
        if intentos == 0:
            os.system('clear')
            print('Perdiste')
            break
        
if __name__ == '__main__':
    run()