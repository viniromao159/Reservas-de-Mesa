from os import system

def menu():
    print("------------- Menu de reserva -----------")
    print("-> 0 - Verificar mesas disponiveis ------")
    print("-> 1 - Adicionar mesa -------------------")
    print("-> 2 - Remover mesa ---------------------")
    print("-> 3 - Adicionar Reserva ----------------")
    print("-> 4 - Remover Reserva ------------------")
    print("-> 5 - Limpar tela ----------------------")
    print("-> 6 - Finalizar programa ---------------")
    print("-----------------------------------------")
    
def mostrar_mesas(restaurante):
    if len(restaurante) == 0:
        print("Não tem mesa.")
    else:
        for mesa in restaurante:
            print(f'\nMesa {mesa['mesa']}: ')
            
            for horario, reserva in mesa['Reserva'].items():
                print(f'{horario} -> {reserva}')

def quebralinha():
    print()  

def limparTela():
    system('cls')