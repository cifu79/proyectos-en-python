def enumeracion_exhaustiva(objetivo):
    respuesta = 0
    
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
        
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
        
        
def apriximacion_soluciones(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
        
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        
        
def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0,objetivo)
    respuesta = (alto + bajo) / 2
    
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo} alto={alto} respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    

def run():
    print("="* 46)
    print("Programa para hallar raiz una raiz cuadrada")
    print("="*46)

    menu = """
    Este programa te permite hallar la raiz cuadra de cualquier numero,
    1 - enumeracion exahustiva
    2 - aproximacion de soluciones
    3 - busqueda binaria
    Elige (1,2,3)  """
    
    menu = int(input(menu))
    
    if menu == 1:
        
        enumeracion_exhaustiva(objetivo = int(input("A cual numero le quieres sacar raiz cuadrada con enumeracion exhaustiva: ")))
    elif menu == 2:
        apriximacion_soluciones(objetivo = int(input("A cual numero le quieres sacar raiz cuadrada con aproximacion de soluciones: ")))
    elif menu == 3:
        busqueda_binaria(objetivo = int(input("A cual numero le quieres sacar raiz cuadrada con busqueda binaria: ")))
    else:
        print('La opcion que elegiste no esta disponible')

if __name__ == '__main__':
    run()